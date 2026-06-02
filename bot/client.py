from binance.client import Client
from dotenv import load_dotenv
import os
import logging

load_dotenv()


class BinanceClient:

    def __init__(self):

        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key:
            raise ValueError("API_KEY not found in .env")

        if not api_secret:
            raise ValueError("API_SECRET not found in .env")

        logging.info("Initializing Binance Futures Testnet Client")

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret
        )

        # Binance Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client