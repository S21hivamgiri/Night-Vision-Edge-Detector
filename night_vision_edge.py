#For Computer Visioning
import cv2
# For Image processing
from PIL import Image

#path of input image
image_path = r'./night_image.jpeg'
#path of output image
final_image = r'./output_night_image.jpeg'
#path of optimizd output image
optimized_image = r'./optimized_night_image.jpeg'

#Output File Names
output_filename = 'output_night_image.jpeg'
optimizedname = 'optimized_night_image.jpeg'
# Show Image
image=Image.open(image_path)
image.show()
#Read Image file
img = cv2.imread(image_path)
# Read the edges and write it in the output_file
cv2.imwrite(output_filename, cv2.Canny(img,100, 100))
#Display Output Image
output=Image.open(final_image)
output.show()
# Read the edges with number of edges to 350 and write it in the output_filename
cv2.imwrite(optimizedname, cv2.Canny(img,100, 350))
#Display Optimized Image
optimized=Image.open(optimized_image)
optimized.show()