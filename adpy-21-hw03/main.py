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


def main(advaced_task=False):
    text = get_url_text(BASEURL)
    article_list = []
    if text:
        soup = bs(text, features="html.parser")
        articles = soup.find_all('article', class_='post_preview')
        for article in tqdm(articles):
            post_time = article.find('span', class_='post__time').text
            post_title = article.find('a', class_='post__title_link')
            post_title_text = post_title.text
            post_title_link = post_title['href']
            if advaced_task:
                # Далее код от дополнительного задания
                # отсюда
                post_text_full = get_url_text(post_title_link)
                post_words = {}
                if post_text_full:
                    soup_post = bs(post_text_full, features="html.parser")
                    post_fulltext = soup_post.find('div', class_='post__body_full').text
                    post_words = {word for word in post_fulltext.split(' ')}
                # досюда
            else:
                post_text = article.find('div', class_='post__text').text
                post_words = {word for word in post_text.split(' ')}
            if KEYWORDS & post_words:
                article_list.append(f'{post_time} - {post_title_text} - {post_title_link}')
        print(*article_list, sep='\n')


if __name__ == '__main__':
    main(True)
