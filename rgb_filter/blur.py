def Blur(height , width , channels , array , blur_square = 3):
   offset_x , offset_y = - blur_square // 2  , blur_square // 2 + 1
   
   for i in range(height):
      for j in range(width):
         R , G , B = 0 , 0 , 0
         neighbour_count = 0 
         for x in range(offset_x , offset_y):
            for y in range(offset_x , offset_y):
               fit_x = i + x 
               fit_y = j + y 
               if 0 <= fit_x < height and 0 <= fit_y < width:
                  r , g , b = array[fit_x , fit_y]
                  R += r 
                  G += g 
                  B += b 
                  neighbour_count += 1
         
         counter = max(1 , neighbour_count)
         array[i , j] = [round(R/counter) , round(G/counter), round(B/counter)]
   return array 