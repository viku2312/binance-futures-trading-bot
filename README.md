# Binance Futures Testnet Trading Bot

## Overview

A Python-based CLI trading bot for Binance Futures Testnet (USDT-M). The application supports placing MARKET and LIMIT orders for both BUY and SELL sides using Binance Futures Testnet APIs.

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Command-line interface using argparse
* Input validation
* Logging of requests, responses, and errors
* Exception handling for invalid input and API failures
* Environment variable support using .env

## Project Structure

trading_bot/

├── bot/

│   ├── **init**.py

│   ├── client.py

│   ├── orders.py

│   ├── validators.py

│   └── logging_config.py

├── logs/

│   └── trading.log

├── cli.py

├── requirements.txt

├── README.md

└── .env

## Installation

1. Clone the repository:

git clone <repository-url>

cd trading_bot

2. Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the root directory:

API_KEY=your_binance_testnet_api_key

API_SECRET=your_binance_testnet_api_secret

## Usage

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 150000

## Example Output

ORDER REQUEST

Symbol : BTCUSDT

Side : BUY

Type : MARKET

Quantity : 0.001

ORDER RESPONSE

Order ID : 13799779081

Status : NEW

Executed Qty : 0.0000

SUCCESS: Order request completed.

## Logging

All API requests, responses, and errors are stored in:

logs/trading.log

## Validation

* Side must be BUY or SELL
* Order type must be MARKET or LIMIT
* Price is mandatory for LIMIT orders

## Error Handling

The application handles:

* Invalid user input
* Missing API credentials
* Binance API exceptions
* Network-related issues

## Assumptions

* User has a Binance Futures Testnet account.
* Valid API credentials are configured in `.env`.
* Binance Futures Testnet is available and reachable.
