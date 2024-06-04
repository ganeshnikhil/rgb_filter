def Warmth(height , width , channels , image , warmth_factor = 1.2):
   for i in range(height):
      for j in range(width):
         r, g, b = image[i][j]
         image[i][j] = [
            min(255, int(r * warmth_factor)),
            max(0, int(g * (warmth_factor - 0.2))),
            max(0, int(b * (warmth_factor - 0.4)))
         ]
   return image 
