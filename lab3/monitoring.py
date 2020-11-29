import requests
import json
import logging
from requests.exceptions import HTTPError
import time

logging.basicConfig(
    # format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} : {message}',
    style='{',
    encoding='utf-8',
)
# log = logging.getLogger(__name__)


def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        logging.warning("Попередження 404. Помилка: %s", http_err)
    except Exception as error:
        logging.error("Сервер недоступний. Помилка: %s", error)
    else:
        data = json.loads(r.content)
        logging.info("Сервер доступний. Час на сервері: %s", data['date'])
        logging.info("Запитувана сторінка: : %s", data['current_page'])
        logging.info("Відповідь сервера місти наступні поля:")
        for key in data.keys():
            logging.info("Ключ: %s, Значення: %s", key, data[key])

if __name__ == '__main__':
    while True:
        main("http://127.0.0.1:8000/health")
        time.sleep(60)