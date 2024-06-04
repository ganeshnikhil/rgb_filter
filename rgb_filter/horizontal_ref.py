def Horizontal_ref(height , width , channels , array):
   for i in range(height//2):
      for j in range(width):
         h_i = height - i - 1
         array[i , j] , array[h_i , j] = array[h_i , j] , array[i , j]
   return array 