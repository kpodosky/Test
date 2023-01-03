n = 5 
i = 1 
prev = float ('-inf')
while i <= n :
      x = int(input())
      if x <= prev :
          print ('▼')
      elif x > prev:
            print ('▲') 
            