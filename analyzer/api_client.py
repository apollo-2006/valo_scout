import random
from typing import List, Dict


class ValorantAPI:
    def __init__(self, api_key: str = "mock_key"):
        self.api_key = api_key
        self.base_url = "https://api.henrikdev.xyz/valorant/v3"  # Popular community API

    def fetch_recent_matches(self, player_name: str, tag: str) -> List[Dict]:
        """
        Generates 20 synthetic matches in the Ascendant/Diamond range.

        This is mock data, not a live fetch. Wiring it to the real API means
        replacing the body below with:

            import requests
            response = requests.get(f"{self.base_url}/matches/na/{player_name}/{tag}",
                                    headers={"Authorization": self.api_key})
            return response.json()["data"]
        """

        matches = []
        maps = ["Ascent", "Bind", "Haven", "Split", "Lotus"]

        for i in range(20):
            kills = random.randint(10, 28)
            deaths = random.randint(9, 22)
            assists = random.randint(5, 15)
            efficiency_score = (kills + assists) / max(1, deaths) * random.uniform(0.8, 1.2)

            matches.append({
                "match_id": f"OMEN-{1000 + i}",
                "map": random.choice(maps),
                "agent": "Omen",
                "kills": kills,
                "deaths": deaths,
                "assists": assists,
                "kda_ratio": round((kills + assists) / max(1, deaths), 2),
                "efficiency_score": round(efficiency_score, 2),
                "smokes_deployed": random.randint(15, 35)
            })
        return matches