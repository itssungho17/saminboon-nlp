try:
    import _jpype
except ImportError:
    pass

from konlpy.tag import Hannanum
# from gensim.models import Word2Vec

f = open('./input/파스타.txt', 'rb')
text = f.read()
text = text.decode('utf-8')
category = f.name.replace('./input/', '').replace('.txt', '')
f.close

inputList = text.split(",")
inputList.append(category)
# print(inputList)

hannanum = Hannanum()
for i in inputList:
    print(hannanum.morphs(i))

# model = Word2Vec(inputList)