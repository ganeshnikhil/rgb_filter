def Faded(height , width , channels , image , saturation_factor = 0.8):
   for i in range(height):
      for j in range(width):
         r, g, b = image[i][j]
         gray = round((float(r) + float(g) + float(b)) / 3)
         image[i][j] = [
            min(255, int(r * saturation_factor + gray * (1 - saturation_factor))),
            min(255, int(g * saturation_factor + gray * (1 - saturation_factor))),
            min(255, int(b * saturation_factor + gray * (1 - saturation_factor)))
         ]
   return image 