# Задание:  
Разработать инструмент командной строки для учебного конфигурационного
языка, синтаксис которого приведен далее. Этот инструмент преобразует текст из
входного формата в выходной. Синтаксические ошибки выявляются с выдачей
сообщений.  
Входной текст на языке json принимается из стандартного ввода. Выходной
текст на учебном конфигурационном языке попадает в стандартный вывод.  
Массивы:  
{ значение, значение, значение, ... }

Имена:  
[_a-zA-Z]+  
Значения:  
• Числа.  
• Массивы.  
Объявление константы на этапе трансляции:  
имя is значение;  
Вычисление константного выражения на этапе трансляции (префиксная
форма), пример:  
.[+ имя 1].  
Результатом вычисления константного выражения является значение.  
Для константных вычислений определены операции и функции:
1. Сложение.
2. Вычитание.
3. Умножение.
4. Деление.
5. sort().

Все конструкции учебного конфигурационного языка (с учетом их
возможной вложенности) должны быть покрыты тестами. Необходимо показать 2
примера описания конфигураций из разных предметных областей.

# Для запуска приложения:

```commandline
cd hw2
pip install -r requirements.txt
```

# Для запуска тестов:

```commandline
 python -m coverage run -m tests
```

Затем

```commandline
python -m coverage report
```