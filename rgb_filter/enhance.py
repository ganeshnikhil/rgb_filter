def Enhance(height , width , channels , array , factor = 1.2 ):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i , j]
         array[i , j] = [min(255 , int(R * factor)) , min(255 , int(G * factor)) , min(255 , int(B * factor))]
   return array 