import argparse
from pprint import pprint

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type
)
from bot.logging_config import setup_logger


def main():

    setup_logger()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_side(args.side)
        validate_order_type(args.type)

        if args.type.upper() == "LIMIT" and args.price is None:
            raise ValueError(
                "Price is required for LIMIT orders"
            )

        client = BinanceClient().get_client()
        manager = OrderManager(client)

        print("\nORDER REQUEST")
        print("-" * 40)
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")

        if args.price:
            print(f"Price    : {args.price}")

        response = manager.place_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )


        if isinstance(response, dict):

            print("\nORDER RESPONSE")
            print("-" * 40)
            print(f"Order ID     : {response.get('orderId', 'N/A')}")
            print(f"Status       : {response.get('status', 'N/A')}")
            print(f"Executed Qty : {response.get('executedQty', 'N/A')}")

            if "avgPrice" in response:
                print(f"Avg Price    : {response.get('avgPrice')}")

        print("\nSUCCESS: Order request completed.")

    except Exception as e:
        print(f"\nERROR: {type(e).__name__}")
        print(e)


if __name__ == "__main__":
    main()