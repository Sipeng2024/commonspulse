# CommonsPulse Report

Generated at: 2026-03-11T09:32:54.610913+00:00
Projects monitored: 3

## Portfolio health

- strong: 4
- weak: 3
- medium: 1
- unknown: 1

## Project snapshots

### Vyper
- Summary: Vyper shows strong signal in development but weak signal in release_cadence.
- Repo: https://github.com/vyperlang/vyper
- Homepage: https://vyperlang.org/
- Derived signals: {'development': {'level': 'strong', 'rationale': 'Latest commit was 1 days ago.', 'source_refs': ['https://github.com/vyperlang/vyper/commit/0c7bdc19ca01ec82bcb6019741badf3f96aed703'], 'threshold': {'strong_lte_days': 14, 'medium_lte_days': 45}}, 'release_cadence': {'level': 'weak', 'rationale': 'Latest release was 265 days ago.', 'source_refs': ['https://github.com/vyperlang/vyper/releases/tag/v0.4.3'], 'threshold': {'strong_lte_days': 60, 'medium_lte_days': 180}}, 'maintainability': {'level': 'medium', 'rationale': 'Open issue count is 590.', 'source_refs': ['https://github.com/vyperlang/vyper'], 'threshold': {'weak_gt_open_issues': 1000, 'otherwise': 'medium'}}}
- Evidence: latest commit 2026-03-09T19:22:21Z, latest release 2025-06-18T20:09:23Z, open issues 590

### Python
- Summary: Python shows strong signal in development but weak signal in maintainability.
- Repo: https://github.com/python/cpython
- Homepage: https://www.python.org/
- Derived signals: {'development': {'level': 'strong', 'rationale': 'Latest commit was 0 days ago.', 'source_refs': ['https://github.com/python/cpython/commit/cf7c67b7c6b96527dfb0da2d6305923a92e3d766'], 'threshold': {'strong_lte_days': 14, 'medium_lte_days': 45}}, 'release_cadence': {'level': 'unknown', 'rationale': 'No release found.', 'source_refs': ['https://github.com/python/cpython/releases'], 'threshold': {'strong_lte_days': 60, 'medium_lte_days': 180}}, 'maintainability': {'level': 'weak', 'rationale': 'Open issue count is 9290.', 'source_refs': ['https://github.com/python/cpython'], 'threshold': {'weak_gt_open_issues': 1000, 'otherwise': 'medium'}}}
- Evidence: latest commit 2026-03-11T08:02:23Z, latest release None, open issues 9290

### uv
- Summary: uv shows strong signal in development, release_cadence but weak signal in maintainability.
- Repo: https://github.com/astral-sh/uv
- Homepage: https://docs.astral.sh/uv/
- Derived signals: {'development': {'level': 'strong', 'rationale': 'Latest commit was 0 days ago.', 'source_refs': ['https://github.com/astral-sh/uv/commit/5fca951e26383d30f38ce96f141ef7a9018a4327'], 'threshold': {'strong_lte_days': 14, 'medium_lte_days': 45}}, 'release_cadence': {'level': 'strong', 'rationale': 'Latest release was 4 days ago.', 'source_refs': ['https://github.com/astral-sh/uv/releases/tag/0.10.9'], 'threshold': {'strong_lte_days': 60, 'medium_lte_days': 180}}, 'maintainability': {'level': 'weak', 'rationale': 'Open issue count is 2706.', 'source_refs': ['https://github.com/astral-sh/uv'], 'threshold': {'weak_gt_open_issues': 1000, 'otherwise': 'medium'}}}
- Evidence: latest commit 2026-03-10T19:02:18Z, latest release 2026-03-06T21:24:15Z, open issues 2706

## Why this matters for grant programs

- Tracks public evidence instead of relying on quarterly manual follow-up.
- Flags projects that need human review without pretending to replace grant managers.
- Produces auditable markdown + JSON outputs that can feed dashboards, GitHub comments, or governance workflows.
