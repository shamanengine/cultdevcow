import requests
import json
import urllib.parse

url = "https://www.monster.com/jobs/search/?q=q&where=VA&stpage=1&page=10"
r1 = requests.get(url=url)
r2 = requests.get("https://www.indeed.com/jobs?q=rpa&l=Norwood%2C+MA&radius=50&sort=date")
print(r2.text)

# response_dict = json.loads(r.text)
