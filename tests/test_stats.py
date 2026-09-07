"""Tests for :mod:`orderstats.stats`."""

from orderstats.models import Order
from orderstats.stats import average_order_value, total_order_value


def _orders(*values: float) -> list[Order]:
    """Build a list of orders with the given values and generated ids."""
    return [
        Order(order_id=f"ORD-{index}", value=value)
        for index, value in enumerate(values, start=1)
    ]


def test_total_order_value_sums_every_order() -> None:
    assert total_order_value(_orders(10.0, 20.0, 5.5)) == 35.5


def test_total_order_value_is_zero_without_orders() -> None:
    assert total_order_value([]) == 0.0


def test_average_order_value_returns_the_mean() -> None:
    assert average_order_value(_orders(10.0, 20.0, 30.0)) == 20.0
