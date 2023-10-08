# Commerce: An eBay-like Auction Site

## Overview
**Commerce** is an e-commerce auction platform inspired by eBay. This web application offers the following features:

- **Post Auction Listings:** Users can easily list items they wish to auction.
- **Place Bids:** Engage in competitive bidding for items of interest.
- **Comment on Listings:** Engage in discussions or ask questions related to the auction item.
- **Add to Watchlist:** Track items of interest by adding them to your watchlist.

This project is an assignment from [Harvard's CS50 Web Programming with Python and JavaScript course](https://cs50.harvard.edu/web/2020/projects/2/).

## Setup
1. **Clone this repository**

    ```bash
    git clone https://github.com/qildeli/commerce.git
    ```

2. **Navigate into the repository's directory**

    ```bash
    cd commerce
    ```

3. **Create a virtual environment** (optional)

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the application**

    ```bash
    python manage.py runserver
    ```
Open your web browser and navigate to http://127.0.0.1:8000/ to dive into Commerce.
