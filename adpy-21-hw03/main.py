import requests
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'python'}
BASEURL = 'https://habr.com/ru/all/'


# Ваш код
def get_url_text(url):
    response = requests.get(url)
    if response.ok:
        return response.text
    else:
        return False


def main(url=BASEURL, advaced_task=False):
    text = get_url_text(url)
    article_list = []
    if text:
        soup = bs(text, features="html.parser")
        articles = soup.find_all('article', class_='post_preview')
        for article in tqdm(articles):
            article_time = article.find('span', class_='post__time').text
            article_title = article.find('a', class_='post__title_link')
            article_title_text = article_title.text
            article_title_link = article_title['href']
            if advaced_task:
                # Далее код от дополнительного задания
                # отсюда
                article_text_full = get_url_text(article_title_link)
                article_words = {}
                if article_text_full:
                    article_post = bs(article_text_full, features="html.parser")
                    article_fulltext = article_post.find('div', class_='post__body_full').text
                    article_words = {word for word in article_fulltext.split(' ')}
                # досюда
            else:
                article_text = article.find('div', class_='post__text').text
                article_words = {word for word in article_text.split(' ')}
            if KEYWORDS & article_words:
                article_list.append(f'{article_time} - {article_title_text} - {article_title_link}')
        return article_list


if __name__ == '__main__':
    output_list = []
    pages = int(input('Введите количество страниц: '))
    for page in range(pages):
        print(f'Обрабатываем страницу {page + 1} из {pages}')
        if page == 0:
            output_list += main(advaced_task=True)
        else:
            output_list += main(url=f'{BASEURL}page{page+1}/', advaced_task=True)
    print(*output_list, sep='\n')
