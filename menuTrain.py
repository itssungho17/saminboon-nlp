try:
    import _jpype
except ImportError:
    pass

from konlpy.tag import Hannanum
from gensim.models import FastText
import time

f = open('./input/menuList.txt', 'r', encoding='utf-8')
lines = f.readlines()

menuList = []
for line in lines:
    count = 0
    category = ''
    foodList = []

    singleFoodList = line.strip().split(',')
    for food in singleFoodList:
        if (food.isspace() == False and food != ''):
            if (category != ''):
                foodList.append('{0} {1}'.format(category, food.strip()))
            else:
                foodList.append(food.strip())

            if (count == 0):
                category = food.strip()

            count += 1
    menuList.append(foodList)
f.close

# print(menuList)

sentences = []
hannanum = Hannanum()
for menu in menuList:
    for m in menu:
        # print(hannanum.morphs(m))
        sentences.append(hannanum.morphs(m))

# print(sentences)

start = time.time()

model_file = './output/menuList.model'
model = FastText(sentences=sentences, size=15, window=1, min_count=1, iter=100, workers=4, sg=1)
model.save(model_file)

print('train time:\t{0:0.5f}'.format(time.time() - start))