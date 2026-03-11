from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, asdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx
import yaml


@dataclass
class ProjectSnapshot:
    name: str
    homepage: str | None
    github_repo: str | None
    tags: list[str]
    evidence: dict[str, Any]
    signals: dict[str, str]
    summary: str


def _github_headers() -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "User-Agent": "commonspulse/0.1.0",
    }


def _get_json(url: str) -> Any:
    with httpx.Client(timeout=20.0, follow_redirects=True, headers=_github_headers()) as client:
        resp = client.get(url)
        resp.raise_for_status()
        return resp.json()


def _iso_to_days(iso_text: str | None) -> int | None:
    if not iso_text:
        return None
    dt = datetime.fromisoformat(iso_text.replace("Z", "+00:00"))
    return (datetime.now(UTC) - dt.astimezone(UTC)).days


def _bucket(days: int | None, *, good: int, warn: int) -> str:
    if days is None:
        return "unknown"
    if days <= good:
        return "strong"
    if days <= warn:
        return "medium"
    return "weak"


def _summarize(name: str, signals: dict[str, str], evidence: dict[str, Any]) -> str:
    strengths = [k for k, v in signals.items() if v == "strong"]
    warnings = [k for k, v in signals.items() if v == "weak"]
    parts: list[str] = []
    if strengths:
        parts.append(f"{name} shows strong signal in {', '.join(strengths)}")
    if warnings:
        parts.append(f"but weak signal in {', '.join(warnings)}")
    if evidence.get("open_issues", 0) > 500:
        parts.append("and may require triage bandwidth")
    if not parts:
        parts.append(f"{name} has mixed activity signals")
    return " ".join(parts) + "."


def _snapshot_project(project: dict[str, Any]) -> ProjectSnapshot:
    repo = project.get("github_repo")
    evidence: dict[str, Any] = {}
    signals: dict[str, str] = {}

    if repo:
        repo_meta = _get_json(f"https://api.github.com/repos/{repo}")
        commits = _get_json(f"https://api.github.com/repos/{repo}/commits?per_page=5")
        releases = _get_json(f"https://api.github.com/repos/{repo}/releases?per_page=3")
        latest_commit_at = commits[0]["commit"]["author"]["date"] if commits else None
        latest_release_at = releases[0]["published_at"] if releases else None
        commit_days = _iso_to_days(latest_commit_at)
        release_days = _iso_to_days(latest_release_at)
        evidence.update(
            {
                "stars": repo_meta.get("stargazers_count"),
                "forks": repo_meta.get("forks_count"),
                "open_issues": repo_meta.get("open_issues_count"),
                "latest_commit_at": latest_commit_at,
                "latest_release_at": latest_release_at,
                "default_branch": repo_meta.get("default_branch"),
                "repo_url": repo_meta.get("html_url"),
                "description": repo_meta.get("description"),
            }
        )
        signals["development"] = _bucket(commit_days, good=14, warn=45)
        signals["release_cadence"] = _bucket(release_days, good=60, warn=180)
        signals["maintainability"] = "weak" if (repo_meta.get("open_issues_count") or 0) > 1000 else "medium"
    else:
        signals = {"development": "unknown", "release_cadence": "unknown", "maintainability": "unknown"}

    summary = _summarize(project["name"], signals, evidence)
    return ProjectSnapshot(
        name=project["name"],
        homepage=project.get("homepage"),
        github_repo=repo,
        tags=project.get("tags", []),
        evidence=evidence,
        signals=signals,
        summary=summary,
    )


def build_snapshot(config_path: Path) -> dict[str, Any]:
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    projects = [_snapshot_project(item) for item in config.get("projects", [])]
    signal_counts = Counter(signal for project in projects for signal in project.signals.values())
    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "project_count": len(projects),
        "portfolio_health": dict(signal_counts),
        "projects": [asdict(project) for project in projects],
    }


def render_markdown(snapshot: dict[str, Any]) -> str:
    lines = [
        "# CommonsPulse Report",
        "",
        f"Generated at: {snapshot['generated_at']}",
        f"Projects monitored: {snapshot['project_count']}",
        "",
        "## Portfolio health",
        "",
    ]
    for key, value in snapshot["portfolio_health"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Project snapshots", ""])
    for project in snapshot["projects"]:
        lines.extend(
            [
                f"### {project['name']}",
                f"- Summary: {project['summary']}",
                f"- Repo: {project['evidence'].get('repo_url', 'n/a')}",
                f"- Homepage: {project.get('homepage') or 'n/a'}",
                f"- Signals: {project['signals']}",
                f"- Evidence: latest commit {project['evidence'].get('latest_commit_at', 'n/a')}, latest release {project['evidence'].get('latest_release_at', 'n/a')}, open issues {project['evidence'].get('open_issues', 'n/a')}",
                "",
            ]
        )
    lines.extend(
        [
            "## Why this matters for grant programs",
            "",
            "- Tracks public evidence instead of relying on quarterly manual follow-up.",
            "- Flags projects that need human review without pretending to replace grant managers.",
            "- Produces auditable markdown + JSON outputs that can feed dashboards, GitHub comments, or governance workflows.",
            "",
        ]
    )
    return "\n".join(lines)
