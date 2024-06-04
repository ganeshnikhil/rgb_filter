from random import random 
from rgb_filter.blur import Blur 


def Lo_fi(height , width , channels , array ,  noise_factor=0.1, color_depth=8):
   # Apply blur (replace with your preferred blurring function)
   # ... (blurring logic)
   blur_array = Blur(height , width , channels , array , blur_square= 3)
   for i in range(height):
      for j in range(width):
         R , G , B = blur_array[i , j]
         # Reduce color depth (assuming conversion to grayscale for simplicity)
         gray = round((float(R) + float(G)  + float(B)) / 3)
         quantized_gray = round(gray * (2**color_depth - 1) / 255) * (255 / (2**color_depth - 1))

         # Add noise
         noise = int(random() * noise_factor * 255)
         adjusted_gray = min(255, max(0, quantized_gray + noise))
         blur_array[i , j] = adjusted_gray 
   return blur_array