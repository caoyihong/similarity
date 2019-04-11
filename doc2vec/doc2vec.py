# -*- coding: utf-8 -*-
import sys
import logging
import os
import gensim
# 引入doc2vec
from gensim.models import Doc2Vec
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from utilties import ko_title2words

# 引入日志配置
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 加载数据
documents = []
# 使用count当做每个句子的“标签”，标签和每个句子是一一对应的
count = 0
with open('../data/titles/ko.video.corpus','r') as f:
    for line in f:
        title = unicode(line, 'utf-8')
        # 切词，返回的结果是列表类型
        words = ko_title2words(title)
        # 这里documents里的每个元素是二元组，具体可以查看函数文档
        documents.append(gensim.models.doc2vec.TaggedDocument(words, [str(count)]))
        count += 1
        if count % 10000 == 0:
            logging.info('{} has loaded...'.format(count))

# 模型训练
model = Doc2Vec(documents, dm=1, size=100, window=8, min_count=5, workers=4)
# 保存模型
model.save('models/ko_d2v.model')