# Домашняя работа №1. Задание №14

## Условие:

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
tar. Эмулятор должен работать в режиме CLI.

Ключами командной строки задаются:

• Имя пользователя для показа в приглашении к вводу.

• Путь к архиву виртуальной файловой системы.

• Путь к стартовому скрипту.

Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:

1. clear.

2. echo.

Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 3 теста.

# Для запуска программы необходимо использовать следующую команду

```
py konfig_hw.py --user=user --path=path --script=script
```

Где user - имя пользователя, path - путь до каталога, script - путь до скрипта

# Команды

`cd` - переход в указанный файл

`clear` - очистка терминала

`exit` - окончание программы

`echo` - вывод в терминал заданной строки

`ls` - вывести список файлов в директории

В команде можно `ls` использовать следующие опции

&nbsp;&nbsp;&nbsp;&nbsp;`-s` - сортировка

&nbsp;&nbsp;&nbsp;&nbsp;`-r` - сортировка в обратном порядке

&nbsp;&nbsp;&nbsp;&nbsp;`-1` - вывод файлов в столбик



