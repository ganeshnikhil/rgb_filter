def Vertical_ref(height , width , channels , array):
   for i in range(height):
      for j in range(width//2):
         w_j = width - j - 1
         array[i , j] , array[i , w_j] = array[i , w_j] , array[i , j]
   return array 