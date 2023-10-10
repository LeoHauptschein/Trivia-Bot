import requests

url = 'https://opentdb.com/api.php?amount=10'
params = {}

def pull_questions(count, category, difficulty) -> list:
    params['amount'] = count
    if category:
        params['category'] = category
    if difficulty != 'any':
        params['difficulty'] = difficulty

    questions = requests.get(url, params)
    return questions.json()['results']
