from app import app

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


@app.route('/')
def index():
    source = requests.get(
        'https://mwarszczynski.github.io/Weekly-WebDev-Challenge//weekly-webdev-2/').text

    soup = BeautifulSoup(source, 'lxml')

    print(soup)

    return soup


# print(soup)
