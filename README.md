# nlp-ner
中文自然语言处理，命名实体识别ner，CRF算法，准确率95%-99%

## 环境  
python3  
## 文件  
**data目录**  
存放 人民日报1998年1月已标注数据集，  
    2014年人民日报标注预料集，链接: https://pan.baidu.com/s/1avSF6YCctNFQK-6IHoVAxQ 提取码: p5st 。  
**model目录**    
此目录存放已经训练好的模型，可以直接使用。    
模型文件下载链接:https://pan.baidu.com/s/1t8dHEIsWmfUGQO6xbadhIA  密码:hln7   
template_XX_XX,CRF++特征提取模版，template_{标识方式名称}_{特征数}
exec_XX_XX.sh,CRF++训练，测试，验证结果正确率执行脚本。
analyze_result_XX_XX_XX.txt,CRF++验证结果。

**corpus.py**  
处理数据集，标注格式，生成可供CRF++训练和测试的数据集。  
**nerpredit.py**  
用训练好的模形预测NER内容。此文件只在python3环境下测试通过。  
**conlleval.py**  
分析crf用训练好的模形预测NER内容。  
## 工具
CRF++,安装，使用说明请自行百度，下载 https://taku910.github.io/crfpp/#download  
使用的CRF++版本是0.59

## 测试结果
1.只用使用单一标注方式
BIO,BMEWO，这两种标注方式，特征数量，10或者15，数据相差正负0.5左右， 
accuracy:  98-99; precision:  94-96%; recall:  91-92%; FB1:  92-93  
2.词性+标注
词性标计+BIO,BMEWO，特征数量，10或者15，数据相差正负0.3左右，
accuracy:  99+%; precision:  98+%; recall:  98+%; FB1:  98+   
## 总结  
词性标注+序列标注，正确率优于单一序列标注算法，整体正确率在99%以上，在某些细分领域达到100%。在非专业领域内，本模型已经可以在生产环境上线。  
本项目训练数据采用人民日报1998年1月标注数据，如果加上人民日报2014年标注数据，效果应该会更好，但我没有测试过，结果如何，未知。