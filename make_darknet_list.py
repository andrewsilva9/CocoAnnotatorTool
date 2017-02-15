import os
from pycocotools.coco import COCO
from pycocotools import mask
import numpy as np
import skimage.io as io
import pylab
import cv2

text_out = open('/Users/andrewsilva/Desktop/MSCOCO/coco/all_files.txt', 'w')
dataDir='..'
dataType='train2014'
annFile='%s/annotations/instances_%s.json'%(dataDir,dataType)
coco=COCO(annFile)
# cats = coco.loadCats(coco.getCatIds())
#
# nms=[cat['name'] for cat in cats]
# for index, name in enumerate(nms):
#     print index, ':', name
#
# print 'COCO categories: \n\n', ' '.join(nms)

# Keep a list of images so far so that we don't add anything twice
imgs_so_far = []
# List of all categories I want
categories=['person', 'bottle', 'cup', 'bowl', 'tv', 'laptop', 'cell phone', 'book']
# IDs for the categories above
category_ids = [0, 39, 41, 45, 62, 63, 67, 73]
# categories = ['laptop']
# For each category, get images that fit for that
for cat in categories:
    catIds = coco.getCatIds(catNms=cat)
    imgIds = coco.getImgIds(catIds=catIds)
    for number in imgIds:
            img = coco.loadImgs(number)[0]
            if img['file_name'] in imgs_so_far:
                continue
            arr = cv2.imread('/Users/andrewsilva/Desktop/MSCOCO/coco/images/' + img['file_name'])
            # cv2.imshow('win', arr)
            # cv2.waitKey(0)
            text_file_path = '/Users/andrewsilva/Desktop/MSCOCO/coco/labels/' + img['file_name'].split('.')[0] + '.txt'
            outfile = open(text_file_path, 'w')
            annIds = coco.getAnnIds(imgIds=img['id'], catIds=category_ids, iscrowd=None)
            anns = coco.loadAnns(annIds)
            for ann in anns:
                cat_id = ann['category_id']
                if cat_id in category_ids:
                    bbox = ann['bbox']
                    # Left edge of bounding box, normalized by image width
                    left = bbox[0] / len(arr[0])
                    # Top edge of bounding box, normalized by image height
                    top = bbox[1] / len(arr)
                    width = bbox[2] / len(arr[0])
                    height = bbox[3] / len(arr)
                    # Should the category id that I add be true, or a new one because I'm reducing the number of categories?
                    outfile.write('{:d} {:f} {:f} {:f} {:f} \n'.format(cat_id, left, top, width, height))
            outfile.close()
            text_out.write(img['file_name'] + '\n')
            imgs_so_far.append(img['file_name'])
