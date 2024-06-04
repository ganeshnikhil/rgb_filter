def Positive(height , width , channel , array):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i , j]
         array[i , j] = [max(R , 255 - R ) , max(G , 255 - G ) , max(B , 2555 - B )]
   return array 