from gensim.models import FastText
import time

model_file = './output/menuList.model'
model = FastText.load(model_file)

# print(len(model.wv.vocab.keys()))
# print(list(model.wv.index2word))

while (1):
    print('=========================================')
    searchText = input('검색어를 입력하세요 > ')
    start = time.time()
    mostSimilarList = model.wv.most_similar(searchText, topn=10)
    end = time.time() - start
    print('=========================================')
    print('검색어 > ', searchText)
    print('predict time:\t{0:0.5f}'.format(end))
    print('=========================================')
    count = 0
    for i in mostSimilarList:
        count += 1
        print('{0}:\t{2:0.5f}:\t{1}'.format(count, i[0], i[1]))