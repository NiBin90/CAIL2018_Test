import json
import jieba

class Data_Transform():
    def __init__(self):
        self.data_path = None
        self.data = None
        self.texts_cut = None
        self.extraction = {}

    def read_data(self, path):
        self.data_path = path
        f = open(path, 'r', encoding='utf8')
        data_raw = f.readlines()
        data = []
        for num, data_one in enumerate(data_raw):
            try:
                data.append(json.loads(data_one))
            except Exception as e:
                print(e)
        self.data = data

    def extract_data(self, name='accusation'):
        data = self.data
        if name=='fact':
            extraction = list(map(lambda x: x['fact'], data))
        self.extraction.update({name: extraction})

    def cut_texts(self, texts=None, need_cut=True, stopwords=None, texts_cut_savepath=None):
        '''
        文本分词剔除停用词
        :param texts:文本列表
        :param need_cut:是否需要分词
        :param word_len:保留词语长度
        :param texts_cut_savepath:保存路径
        :return:
        '''
        
        if need_cut:
            print("正在分词...")            
            texts_cut = [[word for word in jieba.lcut(one_text) if word not in stopwords] for one_text in texts]           
        else:       
            texts_cut = texts

        if texts_cut_savepath is not None:
            with open(texts_cut_savepath, 'w') as f:
                json.dump(texts_cut, f)
        self.texts_cut = texts_cut
        return texts_cut
