import requests
import json

def isListEmpty(username: str, page: int):
    request = requests.get(f'https://api.jikan.moe/v3/user/{username}/animelist/all/{page}')

    return json.loads(request.text)


def website():
    username = "Dark_Vash"
    # username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()

def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()
def website():
    # username = "Dark_Vash"
    username = "Bk-201kun"
    page = 0
    x = []
    while True:
        __listSize = len(x)
        for y in isListEmpty(username, page + 1)['anime']:
            x.append(y)
        page += 1
        print(f"{__listSize} Anime Name Added")
        if __listSize == len(x):
            print(f"{__listSize} Done")
            break

    with open('animeList.json', 'w') as animeList:
            animeList.write(json.dumps(x, indent=3))

website()