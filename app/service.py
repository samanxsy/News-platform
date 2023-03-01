import requests
import os
import time
import datetime

#  #  #  Required dev info
Today = datetime.datetime.now()
interests = []
available_countries = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk' 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']
newsAPI_Key = os.environ.get('newsAPI_Key')

#  #  #  Entrance
print("\nWelcome to the most time-efficient news platform!")
time.sleep(0.5)
print()


#  #  #  Getting & Checking country code
def start():
    global country_code
    global country
    country_code = False

    while not country_code:
        country = input("Enter your country code\ne.g: 'us' for united states >> ").lower()
        if country in available_countries:
            country_code = True
            os.system("clear")
        else:
            print("\nCountry not available :(\nplease check your spelling")
            time.sleep(1.5)
            os.system('clear')


start()


#  #  #  Creating the interest list
while exit != 'done':
    user_interests = input("Add only topics you're interested in >> ").lower()
    interests.append(user_interests)
    print()
    print(f"{user_interests} added to the interests!")

    time.sleep(0.8)
    os.system('clear')
    exit = input("Press [Enter] to add more topics, and [Done] to get the news. > [Enter/Done] ?").lower()
    os.system('clear')

#  #  #  API Communication
url = f"https://newsapi.org/v2/top-headlines?country={country}&category=business&apiKey={newsAPI_Key}"
data = requests.get(url)
result = data.json()

#  #  #  Getting what we need from NewsAPI
print("Searching for the news . . .")
time.sleep(1)
articles = result['articles']
os.system('clear')
print(f"Today is {Today.strftime('%Y-%m-%d %H:%M')}")
print()


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
