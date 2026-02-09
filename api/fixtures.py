import requests
import os

API_KEY = os.environ.get("API_FOOTBALL_KEY")
API_BASE = "https://v3.football.api-sports.io"

def handler(request, response):
    url = f"{API_BASE}/fixtures?live=all"
    res = requests.get(url, headers={"x-apisports-key": API_KEY})
    response.status_code = res.status_code
    response.headers["Content-Type"] = "application/json"
    response.send(res.text)
