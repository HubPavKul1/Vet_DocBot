from requests import Session
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36"}

base_url = "https://veterinarka.ru"

session = Session()


def get_data(url):
    session.get(url, headers=headers)
    new_url = url + "/vetmedicaments.html"
    response = session.get(new_url, headers=headers)
    #
    with open("vet_site.html", "w", encoding="utf-8") as file:
        file.write(response.text)


def get_subcategories(file_path: str):
    with open(file_path, encoding='utf-8') as f:
        resp = f.read()
        soup = BeautifulSoup(resp, "lxml")
        sub_cat_list = soup.find_all('h2', class_="subcategory-title")
        sub_cat_urls = [base_url + elem.find("a").get("href") for elem in sub_cat_list]
        return sub_cat_urls


if __name__ == "__main__":
    # get_data(base_url)
    print(get_subcategories('vet_site.html'))
