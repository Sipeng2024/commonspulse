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
