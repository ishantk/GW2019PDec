import requests
import json

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey="
# print(url)

response = requests.get(url)
# print(response.text)

# Covert JSON Data into Python Dictionary
news = json.loads(response.text)
# print(news)
# print(type(news))

# print(news["status"])

print(news["totalResults"])
results = news["totalResults"]
for i in range(0, results):
    print("------------------------")
    print(news["articles"][i]["author"])
    print(news["articles"][i]["title"])
    print(news["articles"][i]["description"])
    print("------------------------")

# PS: Parse JSON Data from web service:  https://openweathermap.org/
#     Parse JSON Data from Uber Developer:  https://developer.uber.com/