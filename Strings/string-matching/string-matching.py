def solve():
  
  def zarray(string):
    z=[]
    for i in range(len(string)):
      if i == 0:
          z.append(0)
          continue
      
      rightString = string[i:]
      coincidences = 0
      for k in range(len(rightString)):
        if rightString[k] != string[k]:
          break
        else: coincidences += 1
        
      z.append(coincidences)
        