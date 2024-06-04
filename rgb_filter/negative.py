def Negative(height , width , channels , array):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i , j]
         array[i , j] = [min(R , 255 - R) , min(G , 255 - G) , min(B , 255 - B)]
   return array