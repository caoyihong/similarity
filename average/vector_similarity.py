import gensim
import jieba
import logging
import numpy as np
from scipy.linalg import norm

model_file = 'D:/model/news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=True)

# 获取停用词
def get_stopwords():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)
    #加载停用词表
    stopword_set = set()
    with open("../stop_words/stopwords.txt",'r',encoding="utf-8") as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip("\n"))
    return stopword_set

def vector_similarity(s1, s2):
    def sentence_vector(s):
        words = jieba.lcut(s)
        #获取停用词表
        stopwords = get_stopwords()
        v = np.zeros(64)
        for word in words:
            if word not in stopwords:
                v += model[word]
        v /= len(words)
        return v
    
    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))
# 测试
original = '请问截至六月30日公司的股东人数是多少谢谢'
targets = [
    '请问截至六月30日公司的股东人数是多少谢谢',
    '请问截至7月十五日 公司的股东人数是多少谢谢',
    '请问8月中期股东户数谢谢',
    '4月30日股东户6442户6月15日6364户请问减少的这部分是何原因为主股份数量增加的账号是否全是机构投资者谢谢解答',
    '我喜欢吃香蕉'
]
print("原句：",original)
for target in targets:
    print(target, vector_similarity(target, original))
