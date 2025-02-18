from .api import get_asteroids
import argparse
def main():
    parse = argparse.ArgumentParser(description="Get a list of asteroids that have approached Earth around a given date.")
    parse.add_argument("--date",type = str, required= True, help="Date to search for asteroids (YYYY-MM-DD)")
    args = parse.parse_args()
    date = args.date
    asteroids = get_asteroids(date)
    if not asteroids:
        print(f"No Asteroids found on {date}")
    else:
        for asteroid in asteroids:
            print(f"Name: {asteroid['name']}")
            print(f"Distance: {asteroid['distance_km']} km")
            print(f"Diameter: {asteroid['diameter_meters']} meters")
            print(f"Approach Date: {asteroid['approach_date']}\n")

