import requests
from bs4 import BeautifulSoup
from langchain.agents import tool
import json
import streamlit as st


def search_questions(query, count=5):
    """Searches Stack Overflow for questions related to the query."""
    url = "https://api.stackexchange.com/2.3/search"
    params = {
        "order": "desc",
        "sort": "activity",
        "intitle": query,     # search by text in question title
        "site": "stackoverflow",
        "pagesize": count
    }
    res = requests.get(url, params=params)
    return res.json()   # return full JSON response


def parse_response(items):
    """Extracts links from Stack Overflow question items."""
    links = []
    for item in items:
        if "link" in item:
            links.append(item["link"])
    return links


@tool
def fetch_data_from_stackoverflow(query: str, count: int = 5):
    """Fetches links to Stack Overflow questions based on the query."""
    response = search_questions(query, count)
    if "items" in response:
        links = parse_response(response["items"])
        return json.dumps(links, indent=2)  # ✅ return string
    else:
        return "[]"

@tool
def get_data_from_stackoverflow(links: list[str]):
    """Fetches data from Stack Overflow posts."""
    data = []
    for link in links:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")
        post_bodies = soup.find_all("div", class_="s-prose js-post-body")
        for body in post_bodies:
            data.append(body.get_text(strip=True))
    return json.dumps(data, indent=2)  # ✅ return string

