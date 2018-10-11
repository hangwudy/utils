
# coding: utf-8
import re
import random

def random_list(NAME):
    x_angle = random.sample(range(0, 50), 50)
    y_angle = random.sample(range(0,360),360)
    name_list = []
    for i in x_angle:
        for j in y_angle:
            name_list.append('{}_{}_{}\n'.format(NAME, i, j))
    
    random.shuffle(name_list)


    file = open('trainval.txt', 'w')
    for _ in range(len(name_list)):
        file.write(name_list[_])
    file.close()

def get_class_name_from_filename(file_name):
  """Gets the class name from a file.

  Args:
    file_name: The file name to get the class name from.
               ie. "american_pit_bull_terrier_105.jpg"

  Returns:
    A string of the class name.
  """
  match = re.match(r'([A-Za-z_]+)(_+)([0-9]+)(_+)([0-9]+)(\.jpg)', file_name, re.I)
  print(match.groups()[0])
  print(match.groups()[2])
  print(match.groups()[4])
  return match.groups()[0]

# random_list('car_door')
get_class_name_from_filename('car_door_1_2.jpg')


def get_class_name_from_filename1(file_name):
  """Gets the class name from a file.

  Args:
    file_name: The file name to get the class name from.
               ie. "american_pit_bull_terrier_105.jpg"

  Returns:
    A string of the class name.
  """
  match = re.match(r'([A-Za-z_]+)(_+)([0-9]+)(\.jpg)', file_name, re.I)
  print(match.groups()[0])
  print(match.groups()[2])
  return match.groups()[0]

# get_class_name_from_filename1('american_pit_bull_terrier_105.jpg')