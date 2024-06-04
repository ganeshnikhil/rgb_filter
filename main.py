import numpy as np 
from PIL import Image
import argparse 
from rgb_filter.gray_scale import Grayscale 
from rgb_filter.blur  import Blur
from rgb_filter.horizontal_ref import Horizontal_ref
from rgb_filter.vertical_ref import Vertical_ref
from rgb_filter.lo_fi import Lo_fi 
from rgb_filter.amaro import Amaro
from rgb_filter.sepia import Sepia 
from rgb_filter.grain import Grain 
from rgb_filter.enhance import Enhance 
from rgb_filter.negative import Negative 
from rgb_filter.positive import Positive
from rgb_filter.up_low import Up_low 
from rgb_filter.max_up import Max_up 
from rgb_filter.min_low import Min_low
from rgb_filter.vintage import Vintage 
from rgb_filter.vignetting import Vignetting
from rgb_filter.warmth import Warmth 
from rgb_filter.faded import Faded 
def load_image(path):
   img = Image.open(path)
   return  np.array(img , np.uint8)

def save_image( filter_array , path):
   img = Image.fromarray(filter_array)
   img.save(path)
   return path 
def parse_arguments():
   """Parses command-line arguments for image processing functions.

   Returns:
         A namespace object containing parsed arguments.
   """

   parser = argparse.ArgumentParser(description="Process an image file")
   parser.add_argument("image_file", help="Path to the image file to process")
   parser.add_argument("-o", "--output", help="Optional output filename (default: image_array.jpg)")
   
   # Define mutually exclusive filter group
   #parser = parser.add_mutually_exclusive_group(required=True)
   parser.add_argument("-g", "--grayscale", action="store_true", help="Convert image to grayscale")
   parser.add_argument("-b", "--blur", type=int, nargs = '?', const = 3  , help="Apply blur filter (specify kernel size)")
   parser.add_argument("-hr", "--horizontal_ref", action="store_true", help="Apply horizontal reflection")
   parser.add_argument("-vr", "--vertical_ref", action="store_true", help="Apply vertical reflection")
   parser.add_argument("-lf", "--lofi", type=float, nargs='?' , const = (0.1 , 8), help="Apply lo-fi filter (blur radius, noise factor, color depth)")
   parser.add_argument("-a", "--amaro", action="store_true", help="Apply Amaro filter")
   parser.add_argument("-s", "--sepia", action="store_true", help="Apply sepia filter")
   parser.add_argument("-e", "--enhance", type=float, nargs = '?', const = 1.2 , help="Enhance image (warmth factor)")
   parser.add_argument("-n", "--negative", action="store_true", help="Convert image to negative")
   parser.add_argument("-p", "--positive", action="store_true", help="Convert image to positive (for use with negative filter)")
   parser.add_argument("-ul", "--up_low", action="store_true", help="Apply up-low filter")
   parser.add_argument("-mu", "--max_up", action="store_true", help="Apply max-up filter")
   parser.add_argument("-ml", "--min_low", action="store_true", help="Apply min-low filter")
   parser.add_argument("-v", "--vintage",type = float , nargs= '?' , const = (1.2 , 0.8 , 0.8 , 0.05) ,  help="Apply vintage filter")
   parser.add_argument("-vi", "--vignetting", type=float, nargs='?' , const = 0.8 , help="Apply vignetting effect (intensity)")
   parser.add_argument("-w", "--warmth", type=float, nargs = '?' , const = 1.2 , help="Increase image warmth")
   parser.add_argument("-gr", "--grain", type=float ,nargs = '?' , const = 0.05 , help="grain the image")
   parser.add_argument("-f", "--faded", type=float, nargs= '?' , const = 0.8 , help="Apply faded effect (intensity)")
   
   args = parser.parse_args()
   # Check if no filter options are provided
   if not any(vars(args).get(filter_arg) for filter_arg in ['grayscale', 'blur', 'horizontal_ref', 'vertical_ref',
                                                            'lofi', 'amaro', 'sepia', 'enhance', 'negative',
                                                            'positive', 'up_low', 'max_up', 'min_low', 'vintage',
                                                            'vignetting', 'warmth', 'grain', 'faded']):
      parser.error("At least one filter option must be provided.")
    
   return args
   



