# Задача решена для частного случая n*m = 3*2. Как сделать общее решение - пока не придумала.

import random
n = 3
m = 2
k = random.randint(1, (n*m - 1))
if k % 2 == 0:
    print(f"От шоколадки {n}*{m} можно отломить {k} долек за один разлом.")
else:
    print(f"От шоколадки {n}*{m} нельзя отломить {k} долек за один разлом.")
