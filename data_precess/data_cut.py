import sys
sys.path.append('../')
from Data_Transform import Data_Transform

# 读入数据
data_transform_mini = Data_Transform()
data_transform_mini.read_data(path="../data/data_train.json")

# 提取数据-案件事实fact
data_transform_mini.extract_data(name='fact')

# 分词
with open("../data/stopwords-zh.txt", "r", encoding="utf-8") as stop_f:
    stopwords_raw = stop_f.readlines()
    stopwords = list(map(lambda x: x.strip("\n"), stopwords_raw))
data_transform_mini.cut_texts(texts=data_transform_mini.extraction['fact'], stopwords=stopwords)
print(data_transform_mini.texts_cut[100])