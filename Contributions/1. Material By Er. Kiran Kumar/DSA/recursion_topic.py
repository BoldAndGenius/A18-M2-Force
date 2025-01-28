# Print N to 1 Numbers Using Recursion


N = 5 
def Print1ToN(N): 
  if N == 0:
    return None 
  print(N)
  Print1ToN(N-1)
Print1ToN(N)