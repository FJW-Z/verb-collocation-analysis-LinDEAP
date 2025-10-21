#coding=utf-8
import nltk
from nltk import word_tokenize, pos_tag

def proposition_noun(linel, keyverb):
    # 中文注释：提取论证命题（PROPOSITION）中的名词搭配
    # English note: Extract noun collocations in PROPOSITION (argument proposition)
    try:
        vindex = linel.index(keyverb)  # 定位目标动词位置
        proplist = linel[vindex+1:-1]  # 提取动词后的命题成分
        proplist = word_tokenize(' '.join(proplist))  # 分词处理
        proplist = pos_tag(proplist)  # 词性标注
        listnoun = []
        for item in proplist:
            # 筛选名词（NN/NNS/NNP/NNPS）
            if item[1] in ['NN', 'NNS', 'NNP', 'NNPS']:
                listnoun.append(item[0])
        return listnoun
    except:
        return []

# 处理语料文件并提取搭配
with open('concordance_suggest.txt', encoding='utf-8') as f:
    listall = [line.strip() for line in f.readlines()]

with open('proposition_nouns_suggest.txt', 'w', encoding='utf-8') as f_out:
    for line in listall:
        nouns = proposition_noun(line.split(), 'suggest')
        if nouns:
            f_out.write('\n'.join(nouns) + '\n')
