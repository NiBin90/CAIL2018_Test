import sys
sys.path.append('../')
from Data_Transform import Data_Transform
import pickle

# 读入数据
data_transform_mini = Data_Transform()
data_transform_mini.read_data(path="../data/data_train.json")

# 提取数据-案件事实fact
data_transform_mini.extract_data(name='fact')

# 分词
with open("../data/stopwords-zh.txt", "r", encoding="utf-8", buffering=1) as stop_f:
    stopwords_raw = stop_f.readlines()
    stopwords = list(map(lambda x: x.strip("\n"), stopwords_raw))
# data_transform_mini.cut_texts(texts=data_transform_mini.extraction['fact'], stopwords=stopwords)
# print(len(data_transform_mini.texts_cut))

# 分词并保存原始分词结果，词语长度后期可以再改
for i in range(3):
    texts=data_transform_mini.extraction['fact'][i*1000:(i*1000 + 1000)]
    mini_fact_cut = data_transform_mini.cut_texts(texts=texts, stopwords=stopwords, need_cut=True)
    with open('mini_fact_cut_%d_%d.pkl' % (i*1000, i*1000 + 1000), 'wb') as f:
        pickle.dump(mini_fact_cut, f)
    print('finish mini_fact_cut_%d_%d' % (i*1000, i*1000 + 1000))
