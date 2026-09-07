# orderstats

A very small Python library that computes aggregate statistics over a list of
customer orders.

## House rule

Every aggregation helper in `orderstats/stats.py` accepts an **empty** sequence
of orders and returns the neutral value for its aggregation rather than
raising. The `Returns:` clause of each docstring is the contract callers rely
on. `total_order_value` is the reference implementation of that convention.

## Usage

```python
from orderstats.models import Order
from orderstats.stats import total_order_value

orders = [Order(order_id="ORD-1", value=10.0), Order(order_id="ORD-2", value=20.0)]
total_order_value(orders)   # 30.0
total_order_value([])       # 0.0
```

## Development

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements-dev.txt

coverage run -m pytest
coverage report
coverage xml -o coverage.xml     # consumed by SonarQube
```

## Quality pipeline

`.github/workflows/build.yml` runs the test suite with coverage, then
SonarQube Cloud analysis and a blocking Quality Gate check — on every push to
`main` and on every pull request. Configuration lives in
`sonar-project.properties`; the only secret required is `SONAR_TOKEN`.

Code-review conventions for this repository are committed under `.gitar/`.

## Layout

```
orderstats/
  models.py       # Order dataclass
  stats.py        # aggregation helpers
tests/            # pytest suite
.gitar/
  review/         # custom code-review instructions
  rules/          # PR lifecycle automation rules
.github/workflows/build.yml
sonar-project.properties
docs/             # demo harness documentation (see below)
```

---

> **Note** — this repository is a demo harness for a Gitar × SonarQube
> workflow, not a production library. The scenario it stages, and the runbook
> for presenting it, are in [`docs/`](docs/). Everything above this line is an
> ordinary project README on purpose: `docs/` is the only place that describes
> the demo, so deleting that directory yields a repository with no hints in it.
