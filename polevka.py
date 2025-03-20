from bs4 import BeautifulSoup
import requests, json


def main():

    url = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(url)

    soup = BeautifulSoup(
        response.content, "html.parser"
    )  # vytvoření proměnnou, která zbírá informace z webu v html stylu

    list = []
    suroviny = soup.find_all(class_="stuff")
    for p in suroviny:
        list.append(p.text)
    jidlo = list[0], list[1], list[2], list[3]
    with open("ingredience.json", mode="w") as soubor:
        json.dump(jidlo, soubor, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
