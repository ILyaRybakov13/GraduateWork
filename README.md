# QAP 161 diplom
Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии»
Тестирование страницы https://b2c.passport.rt.ru сайта "Ростелеком"


Ссылка на описание тестов
https://docs.google.com/spreadsheets/d/1ARlu5AP4wXvRdesBJhxkLAlqks3JUXr3KgA6EN5qTKs/edit?usp=sharing

Чек-лист, тест-кейсы и баг- репорты:
автоматизированные тесты.

В процессе проверки функциональности веб-сайта использовались следующие методики для разработки тестов:

    Оценка граничных значений: Мы анализировали и тестировали значения, находящиеся на грани различных 
    диапазонов, чтобы     убедиться, что система     корректно обрабатывает крайние ситуации.

    Группировка на классы эквивалентности: Мы разделяли входные данные на группы схожих значений, 
    чтобы тестировать их     представителей вместо каждого     отдельного значения. Это позволяло 
    снизить количество тестов, при этом сохраняя полное покрытие.

    Проверка состояний и переходов: Мы проводили тестирование, уделяя внимание 
    состояниям системы и переходам между ними. 
    Это позволяло убедиться,     что сайт правильно реагирует на различные действия 
    пользователей и переходы между страницами или функциями работают корректно.

Эти методики помогли нам разработать тесты, которые обеспечивают обширное покрытие 
функциональности сайта и помогают выявить потенциальные проблемы.

Библиотеки, которые применяются во время тестирования в среде PyCharm, включают:


    requests
    python-dotenv
    pytest
    selenium
    faker
    

Настройки автотестов выполнены так, чтобы их можно было запускать непосредственно через опцию "Run".


Для тестирования страниц восстановления пароля, как в позитивных, так и в негативных сценариях, требуется ручной ввод символов с изображения "капчи" в соответствующее поле, при этом задержка для ввода организована автоматически. Также, для проверки авторизации по адресу электронной почты и паролю, 
потребуется ручной ввод "капчи".

Для создания временного адреса электронной почты использовался веб-сайт www.1secmail.com.

В проекте также имеется папка с названием "PRG," в которой находятся Python-скрипты.

В данной папке содержатся следующие файлы и их функциональное назначение:

    registration_email.py - этот файл содержит GET-запросы, которые позволяют получить действительный 
                            адрес электронной почты и код     для регистрации на сайте, а также для восстановления пароля.

    config.py - здесь находится основной URL тестируемого веб-сайта.

    auth.py - в этом файле содержатся функции-обертки для локаторов, которые 
                организованы по классам в соответствии с темой проводимых тестов.

    base.py - этот файл включает функции для применения явных ожиданий к локаторам, 
                получения главной страницы сайта и определения текущего пути страницы.

    locators.py - здесь находятся XPath- и CSS-локаторы веб-элементов на сайте, 
                которые используются в тестах.

    settings.py - данный файл содержит информацию, которая используется во время проведения тестов.

    tests_neg.py - в этом файле размещены негативные тесты.

    tests_pos.py - здесь находятся позитивные тесты.

      

    
