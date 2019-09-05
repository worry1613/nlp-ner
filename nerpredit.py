# -*- coding: utf-8 -*-
# @创建时间 : 15/3/2019 
# @作者    : worry1613(549145583@qq.com)
# GitHub  : https://github.com/worry1613
# @CSDN   : http://blog.csdn.net/worryabout/

from optparse import OptionParser
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def load_model(path):
    import os, CRFPP
    # -v 3: access deep information like alpha,beta,prob
    # -nN: enable nbest output. N should be >= 2
    if os.path.exists(path):
        return CRFPP.Tagger('-m {0} -v 3 -n2'.format(path))
    raise RuntimeError('模形文件 %s 不存在！'% (path,))

def NER_bmewo(tagger,text):

    for c in text:
        if c :
            tagger.add(c)

    result = []

    # parse and change internal stated as 'parsed'
    tagger.parse()
    word = ''
    for i in range(0, tagger.size()):
        for j in range(0, tagger.xsize()):
            ch = tagger.x(i, j)
            tag = tagger.y2(i)
            if tag[0] == 'B':
                word = ch
            elif tag[0] == 'M':
                word += ch
            elif tag[0] == 'E':
                word += ch
                result.append(word)
                word = ''
            elif tag[0] == 'O':
                # word = ch
                # result.append(word)
                pass
    tagger.clear()
    return result

def NER_bio(tagger,text):

    for c in text:
        if c :
            tagger.add(c)

    result = []

    # parse and change internal stated as 'parsed'
    tagger.parse()
    word = ''
    for i in range(0, tagger.size()):
        for j in range(0, tagger.xsize()):
            ch = tagger.x(i, j)
            tag = tagger.y2(i)
            if tag[0] == 'B':
                if not word:
                    word = ch
                else:
                    result.append(word)
            elif tag[0] == 'I':
                word += ch
            elif tag[0] == 'O':
                if word:
                    result.append(word)
                    word = ''
    return result


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-i', '--input', type=str, help='model文件', dest='input')
    parser.add_option('-t', '--txt', type=str, help='需要用ner分析的单行文本，与-f互斥，优先级高', dest='txt')
    parser.add_option('-f', '--file', help='需要用ner分析的文本文件，一行或多行', dest='file')
    parser.add_option('-d', '--dataformat', type=str, default='bio', help='标注格式, bio,bmewo,默认bio',
                      dest='dataformat')
    usage = """  
            nerpredit.py -i model文件 -t 预测文本内容 -f 预测文件

            nerpredit.py  -i model/model_bio_pos -t  5月09日消息快评深度报告权威内参来自“证券通”今日热点：证券通认为，由于市场预期美联储将在今年6月暂停升息，导致了国际市场上美元走势疲软，从而推高了人民币汇率。
            nerpredit.py  -i model/model_bio_pos -f  data/nerpredit.txt  
            """
    parser.set_usage(usage)
    options, args = parser.parse_args()
    if not (options.input or (options.file or options.txt)):
        parser.print_help()
        exit()

    fmodel = options.input
    fptxt = options.txt
    fpfile = options.file
    dmap = {'bio':NER_bio,'bmewo':NER_bmewo}
    df = options.dataformat

    tagger = load_model(fmodel)
    if fptxt:
        print(dmap.get(df)(tagger, fptxt))
    else:
        f = open(fpfile)
        lines = f.readlines()
        f.close()
        for text in lines:
            print(dmap.get(df)(tagger, text.strip()))