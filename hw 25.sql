"""Владимир, добрый день. Писал запросы без верхнего регистра. Надеюсь это не ошибка, в следующий раз буду следить."""
"""Не уверен насчет 18 задания, не совсем его понял."""

"Лысые злодеи 90х годов"

Select name, APPEARANCES, FIRST_APPEARANCE
from MarvelCharacters
Where hair == 'Bald' and align == 'Bad Characters' and Year Between 1990 and 1999

"Герои с тайной идентичностью и необычными глазами"

Select name, Eye, FIRST_APPEARANCE
from MarvelCharacters
Where identify = 'Secret Identity' and Eye not in ('Blue Eyes', 'Brown Eyes', 'Green Eyes')

"Персонажи с изменяющимся цветом волос"

Select name, hair
from MarvelCharacters
Where hair = 'Variable Hair'

"Женские персонажи с редким цветом глаз"

Select name, eye
from MarvelCharacters
Where sex = 'Female Characters' and eye in ('Gold Eyes', 'Amber Eyes')

"Персонажи без двойной идентичности, сортированные по году появления"

Select name, FIRST_APPEARANCE
from MarvelCharacters
Where identify = 'No Dual Identity'
Order by year Desc

"Герои и злодеи с необычными прическами"

Select name, align, hair
from MarvelCharacters
Where hair not in ('Brown Hair', 'Red Hair', 'Blond Hair', 'Black Hair')

"Персонажи, появившиеся в определённое десятилетие"

Select name, FIRST_APPEARANCE
from MarvelCharacters
Where Year Between 1960 and 1969

"Персонажи с уникальным сочетанием цвета глаз и волос"

Select name, eye, hair
from MarvelCharacters
Where hair = 'Red Hair' and eye = 'Yellow Eyes'

"Персонажи с ограниченным количеством появлений"

Select name, APPEARANCES
from MarvelCharacters
Where APPEARANCES < 10

"Персонажи с наибольшим количеством появлений"

Select name, APPEARANCES
from MarvelCharacters
Order by APPEARANCES Desc
LIMIT 5

"Персонажи, появившиеся только в одном десятилетии"

Select name, FIRST_APPEARANCE
from MarvelCharacters
Where Year Between 2000 and 2009

"Персонажи с самыми редкими цветами глаз"

Select name, eye
from MarvelCharacters
Where eye in ('Magenta Eyes', 'Pink Eyes', 'Violet Eyes')

"Герои с публичной идентичностью, сортированные по году"

Select name, identify, FIRST_APPEARANCE
from MarvelCharacters
Where identify = 'Public Identity'
Order by year

"Персонажи с конкретным цветом волос и глаз, упорядоченные по имени"

Select name, eye, hair
from MarvelCharacters
Where hair = 'Black Hair' and eye = 'Green Eyes'
Order by name

"Злодеи с нестандартными физическими характеристиками"

Select name, sex
from MarvelCharacters
Where align = 'Bad Characters' and sex not in ('Male Characters', 'Female Characters')

"Персонажи с наибольшим числом появлений по полу"

Select name, sex, max(APPEARANCES)
from MarvelCharacters
Where sex in ('Male Characters', 'Female Characters')
Group by sex

"Сравнение популярности персонажей по цвету волос и глаз"

Select eye, hair, sum(APPEARANCES)
from MarvelCharacters
Group by hair, eye

'Персонажи с максимальным количеством появлений в десятилетие'

Select name, APPEARANCES, year
from MarvelCharacters
Where year like '%0'
Group by year

'Герои и злодеи 80-х'

Select align, count(*) total
from MarvelCharacters
Where year Between 1980 and 1989 and align in ('Bad Characters', 'Good Characters')
Group by align

'Самые популярные прически супергероев'

Select hair, sum(APPEARANCES)
from MarvelCharacters
Group by hair
Order by sum(APPEARANCES) desc
Limit 3
