import requests
import os

API_KEY = os.environ.get("API_FOOTBALL_KEY")
API_BASE = "https://v3.football.api-sports.io"

def handler(request, response):
    league = request.args.get("league", "39")  # Premier League default
    season = request.args.get("season", "2025")
    url = f"{API_BASE}/standings?league={league}&season={season}"
    res = requests.get(url, headers={"x-apisports-key": API_KEY})
    response.status_code = res.status_code
    response.headers["Content-Type"] = "application/json"
    response.send(res.text)
