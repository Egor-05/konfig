# Задание:

Разработать инструмент командной строки для визуализации графа
зависимостей, включая транзитивные зависимости. Сторонние средства для
получения зависимостей использовать нельзя.
Зависимости определяются по имени пакета языка Python (pip). Для
описания графа зависимостей используется представление Graphviz.
Визуализатор должен выводить результат в виде сообщения об успешном
выполнении и сохранять граф в файле формата png.
Конфигурационный файл имеет формат csv и содержит:

• Путь к программе для визуализации графов.  
• Имя анализируемого пакета.  
• Путь к файлу с изображением графа зависимостей.  
• URL-адрес репозитория.  
Все функции визуализатора зависимостей должны быть покрыты тестами.

# Запуск:

```commandline
pip install -r requirements.txt
```

Затем

```commandline
python main.py setup.csv 
```

# Запуск тестов

```commandline
 python -m coverage run -m tests
```

Затем

```commandline
python -m coverage report
```