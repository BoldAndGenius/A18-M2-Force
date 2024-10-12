# Question - 1


n = 1000
sum = 0
for num in range(1,n):
    if num%3==0 or num%5==0:
        sum = sum + num
print(sum)
