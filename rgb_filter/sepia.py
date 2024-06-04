def Sepia(height , width , channels , array):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i , j]
         sp_R = .393 * R + .769 * G + .189 * B 
         sp_G = .349 * R + .686 * G + .168 * B 
         sp_B = .272 * R + .534 * G + .131 * B
         array[i , j] = [min(sp_R , 255), min(sp_G , 255) , min(sp_B , 255)]
   return array 