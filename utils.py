# coding: utf-8
# author: Hang Wu
import re
import random
import os


def random_list(name_string):
    x_angle = random.sample(range(0, 50), 50)
    y_angle = random.sample(range(0, 360), 360)
    name_list = []
    for i in x_angle:
        for j in y_angle:
            name_list.append('{}_{}_{}\n'.format(name_string, i, j))

    random.shuffle(name_list)


# output a txt file
def random_list_file_export(out_list):
    file = open('trainval.txt', 'w')
    for row in range(len(out_list)):
        file.write(out_list[row] + '\n')
    file.close()


def get_class_name_from_filename(file_name):
    """Gets the class name from a file.

    Args:
      file_name: The file name to get the class name from.
                ie. "american_pit_bull_terrier_20_105.jpg"

    Returns:
      A string of the class name.
    """
    match = re.match(r'([A-Za-z_]+)(_+)([0-9]+)(_+)([0-9]+)(\.jpg)', file_name, re.I)
    print(match.groups()[0])
    print(match.groups()[2])
    print(match.groups()[4])
    return match.groups()[0]


# get image absolut path
def loadim(image_path='images', ext='png', key_word='car_door'):
    image_list = []
    for filename in os.listdir(image_path):
        if filename.endswith(ext) and filename.find(key_word) != -1:
            current_path = os.path.abspath(image_path)
            image_abs_path = os.path.join(current_path, filename)
            image_list.append(image_abs_path)
    return image_list


# Wrong !!!
def list_shuffle(list_to_shuffle):
    # Wrong !!!! 
    print(random.shuffle(list_to_shuffle))
    return random.shuffle(list_to_shuffle)


# from absolut path to file name
def file_name_from_path(file_list):
    file_name_list = []
    for f_path in file_list:
        fname = f_path.split(os.path.sep)[-1]
        fname = fname.split('.')[-2]
        file_name_list.append(fname)

    return file_name_list


if __name__ == '__main__':
    # random_list('car_door')
    # get_class_name_from_filename('car_door_1_2.jpg')
    raw_list = loadim('/home/hangwu/CyMePro/data/images', 'jpg', 'car_door')
    # print(raw_list)
    # shuffle_list = list_shuffle(raw_list)
    name_list = file_name_from_path(raw_list)
    print(name_list)
    random.shuffle(name_list)
    print(name_list)
    random_list_file_export(name_list)
