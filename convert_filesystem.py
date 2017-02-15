# Set to path for you all_files.txt from make_darknet_list.py
image_file = open('/Users/andrewsilva/Desktop/MSCOCO/coco/all_files.txt', 'r')
# Set to path you want your new image file to be at
new_image_file = open('/Users/andrewsilva/Desktop/MSCOCO/coco/fixed_files.txt', 'w')
for line in image_file:
    # Set this to be the full path for the image (as darknet needs this)
    full_path = '/home/asilva/MSCOCO/coco/images/'+line
    new_image_file.write(full_path)
new_image_file.close()
image_file.close()