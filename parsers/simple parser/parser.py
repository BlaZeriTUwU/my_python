import requests
import csv
from bs4 import BeautifulSoup

def parser():
    t = response.text
    soup = BeautifulSoup(t, 'html.parser')
    posts = soup.find('div', id='mw-content-text')

    if not posts:
        return []

    new_list = []
    lili = posts.find_all('li')

    for post in lili:
        title_tag = post.find_all('a')
        for t_t in title_tag:

            if not t_t.text.strip() or not t_t.has_attr('href'):
                continue

            title_text = t_t.text.strip()
            name_1 = t_t['href']

            if not name_1.startswith('/wiki/') or ':' in name_1:
                continue

            name_2 = URL_easy + name_1
            dead = {
                'text': title_text,
                'link': name_2
            }
            new_list.append(dead)
    return new_list

def csv_file(new_items, path):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['text', 'link'])
        writer.writeheader()
        writer.writerows(new_items)

URL = 'https://ru.wikipedia.org/wiki/Википедия:Избранные_статьи'
URL_easy = 'https://ru.wikipedia.org'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

path = "wiki_all_featured_articles.csv"

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    new_items = parser()
    csv_file(new_items, path)
else:
    print(f"Ошибка: {response}")
