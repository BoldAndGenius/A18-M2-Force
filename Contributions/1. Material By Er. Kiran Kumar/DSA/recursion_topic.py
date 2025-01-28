# Print N to 1 Numbers Using Recursion


N = 5 
def PrintNTo1(N): 
  if N <= 0:
    return None 
  print(N)
  PrintNTo1(N-1)
PrintNTo1(N)




# Print 1 to N Numbers Using Recursion

N = 5 
def Print1ToN(N):
  if N <= 0: 
    return None 
  Print1ToN(N-1)
  print(N)
Print1ToN(N)