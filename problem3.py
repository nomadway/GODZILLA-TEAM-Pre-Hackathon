# Задание №3:
# Если взять строку - "237" и сложить все её числа то получится 2+3+7 = 12.
# Возьмите строку "4729461084" и сложите все её числа.
# Результат выведите на экран.



num = 4729461084
sum = 0
while num>0:
    num1 = num%10
    sum = sum+num1
    num = int(num/10)
print(sum)