def main():
   """Processes image based on command-line arguments."""

   args = parse_arguments()
   # Load image
   try:
      image_array = load_image(args.image_file)
   except FileNotFoundError:
      return  # Exit if file not found
   
   height , width , channels = image_array.shape 

   # Apply filters sequentially
   if args.grayscale:
      image_array = Grayscale(height, width, channels, image_array)
   if args.blur:
      image_array = Blur(height, width, channels, image_array, args.blur)
   if args.horizontal_ref:
      image_array = Horizontal_ref(height, width, channels, image_array)
   if args.vertical_ref:
      image_array = Vertical_ref(height, width, channels, image_array)
   if args.lofi:
      image_array = Lo_fi(height, width, channels, image_array, *args.lofi)
   if args.amaro:
      image_array = Amaro(height, width, channels, image_array)
   if args.sepia:
      image_array = Sepia(height, width, channels, image_array)
   if args.enhance:
      image_array = Enhance(height, width, channels, image_array, args.enhance)
   if args.negative:
      image_array = Negative(height, width, channels, image_array)
   if args.positive:
      image_array = Positive(height, width, channels, image_array)
   if args.up_low:
      image_array = Up_low(height, width, channels, image_array)
   if args.max_up:
      image_array = Max_up(height, width, channels, image_array)
   if args.min_low:
      image_array = Min_low(height, width, channels, image_array)
   if args.vintage:
      image_array = Vintage(height, width, channels, image_array, *args.vintage)
   #vignetting
   if args.vignetting:
      image_array = Vignetting(height, width, channels, image_array ,args.vignetting)
   if args.warmth:
      image_array = Warmth(height, width, channels, image_array, args.warmth)
   if args.faded:
      image_array = Faded(height, width, channels, image_array, args.faded)

   if args.grain:
      image_array = Grain(height, width, channels, image_array, args.grain)

   # Save processed image
   print(args.image_file.split('/')[-1])
   save_image(image_array, args.output or f"img/{args.image_file.split('/')[-1]}")

if __name__ == "__main__":
   main()


# if __name__ == '__main__':
#    full_path = "test/new_test.jpg"
#    arr = load_image(full_path)
#    height , width , channels = arr.shape
#    filter_array = Vignetting(height , width , channels , arr)
#    #print(type(filter_array))
#    path = full_path.split('/')[-1]
#    new_path = save_image(path , filter_array)
   
   
#    full_path = "test/new_test.jpg"
#    arr = load_image(full_path)
#    height , width , channels = arr.shape
#    command = ""
#    for ins in command:
#       if ins == 'g':
#          arr = Grayscale(height , width , channels , arr)
      
#       if ins == 'b':
#          arr = Blur(height , width , channels , arr)
      
#       if ins == 'hr':
#          arr = Horizontal_ref(height , width , channels , arr)
      
#       if ins == 'vr':
#          arr = Vertical_ref(height , width , channels , arr)
      
#       if ins == 'lf':
#          arr = Lo_fi(height , width , channels , arr)
      
#       if ins == 'a':
#          arr = Amaro(height , width , channels , arr)
      
#       if ins == 's':
#          arr = Sepia(height , width , channels , arr)
      
#       if ins == 'g':
#          arr = Grain(height , width , channels , arr)
      
#       if ins == 'e':
#          arr = Enhance(height , width , channels , arr)
      
#       if ins == 'n':
#          arr = Negative(height , width , channels , arr)
      
#       if ins == 'p':
#          arr = Positive(height , width , channels , arr)
      
#       if ins == 'ul':
#          arr = Up_low(height , width , channels , arr)
      
#       if ins == 'mu':
#          arr = Max_up(height , width , channels , arr)
      
#       if ins == 'ml':
#          arr = Min_low(height , width , channels , arr)
      
#       if ins == 'v':
#          arr = Vintage(height , width , channels , arr)
      
#       if ins == 'vi':
#          arr = Vignetting(height , width , channels , arr)
      
#       if ins == 'w':
#          arr = Warmth(height , width , channels , arr)
      
#       if ins == 'f':
#          arr = Faded(height , width , channels , arr)


