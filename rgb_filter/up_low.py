from random import randint
def Up_low(height , width , channel , array):
   for i in range(height):
      for j in range(width):
         R , G , B =  array[i , j]
         array[i , j] = [(255 + randint(0 , R)) %  R ,  (255 + randint(0 , G)) % G, (255 + randint(0 , B))  % B]
   return array 