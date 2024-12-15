start = 1
end = 100 
count = 0
for num in range(start, end+1):
  # print(num)  # 2 
  if num > 1: 
    prime = True 
    for fact in range(2,num):
      if num % fact == 0:
        prime = False
    if prime == True:
      count = count + 1
      print(num)
    
print(f"Total {count} number of Prime Numbers in between {start} and {end}")