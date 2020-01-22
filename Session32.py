import requests
import json
import threading

# Multi threading -> Parallel/Concurrent/Async Programming


"""
def fetchTechNews():
    print(">> Fetch Tech Crunch News:")

    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=31c21508fad64116acd229c10ac11e84"

    response = requests.get(url)
    print(response.text)

    news = json.loads(response.text)
    results = news["totalResults"]

    for i in range(0, len(news)):
        print("------------------------")
        print(news["articles"][i]["author"])
        print(news["articles"][i]["title"])
        print(news["articles"][i]["description"])
        print("------------------------")


def fetchWallStreetNews():
    print(">> Fetch Wall Street News:")

    url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=31c21508fad64116acd229c10ac11e84"

    response = requests.get(url)
    print(response.text)

    news = json.loads(response.text)
    results = news["totalResults"]

    for i in range(0, len(news)):
        print("------------------------")
        print(news["articles"][i]["author"])
        print(news["articles"][i]["title"])
        print(news["articles"][i]["description"])
        print("------------------------")

"""


class FetchTechNewsTask(threading.Thread):

    # What Thread should do, write in run function
    def run(self):
        print(">> Fetch Tech Crunch News:")

        url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=31c21508fad64116acd229c10ac11e84"

        response = requests.get(url)
        print(response.text)

        news = json.loads(response.text)
        results = news["totalResults"]

        for i in range(0, len(news)):
            print("------------------------")
            print(news["articles"][i]["author"])
            print(news["articles"][i]["title"])
            print(news["articles"][i]["description"])
            print("------------------------")


class FetchWallStreetNewsTask(threading.Thread):

    def run(self):
        print(">> Fetch Wall Street News:")

        url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=31c21508fad64116acd229c10ac11e84"

        response = requests.get(url)
        print(response.text)

        news = json.loads(response.text)
        results = news["totalResults"]

        for i in range(0, len(news)):
            print("------------------------")
            print(news["articles"][i]["author"])
            print(news["articles"][i]["title"])
            print(news["articles"][i]["description"])
            print("------------------------")


print(">> App Started")

techNewsTask = FetchTechNewsTask()
wallStreetNewsTask = FetchWallStreetNewsTask()

techNewsTask.start()
wallStreetNewsTask.start()

# fetchTechNews()

print(">>>>>>>>>>>>>>>>>>>>>>>")

# fetchWallStreetNews()

print(">> App Finished")