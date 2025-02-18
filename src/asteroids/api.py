import requests
from typing import Dict

API_URL = "https://api.nasa.gov/neo/rest/v1/feed"
API_KEY = "miyBCvaQVDIcBBZFBbH7A55y8sJ4mK3POiN3vxXr" 

def get_asteroids(date: str) -> Dict:
    """
    Get a list of asteroids that have approached Earth around a given date.

    Args:
        date (str): Date to search for asteroids (YYYY-MM-DD)

    Returns:
        dict: List of asteroids with their name, distance from Earth in km,
              diameter in meters, and date of approach.
    """
    try:
        # Make a GET request to the NASA API
        response = requests.get(API_URL, params={"start_date": date, "end_date": date, "api_key": API_KEY})
        response.raise_for_status()  # Raise an error if the request failed

        # Parse the JSON response
        data = response.json()
        asteroids = data["near_earth_objects"][date]
        result = []

        for asteroid in asteroids:
            # Extract relevant details for each asteroid
            name = asteroid["name"]
            close_approach_data = asteroid["close_approach_data"]
            if not close_approach_data:
                continue

            approach_info = close_approach_data[0]
            distance_km = float(approach_info["miss_distance"]["kilometers"])
            approach_date = approach_info["close_approach_date"]

            # Get estimate diameter
            diameter_data = asteroid["estimated_diameter"]["meters"]
            diameter_min = diameter_data["estimated_diameter_min"]
            diameter_max = diameter_data["estimated_diameter_max"]
            diameter_avg = (diameter_min + diameter_max) / 2

            
            result.append({
                "name": name,
                "distance_km": distance_km,
                "diameter_meters": diameter_avg,
                "approach_date": approach_date,
            })

        return result

    except requests.RequestException as e:
        print(f"Error fetching data from NASA API: {e}")
        return {}