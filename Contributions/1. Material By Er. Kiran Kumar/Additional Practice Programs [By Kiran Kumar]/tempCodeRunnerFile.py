starting_range = 1
ending_range = 10 

while starting_range <= ending_range:
  fact = 1
  temp = starting_range
  
  

  while temp > 0:
    fact = fact * temp 
    temp = temp - 1
  print(fact)
  
  starting_range = starting_range + 1