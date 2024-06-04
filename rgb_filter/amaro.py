def Amaro(height , width , channesl , array , warmth_factor=1.2, saturation_factor=0.8):
   for i in range(height):
      for j in range(width):
         R , G , B = array[i , j]
         adjusted_red = min(255, int(R * warmth_factor))
         adjusted_green = min(255, int(G * (warmth_factor - 0.2)))  # Reduce green slightly
         adjusted_blue = min(255, int(B * (warmth_factor - 0.4)))  # Reduce blue more

         # Reduce saturation (average for all channels)
         average = (adjusted_red + adjusted_green + adjusted_blue) / 3
         array[i , j] = [int(channel * saturation_factor + average * (1 - saturation_factor)) for channel in [adjusted_red, adjusted_green, adjusted_blue]]
   return array
