"""Domain objects for the order-statistics helpers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    """A single customer order.

    Attributes:
        order_id: Unique identifier of the order.
        value: Gross value of the order, in the account currency.
    """

    order_id: str
    value: float
