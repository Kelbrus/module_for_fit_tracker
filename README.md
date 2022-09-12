#### The 2nd project of my studying Python Dev+ at YP

# Module for fitness-tracker

### Описание
###### RU
- Данные приходят в виде списка кортежей с микроконтроллера фитнес трекера. 

- Задача скрипта - обрабатывать входные данные и отображать  информацию о типе тренировки, количество потраченных килокалорий, среднюю скорость и пройденную дистанцию пользователю в user friendly формате. 

- Особенности кода:  использованы аннотации типов, конструктор классов реализован через декоратор @dataclass

*Код выполнен в соответствии с PEP8 и Docstring Convention*
###### EN
- The data comes in the form of a list of tuples from the fitness tracker microcontroller.

- The task of the script is to process input data and display information about the type of workout, the number of calories spent, average speed and distance traveled to the user in a user friendly format.

- Code features: type hints are used, the class constructor is implemented through the @dataclass decorator

*The code is executed in accordance with PEP8 and Docstring Convention*

### Стэк технологий
- Python v.3.7

### Запуск проекта в dev-режиме
- **Установите виртуальное окружение:**
- - _для WIndows_
```
$ python -m venv venv
```
- - _для Unix_
```
$ python3 -m venv venv
```
- **Активируйте виртуальное окружение:**
- - _для WIndows_
```
$ source venv/Scripts/activate
```
- - _для Unix_
```
$ source venv/bin/activate
```
- **Установите зависимости из файла requirements.txt:**
```
$ pip install -r requirements.txt
``` 