import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

WEEKS = 4  # How many weeks ahead the forecast is


def extend_urls():  # Read the urls and extend them X weeks ahead
    file = open("DiningHallUrls.txt", "r")
    temp_url_list = file.readlines()

    url_list = []

    for weeks in range(WEEKS):
        for url in temp_url_list:
            date = (datetime.now() + timedelta(days=7 * weeks)).strftime("%Y-%m-%d")
            url_list.append(url.strip() + date)

    return url_list


def forecast(desired_food):

    food_results = []

    for url in extend_urls():
        r = requests.get(url)

        # Parsing the HTML
        soup = BeautifulSoup(r.content, 'html.parser')

        # Make a label formatted like "for MEAL at DINING_HALL on"
        title = soup.find('title')
        title_text = title.get_text(strip=True)
        meal = title_text.split()[-1:]
        place = title_text.split()[-2:-1]
        label = " for " + meal[0].lower() + " at " + place[0] + " on "

        table = soup.find_all('table', class_='carbs-table')

        for cells in table:
            date = cells.find('span', class_='carbs-table-strongtitle-date')
            if date:
                date_text = date.get_text(strip=True)

            foods = cells.find_all('td', class_='carbs-table-item')
            for food in foods:
                food_text = food.get_text(strip=True)
                if desired_food.lower() in food_text.lower():
                    print(food_text + label + date_text)

        # list_of_days = []
        # day = []
        #
        # table = soup.find_all('table', class_='carbs-table')
        #
        # for cells in table:
        #     date = cells.find('span', class_='carbs-table-strongtitle-date')
        #     if date:
        #         date_text = date.get_text(strip=True)
        #         day.append(label + date_text)
        #
        #     foods = cells.find_all('td', class_='carbs-table-item')
        #     for food in foods:
        #         food_text = food.get_text(strip=True)
        #         if food_text not in day:
        #             day.append(food_text)
        #
        #     if date:
        #         list_of_days.append(day)
        #         day = []
        #
        # for day in list_of_days:
        #     for food in day:
        #         if desired_food.lower() in food.lower():
        #             print(food + day[0])
