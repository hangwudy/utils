import os


def loadim(image_path = 'images', ext='png', keyword='car_door'):
    image_list = []
    for filename in os.listdir(image_path):
        if filename.endswith(ext) and filename.find(keyword) != -1:
            current_path = os.path.abspath(image_path)
            image_abs_path = os.path.join(current_path,filename)
            image_list.append(image_abs_path)
    return image_list


if __name__ == '__main__':
    impath = 'images'
    IMAGE_LIST = loadim(impath)
    print(IMAGE_LIST)