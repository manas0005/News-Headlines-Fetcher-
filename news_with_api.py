import requests

url = "https://newsapi.org/v2/everything"

API = "1e0bd9c19fa145f18bc27e69ec0e3d7f"

while True:
    print("\n-------News Category-------")
    print("Press 1 for Sports News")
    print("Press 2 for Science and Tech News")
    print("Press 3 for Economy Realeted News")
    print("Press 4 for Golbal Politics News")
    print("Press 5 for Education Related News")
    print("press 6 for Hollywood News")
    print("Press 7 for Bollywood News")
    print("Press 8 for Stock-Market News")


    choice = input("\nEnter Your Choice to get news (1-8): ")

    if choice == '1':
        topic = 'Sports'
    elif choice == '2':
        topic = 'Science and Technology'
    elif choice == '3':
        topic = 'Economy'
    elif choice == '4':
        topic = 'Global Politics'
    elif choice == '5':
        topic = 'Education'
    elif choice == '6':
        topic = 'Hollywood'
    elif choice == '7':
        topic = 'Bollywood'
    elif choice == '8':
            topic = 'Stock Market'

    else:
        print("Invalid Input!")

    parameter = {
        'q': topic,
        'apikey': API,
        'language': 'en',
        'pageSize':5
    }

    response = requests.get(url, params=parameter)


    if response.status_code == 200:
        data = response.json()
        articles= data['articles']

        if len(articles)==0:
            print("No News Found")
        else:
            print(f"Top {len(articles)} news about {topic}\n")

        for i, articles in enumerate(articles, 1):
            print(f"{i}. {articles['title']}\n")
            print(f"{articles['description']}\n")
            print(f"  🖋️ Author: {articles['author']}\n")
            print(f"  🌐 {articles['url']}\n\n")
    else:
        print("Falid to fetch news.. please try again later.")

    regen = input("\nDo you want to more news (Y/N): ").strip().upper()
    if regen != 'Y' :
        print("Have a nice day..")
        break


   