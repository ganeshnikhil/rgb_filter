def Vignetting(height , width , channels , image , vignette_intensity = 0.8):
   vignette_factors = [[1 - abs(x - width // 2) / (width // 2) * vignette_intensity for x in range(width)] for i in range(height)]
   for i in range(height):
      for j in range(width):
         factor = vignette_factors[i][j]
         image[i , j] = [round(x * factor) for x in image[i][j]]
   return image