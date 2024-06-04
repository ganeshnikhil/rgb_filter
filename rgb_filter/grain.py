from random import random 
def Grain(height , width , channels , image , noise_factor = 0.05):
   for i in range(height):
      for j in range(width):
         noise = [int(random() * noise_factor * 255 - noise_factor * 128) for _ in range(3)]
         image[i][j] = [min(255, max(0, x + noise[i])) for i, x in enumerate(image[i][j])]
   return image 