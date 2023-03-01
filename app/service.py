import requests
import os
import time
import datetime

Today = datetime.datetime.now()
available_countries = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk' 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']
newsAPI_KEY = os.environ.get('newsAPI_KEY')


#  #  #  Creating the interest list
def news(user_interests, country):
    """This will add the user's interests to the interests list"""
    interests = [user_interests.lower()]

#  #  #  API Communication
    url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_KEY}"
    data = requests.get(url)
    result = data.json()

#  #  #  Getting what we need from NewsAPI

    print("Searching for the news . . .")
    time.sleep(1)
    articles = result['articles']

    #  #  #  Printing the interesting headlines, if there is any
    contains = False
    for news in articles:
        words = news['title'].split()

        for word in words:
            if word.lower() in interests:
                contains = True
                print(news['title'])
                print(news['url'])
                print()
                break

            else:
                continue

    if not contains:
        print("No interesting news for you Today!")
