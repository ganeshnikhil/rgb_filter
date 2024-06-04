import numpy as np 
def Vintage(height , width , channels , image_array, warmth_factor=1.2, saturation_factor=0.8, vignette_factor=0.8, noise_factor=0.05):
   """Applies a basic vintage filter to an image using NumPy arrays.

   Args:
      image_array: A NumPy array representing the image data (RGB channels).
      warmth_factor (optional): Factor to increase warmth (default 1.2).
      saturation_factor (optional): Factor to reduce saturation (default 0.8).
      vignette_factor (optional): Factor for darkening corners (default 0.8).
      noise_factor (optional): Factor for adding noise (default 0.05).

   Returns:
      A NumPy array with the vintage filter applied.
   """

   # Warmth adjustment
   adjusted_red = np.clip(image_array[..., 0] * warmth_factor, 0, 255)
   adjusted_green = np.clip(image_array[..., 1] * (warmth_factor - 0.2), 0, 255)  # Reduce green slightly
   adjusted_blue = np.clip(image_array[..., 2] * (warmth_factor - 0.4), 0, 255)  # Reduce blue more

   # Reduce saturation
   grayscale = np.mean(image_array, axis=2, keepdims=True)
   adjusted_image = image_array * saturation_factor + grayscale * (1 - saturation_factor)

   # Vignetting ( darken corners )
   y, x = np.ogrid[:height, :width]
   mask = (1 - vignette_factor * (np.maximum(x / (width - 1), y / (height - 1))))[:, :, None]
   adjusted_image = adjusted_image * mask

   # Add noise (subtle)
   noise = np.random.rand(height, width, channels) * noise_factor * 255
   adjusted_image = np.clip(adjusted_image + noise, 0, 255).astype(np.uint8)

   return adjusted_image
