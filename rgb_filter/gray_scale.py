
def Grayscale(height , width , channels , array):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i][j]
         avg = 0.299 * R + 0.587 * G + 0.114 * B
         array[i , j] = round(avg)
   return array