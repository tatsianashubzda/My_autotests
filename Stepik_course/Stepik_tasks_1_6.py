# # Задание 1
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#------------------------------------------------------------------------
#
# Задание 2
# На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:
#
#     Добавьте в самый верх своего кода import math
#     Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
#     Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
#
#     str(math.ceil(math.pow(math.pi, math.e)*10000))
#
#     (можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде)
#
#     Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации
#
#     Заполните скриптом форму так же как вы делали в предыдущем шаге урока
#     После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание
#
# Важно! Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов.
# Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса,
# ваши тесты будут проходить только с определенным языком интерфейса.
# Применяйте этот метод с осторожностью и помните про возможные ограничения.



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
#
#     link = browser.find_element(By.LINK_TEXT, link_text)
#     link.click()
#
#
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

#------------------------------------------------------------------------

#
# Задание 3: использование метода find_elements
#
# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
# В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали,
# добавив в форму 100 обязательных полей и ограничив время на ее заполнение.
# Теперь эта задача под силу только роботам
#
# Используйте WebDriver, метод find_elements, нужные локатор и его значение.
# Введите полученный код в качестве ответа к этой задаче.
#
# Используйте приведенный ниже шаблон: в цикле for мы можем последовательно взять каждый элемент из найденного списка
# текстовых полей и отправить произвольный текст в каждое поле.
# Если скрипт не успевает заполнить форму, выберите текст покороче.


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# не забываем оставить пустую строку в конце файла  21.242834517558933


#------------------------------------------------------------------------


# Задание 4: поиск элемента по XPath
#
# На этот раз воспользуемся возможностью искать элементы по XPath.
#
# На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3, при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit", и наша задача нажать в коде именно на неё.
#
# Ваши шаги:
#
#     В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
#     Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
#     Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
#     Запустите ваш код.
#
# Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно отправить в качестве ответа на это задание.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form")
#     input1 = browser.find_element(By.NAME, "first_name")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#
#     button = browser.find_element(By.XPATH, "//button[text()='Submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
#     #25.285888245983035

#------------------------------------------------------------------------


# Задание 5 Уникальность селекторов
#
# Попробуем реализовать один из автотестов из предыдущего шага. Вам дана страница с формой регистрации.
# Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля,
# отмеченные символом *: First name, last name, email.
# Текст для полей может быть любым. У
# спешность регистрации проверяется сравнением ожидаемого текста
# "Congratulations! You have successfully registered!" с текстом на странице,
# которая открывается после регистрации. Для сравнения воспользуемся стандартной конструкцией assert из языка Python.
#
# Ниже дан шаблон кода, который вам нужно использовать для своего теста.
# Не забывайте, что селекторы должны быть уникальными.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, 'input:required')
    for element in elements:
        element.send_keys("Мой ответ")


    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
