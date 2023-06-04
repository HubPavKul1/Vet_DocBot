import json
import os
import random
import time

from requests import Session
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                         " Chrome/110.0.0.0 YaBrowser/23.3.4.603 Yowser/2.5 Safari/537.36"}

base_url = "https://veterinarka.ru"
categories_url = "/vetmedicaments.html"

session = Session()


def get_html(url):
    session.get(base_url, headers=headers)
    if base_url not in url:
        url = base_url + url
    response = session.get(url, headers=headers)
    url_split = url.split("/")
    file_name = f'data\\{url_split[-2] + url_split[-1]}'
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(response.text)
    return file_name


def get_data(url):
    session.get(base_url, headers=headers)
    response = session.get(url, headers=headers)
    return response.text


# def parse_html(url):
#     file_name = get_html(url)
#     with open(file_name, encoding='utf-8') as f:
#         resp = f.read()
#         soup = BeautifulSoup(resp, "lxml")
#         sub_cat_list = soup.find_all('h2', class_="subcategory-title")
#         subcategory_dict = {}
#         for elem in sub_cat_list:
#             subcategory_name = elem.find("a").get("title")
#             subcategory_url = base_url + elem.find("a").get("href")
#             subcategory_dict[subcategory_name] = subcategory_url
#         with open("drugs_subcategories.json", "w", encoding='utf-8') as file:
#             json.dump(subcategory_dict, file, indent=4, ensure_ascii=False)


def parse_json(file_name):
    with open(file_name, encoding='utf-8') as f:
        data_dict = json.load(f)
        drugs_dict = {}
        for name, url in data_dict.items():
            file_name = get_html(url)
            with open(file_name, encoding='utf-8') as file:
                resp = file.read()
                soup = BeautifulSoup(resp, "lxml")
                drugs_list = soup.find_all('h3', class_="item-title")
                pagination = soup.find('div', class_="pagination")
                if not pagination:
                    for elem in drugs_list:
                        drug_name = elem.find("a").get("title")
                        drug_url = base_url + elem.find("a").get("href")
                        drugs_dict[drug_name] = drug_url
                else:
                    tags = pagination.find_all('a')
                    last_page_url = [base_url + tag.get('href') for tag in tags][-1]
                    last_page_num = int(last_page_url.split('.')[-2][-1])
                    url_for_parse = base_url + categories_url.split('.html')[0] + '/' + last_page_url.split('/')[
                        -2] + '/'
                    for i in range(1, last_page_num + 1):
                        file_name = get_html(url_for_parse + f'{i}.html')
                        with open(file_name, encoding='utf-8') as src_file:
                            resp = src_file.read()
                            soup = BeautifulSoup(resp, 'lxml')
                            drugs_list = soup.find_all('h3', class_="item-title")
                            for elem in drugs_list:
                                drug_name = elem.find("a").get("title")
                                drug_url = base_url + elem.find("a").get("href")
                                drugs_dict[drug_name] = drug_url
            time.sleep(random.randint(3, 5))
        with open("drugs.json", "a", encoding='utf-8') as json_file:
            json.dump(drugs_dict, json_file, indent=4, ensure_ascii=False)


# def get_drugs_from_json(file_name):
#     with open(file_name, encoding='utf-8') as f:
#         data_dict = json.load(f)
#         for name, url in data_dict.items():
#             file_name = get_html(url)
            # with open(file_name, encoding='utf-8') as file:
            #     resp = file.read()
            #     soup = BeautifulSoup(resp, "lxml")


def get_drug_property(url: str) -> dict:
    drug_prop = get_data(url)
    soup = BeautifulSoup(drug_prop, "lxml")
    drug_title = soup.find(class_="item-title").text
    drug_image_url = soup.find(class_="item-image align-left").find("img").get("src")
    drug_description_tags = soup.find(class_="element element-textarea first last")
    drug_descriptions = drug_description_tags.find_all("p")
    drug_description_list = [p.text for p in drug_descriptions if not p.text.startswith("<!--")]
    drug_description = ''
    for text in drug_description_list:
        new_text = ''
        counter = 0
        for elem in text:
            if elem.isupper() and counter < 1 and elem not in 'IVUSA':
                new_text += '\n' + elem
                counter += 1
            else:
                new_text += elem
            if elem.islower() or elem in '.,""':
                counter = 0

        drug_description += new_text
    drug_prop_dict = {
        'title': drug_title,
        'image': drug_image_url,
        'description': drug_description
    }
    return drug_prop_dict


def search_drug_by_name(drug_name: str) -> list:
    # file_name = os.path.abspath('drugs.json')
    file_name = os.path.abspath('vet_parser/drugs.json')
    with open(file_name, encoding='utf-8') as json_file:
        drugs = json.load(json_file)
        drug_url = {}
        for name, url in drugs.items():
            if drug_name.lower() in name.lower():
                drug_url[name] = url
        result = []
        if not drug_url:
            result.append('Препарат не найден')
        else:
            for name, url in drug_url.items():
                result.append(get_drug_property(url))
        return result


if __name__ == '__main__':
    parse_json('drugs_subcategories.json')
#     print(search_drug_by_name('синулокс'))
    # print(type(search_drug_by_name('gyh')))
