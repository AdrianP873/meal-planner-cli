"""
Command line tool to interact with the meal planner API.
Features include adding a meal, getting all meals, getting a single meal.
"""

import argparse
import requests
import json

url = "<Enter API URL here>"

parser = argparse.ArgumentParser(prog='meal planner', description="CLI tool for managing the meal planner.")

parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')
parser.add_argument('--get-meals', help='Retrieve all meals', action='store_true')
parser.add_argument('--add-meal', help='Add a meal', action='store_true')

args = parser.parse_args()

def get_meals():
    """ Sends GET request to /meal API. """
    print("Retrieving your meals...")
    print("")
    req = requests.get(url)
    response = req.json()
    print("Status code: " + str(req.status_code))
    print(json.dumps(response, indent=4, sort_keys=True))

if args.get_meals:
    get_meals()
elif args.add_meal:
    print("adding a meal...")