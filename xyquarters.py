x=int(input())
y=int(input())
# Порядок:
# 4 | 1
# - - -
# 3 | 2
if y > 0:
    if x > 0:
        print("Первая четверть")
    else:
        print("Четвертая четверть")
else:
    if x > 0:
        print("Вторая четверть")
    else:
        print("Третья четверть")
