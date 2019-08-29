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
**corpus.py**  
处理数据集，标注格式，生成可供CRF++训练和测试的数据集。  
**nerpredit.py**  
用训练好的模形预测NER内容。此文件只在python3环境下测试通过。  
**conlleval.py**  
分析crf用训练好的模形预测NER内容。此文件只在python3环境下测试通过。  
## 工具
CRF++,安装，使用说明请自行百度，下载 https://taku910.github.io/crfpp/#download  
使用的CRF++版本是0.59
  

