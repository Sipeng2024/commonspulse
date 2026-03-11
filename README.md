# CommonsPulse

**CommonsPulse** is an evidence-based portfolio monitoring agent for grant programs, DAOs, and public-goods funds.

Instead of waiting for quarterly manual updates, CommonsPulse continuously pulls public project signals (GitHub activity, releases, issue load) and turns them into:

- a compact markdown report for operators
- a JSON snapshot for downstream automation
- explicit weak/medium/strong signals for upstream portfolio monitoring

## Why this exists

Grant operators usually face the same problem:

- project updates are scattered across repos, docs, blogs, and social channels
- milestone follow-up is manual and slow
- problems are discovered late
- communities cannot easily verify whether a project is still progressing

CommonsPulse does **not** auto-score grants, auto-trigger payments, or act as a reviewer workbench. It focuses on one narrower upstream job:

> Collect public evidence, normalize project signals, and emit reusable portfolio snapshots.

That makes it safer, more auditable, and more reusable across different funding programs.

## MVP scope

Current MVP monitors:

- latest GitHub commit recency
- latest GitHub release recency
- open issue load
- stars/forks/basic repo metadata

It outputs a per-project snapshot plus portfolio-level health counts.

## Snapshot schema

Each project snapshot is shaped as an upstream evidence object, not just a loose report blob:

```json
{
  "name": "Vyper",
  "sources": [
    {"kind": "github_repo", "url": "https://github.com/vyperlang/vyper", "fetched_at": "2026-03-11T09:00:00Z"}
  ],
  "evidence": {
    "repo": {
      "repo_url": "https://github.com/vyperlang/vyper",
      "open_issues": 590
    },
    "latest_commit": {
      "timestamp": "2026-03-09T19:22:21Z",
      "url": "https://github.com/vyperlang/vyper/commit/...",
      "days_since": 2
    }
  },
  "derived_signals": {
    "development": {
      "level": "strong",
      "rationale": "Latest commit was 2 days ago.",
      "source_refs": ["https://github.com/vyperlang/vyper/commit/..."],
      "threshold": {"strong_lte_days": 14, "medium_lte_days": 45}
    }
  },
  "downstream_use": [
    "portfolio_monitoring",
    "dashboard_ingestion",
    "review_workbench_input"
  ]
}
```

That schema is the point: CommonsPulse is meant to emit reusable, traceable upstream snapshots that downstream dashboards or review tools can consume.

## Thresholds

Current MVP thresholds are intentionally simple and explicit:

- `development`: strong if latest commit <= 14 days, medium if <= 45 days, else weak
- `release_cadence`: strong if latest release <= 60 days, medium if <= 180 days, else weak
- `maintainability`: weak if open issues > 1000, otherwise medium

These are starter heuristics, not grant decisions. They are documented so the project reads like infrastructure, not a mystery scoring box.

## Quick start

```bash
cd /tmp/commonspulse
uv run commonspulse config/projects.example.yml --out output/report.md --json output/report.json
```

## Example output

Generated files:

- `output/report.md`
- `output/report.json`

The JSON output is the canonical machine-readable artifact. The markdown report is just a human-friendly projection of the same snapshot.

Example project config:

```yaml
projects:
  - name: Vyper
    homepage: https://vyperlang.org/
    github_repo: vyperlang/vyper
```

## Roadmap

- add RSS/blog/X/website change detection
- add richer evidence schemas for portfolio events
- publish machine-readable snapshots for downstream tools
- expose a lightweight monitoring dashboard
- support configurable thresholds by project type

## Why this fits GCC

GCC explicitly identified impact evaluation as a real pain point: portfolio tracking is repetitive, high-friction, and often delayed.

CommonsPulse turns that into an open upstream workflow:

1. ingest public evidence
2. normalize recent project activity into structured signals
3. emit weak/medium/strong portfolio snapshots
4. feed downstream review tools or human workflows

This is useful for GCC, but also reusable for any public grant program.

## License

MIT
