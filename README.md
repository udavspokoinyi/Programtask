# Task-on-topic-No.-10-PyCharm

____

## Сравнение времени выполнения

Время выполнения filter.py:

![filter](./filter.png "filter.png")

Время выполнения old_filter.py:

![old_filter](./old_filter.png "old_filter.png")

Разница в общем (total) времени выполнения обусловлена использованием оптимизированных встроенных методов для работы с
матрицами в NumPy, например, average(). Также разница обусловлена использованием срезов вместо циклов. А разница в
собственном (own) времени выполнения обусловлена тем, что ресурсоёмкие задачи в filter.py выделены в отдельные функции.

Время выполнения filter_with_filename.py:

![filter_with_filename](./filter_with_filename.png "filter_with_filename.png")

Разница между временем выполнения filter.py и filter_with_filename.py обусловлена отсутствием необходимости ввода
запрашиваемых параметров.

## Изображение до преобразования и после

Исходное изображение:

![test img](./img.jpg "img.jpg")

Результат работы filter.py и filter_with_filename.py:

![filter res img](./res_img.jpg "res_img.jpg")

Результат работы old_filter.py:

![old_filter res img](./old_filter_res.jpg "old_filter_res.jpg")

## Docstring

![doctests res](./doctests_res.png "doctests_res.png")

Функция работает исправно.

## Debugger

![debugger1](./debugger.png "debugger.png")

![debugger2](./debugger2.png "debugger2.png")

Значения:
+ ширина изображения: 1538;
+ высота изображения: 1378;
+ тип изображения: JPEG;
+ ширины блока: 10;
+ количество градаций серого: 6.