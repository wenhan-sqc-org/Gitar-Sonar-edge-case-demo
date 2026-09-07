"""Aggregation helpers over collections of :class:`orderstats.models.Order`.

House rule for this module: every helper accepts an empty sequence of orders
and returns the neutral value for its aggregation rather than raising. The
``Returns:`` clause of each docstring is the contract callers rely on.
"""

from collections.abc import Sequence

from orderstats.models import Order


def total_order_value(orders: Sequence[Order]) -> float:
    """Return the combined value of every supplied order.

    Args:
        orders: The orders to total. May be empty.

    Returns:
        The sum of every order value, or ``0.0`` when ``orders`` is empty.
    """
    return float(sum(order.value for order in orders))
