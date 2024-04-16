import requests

URL = "https://opentdb.com/api.php?amount=10&type=boolean"
question_request = requests.get(url=URL)
question_data = question_request.json()["results"]