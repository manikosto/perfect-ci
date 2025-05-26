import os

import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Запускает браузер в режиме без графического интерфейса (удобно для серверов)
    options.add_argument("--no-sandbox")  # Отключает режим песочницы для предотвращения проблем с правами доступа
    options.add_argument(
        "--disable-dev-shm-usage")  # Отключает использование общей памяти /dev/shm (для Docker и серверных сред)
    options.add_argument("--disable-gpu")  # Отключает GPU, необходимое для headless-режима на некоторых системах
    options.add_argument("--window-size=1920,1080")  # Устанавливает фиксированный размер окна браузера

    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield
    driver.quit()