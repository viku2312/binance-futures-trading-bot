import logging

class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            logging.info(
                f"Order Request: symbol={symbol}, side={side}, "
                f"type={order_type}, qty={quantity}, price={price}"
            )

            if order_type.upper() == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol.upper(),
                    side=side.upper(),
                    type="MARKET",
                    quantity=quantity
                )

            else:

                response = self.client.futures_create_order(
                    symbol=symbol.upper(),
                    side=side.upper(),
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logging.info(f"Order Response: {response}")

            return response

        except Exception as e:

            logging.exception("Order placement failed")
            raise