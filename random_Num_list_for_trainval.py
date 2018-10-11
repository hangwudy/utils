
# coding: utf-8

import random

Lt = random.sample(range(1, 201), 200)
file = open('trainval.txt', 'w')
for i in range(200):
    file.write('NAME-{}\n'.format(Lt[i]))
    print('NAME-{}'.format(Lt[i]))
file.close()
