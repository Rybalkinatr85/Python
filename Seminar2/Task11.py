# Дано натуральное число A > 1. 
# Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

# F(n) = (Fn-1)+(Fn-2)
# F(0) = 0
# F(1) = 1
# F(2) = F1 + F0 = 1 + 0 = 1
# F(3) = F2 + F1 = 1 + 1 = 2
# F(4) = F3 + F2 = 2 + 1 = 3
# F(5) = F4 + F3 = 3 + 2 = 5
# F(6) = F5 + F4 = 5 + 3 = 8

n = int(input("Введите число Фибоначчи: "))
print((round((5*n*n+4)**0.5, 0)) == (5*n*n+4)**0.5 or (round((5*n*n-4)**0.5, 0)) == (5*n*n-4)**0.5)

y = 1
z = 2
count = 4

# while (((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)/(5**0.5) < n

while z!=n:
    temp = z
    z = z+y
    y = temp
    count+=1

print(count)