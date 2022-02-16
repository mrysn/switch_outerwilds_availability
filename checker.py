#!/usr/bin/env python3
import requests, argparse
from bs4 import BeautifulSoup

def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    args = parser.parse_args()
    return parser, args

def perform_scrape():
    parser, args = handle_args()
    gamename_arg = args.name.lower().replace(' ','-')
    base_url = "https://www.nintendo.com/games/detail/"
    scrape_url = base_url + gamename_arg +"-switch/"
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
    page = requests.get(scrape_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product = soup.find('h1', class_="h2 game-title").get_text()
    availability = soup.find('div', class_="availability").get_text()
    status = "TBD"
    return product, availability, status, scrape_url

def outputs():
    product, availability, status, scrape_url = perform_scrape()
    if availability != None and status in availability:
        print("••",product.strip(),"•• TBD 🛑 URL:", scrape_url)
    else:
        print("••",product.strip(),"•• AVAILABLE ✅ URL:", scrape_url)

def main():
    handle_args()
    outputs()

if __name__ == '__main__':
    main()

# checker.py -n Hades
# checker.py -n "outEr wILds"
