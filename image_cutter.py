__author__ = 'xelmirage'
from PIL import Image
import os
import sys

def cut_for_moments(image_path_string, side_length):
    dir = os.path.dirname(image_path_string) + '/'
    box_number = 3
    thumb_length = 257
    spacing = 9
    total_thumb_length = thumb_length * box_number  + spacing * (box_number - 1)
    im = Image.open(image_path_string)
    '''
    -----
    |1|2|
    -----
    |3|4|
    -----
    or
    -------
    |1|2|3|
    -------
    |4|5|6|
    -------
    |7|8|9|
    -------
    '''
    im_length = im.size[0]
    length_ratio = float(thumb_length) / total_thumb_length
    length_plus_space_ratio = float(thumb_length + spacing) / total_thumb_length
    space_ratio = float(spacing) / total_thumb_length
    cut_length = im_length * length_ratio
    cut_length_plus_space = im_length * length_plus_space_ratio
    cut_space = im_length * space_ratio
    boxes = []
    box_1 = (0, 0, cut_length, cut_length)

    box_2 = (cut_length_plus_space, 0, im_length, cut_length)
    box_3 = (0, cut_length_plus_space, cut_length, im_length)
    box_4 = (cut_length_plus_space, cut_length_plus_space, im_length, im_length)
    for i in range(0, box_number):
        for j in range(0, box_number):
            box = (int(j * cut_length_plus_space), int(i * cut_length_plus_space),
                   int(j * cut_length_plus_space + cut_length), int(i * cut_length_plus_space + cut_length))
            region = im.crop(box)
            name = os.path.basename(image_path_string)[0:-4] + 'tile' + str(i * box_number + j)
            fullpath = dir + name + '.jpg'
            region.save(fullpath, "JPEG")


if __name__ == "__main__":
    file_path=sys.argv[1]
    type=sys.argv[2]
    cut_for_moments(file_path,2)
