# CommonsPulse

**CommonsPulse** is an evidence-based portfolio monitoring agent for grant programs, DAOs, and public-goods funds.

Instead of waiting for quarterly manual updates, CommonsPulse continuously pulls public project signals (GitHub activity, releases, issue load) and turns them into:

- a compact markdown report for humans
- a JSON snapshot for downstream automation
- explicit weak/medium/strong signals for human review

## Why this exists

Grant operators usually face the same problem:

- project updates are scattered across repos, docs, blogs, and social channels
- milestone follow-up is manual and slow
- problems are discovered late
- communities cannot easily verify whether a project is still progressing

CommonsPulse does **not** auto-score grants or auto-trigger payments. It focuses on one narrower job:

> Collect public evidence, summarize progress, and flag projects that deserve human attention.

That makes it safer, more auditable, and more reusable across different funding programs.

## MVP scope

Current MVP monitors:

- latest GitHub commit recency
- latest GitHub release recency
- open issue load
- stars/forks/basic repo metadata

It outputs a per-project snapshot plus portfolio-level health counts.

## Quick start

```bash
cd /tmp/commonspulse
uv run commonspulse config/projects.example.yml --out output/report.md --json output/report.json
```

## Example output

Generated files:

- `output/report.md`
- `output/report.json`

Example project config:

```yaml
projects:
  - name: Vyper
    homepage: https://vyperlang.org/
    github_repo: vyperlang/vyper
```

## Roadmap

- map project evidence to explicit grant milestones
- add RSS/blog/X/website change detection
- publish GitHub Issue comments automatically for review teams
- expose a small dashboard for fund operators
- support human override + confidence explanations

## Why this fits GCC

GCC explicitly identified impact evaluation as a real pain point: portfolio tracking is repetitive, high-friction, and often delayed.

CommonsPulse turns that into an open workflow:

1. ingest public evidence
2. summarize recent project activity
3. flag weak signals
4. hand off to human reviewers

This is useful for GCC, but also reusable for any public grant program.

## License

MIT
