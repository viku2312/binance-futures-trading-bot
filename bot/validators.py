def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")