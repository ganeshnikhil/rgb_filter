from random import randint 
def Max_up(height , widht , channels , array):
   for i in range(height):
      for j in range(widht):
         R , G , B = array[i , j]
         array[i , j] = [max(R , (R + randint(0 , R))%  255) ,  max(G , (G + randint(0 , G)) % 255), max(B , (B + randint(0 , B))  % 255)]
   return array 
