# -*- coding: utf-8 -*-
from district.central_street.house1.room1 import folks as folks_central_street_room1
from district.central_street.house1.room2 import folks as folks_central_street_room2
from district.central_street.house2.room1 import folks as folks_central_street_room1_house2
from district.central_street.house2.room2 import folks as folks_central_street_room2_house2
from district.soviet_street.house1.room1 import folks as folks_soviet_street_house1_room1
from district.soviet_street.house1.room2 import folks as folks_soviet_street_house1_room2
from district.soviet_street.house2.room1 import folks as folks_soviet_street_house2_room1
from district.soviet_street.house2.room2 import folks as folks_soviet_street_house2_room2
# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
print('На районе живут:', ','.join((','.join(folks_central_street_room1),
                                    ','.join(folks_central_street_room2),
                                    ','.join(folks_central_street_room1_house2),
                                    ','.join(folks_central_street_room2_house2),
                                    ','.join(folks_soviet_street_house1_room1),
                                    ','.join(folks_soviet_street_house1_room2),
                                    ','.join(folks_soviet_street_house2_room1),
                                    ','.join(folks_soviet_street_house2_room2))))
