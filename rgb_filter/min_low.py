from random import randint 
def Min_low(height , width , channels , array):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i , j]
         array[i , j] = [min(R , (R + randint(0 , R)) %  255) ,  min(G , (G + randint(0 , G)) % 255), min(B , (B + randint(0 , B))  % 255)]
   return array 