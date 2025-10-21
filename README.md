# Verb Collocation Analysis for Academic Writing  
基于LinDEAP语料库的学术写作动词搭配模式分析（课程项目）


## 项目定位  
本仓库存储的是“语料库语言学”课程项目代码，核心功能是从LinDEAP学术语料库中提取、分析**论证类动词（如show、suggest、indicate）的搭配模式**，为论文《从FrameNet视角识别LinDEAP语料库中的动词搭配模式》提供技术支撑。  
代码基于NLTK工具包实现文本分词、词性标注与核心搭配成分（SUPPORT/PROPOSITION）提取，可复现论文中“论证框架（EVIDENCE Frame）下动词搭配规律”的研究过程。  

This repository stores the code for a Corpus Linguistics course project. Its core function is to extract and analyze the collocational patterns of **evidence-giving verbs (e.g., show, suggest, indicate)** from the LinDEAP academic corpus, supporting the thesis *"Identifying Verb Collocational Patterns in LinDEAP Corpus from the Perspective of FrameNet"*.  
Based on the NLTK toolkit, the code implements text tokenization, POS tagging, and extraction of core collocational elements (SUPPORT/PROPOSITION), enabling the reproduction of the research process on "verb collocation rules under the EVIDENCE Frame" in the thesis.


## 核心功能  
### 1. 论证类动词搭配提取  
- 针对LinDEAP语料库中的目标动词（show、suggest、indicate等），定位其在句中的位置；  
- 自动识别搭配的核心成分：  
  - **SUPPORT**：论证依据（如“study、data、results”等名词短语）；  
  - **PROPOSITION**：论证命题（如“that-从句、wh-从句、名词短语”等）。  

### 2. 词性标注与句法过滤  
- 使用NLTK的`pos_tag`功能标注词汇词性，精准筛选名词短语（NN/NNS/NNP/NNPS）作为核心搭配；  
- 处理语料中的长句修饰成分，避免因“动词-搭配”间隔过远导致的提取遗漏（如“The results for both participants suggest...”中的“results”）。  

### 3. 语料结果输出  
- 读取AntConc生成的语料索引文件（如`concordance_suggest.txt`），批量处理并输出动词搭配列表，为论文数据分析提供结构化数据。


## 技术栈  
- 编程语言：Python 3.8+  
- 核心库：  
  - `nltk`：文本分词、词性标注、句法分析；  
  - `re`（隐含依赖）：正则表达式处理文本格式；  
- 输入数据：LinDEAP语料库的动词索引文件（AntConc导出的TXT格式）；  
- 运行环境：Jupyter Notebook / 本地Python环境。  

| 依赖库 | 版本建议 | 功能说明 |
|--------|----------|----------|
| nltk   | 3.8.1    | 核心自然语言处理工具 |
| pandas | 1.5.3    | （可选）结构化数据存储 |


## 使用说明  
### 1. 环境准备  
1. 安装依赖库：  
   ```bash
   pip install nltk pandas
2. 下载 NLTK 词性标注模型（首次运行时执行）：
   import nltk
   nltk.download('averaged_perceptron_tagger')  # 词性标注模型
   nltk.download('punkt')  # 分词模型

### 2. 数据准备
将 AntConc 生成的目标动词索引文件（如 concordance_suggest.txt、concordance_show.txt）放入 input/ 文件夹；
确保语料文件编码为 utf-8，避免中文乱码或格式错误。

### 3. 运行步骤
1. 克隆仓库到本地：
git clone https://github.com/你的用户名/verb-collocation-analysis-LinDEAP.git
cd verb-collocation-analysis-LinDEAP
2. 运行核心脚本：
若使用 Python 脚本：执行 src/verb_collocation_extractor.py，指定目标动词和输入文件路径；
若使用 Jupyter Notebook：打开 notebooks/Verb_Collocation_Analysis.ipynb，按单元格顺序运行（含详细代码注释）。
3. 查看结果：
提取的动词搭配列表会保存至 output/ 文件夹，按 “动词 - 搭配类型” 命名（如 suggest_proposition_nouns.txt）。

## 论文关联说明
本代码直接支撑论文《从 FrameNet 视角识别 LinDEAP 语料库中的动词搭配模式》的核心研究环节：
论文 “4.2 论证依据（SUPPORT）分析”：代码提取的名词短语搭配为 “表 1 研究结果类搭配” 提供数据；
论文 “4.3 论证命题（PROPOSITION）分析”：代码统计的从句 / 名词短语分布，对应 “表 3 命题句法模式” 的量化结果；
可通过修改 keyverb 参数（如 suggest→indicate），复现论文中 5 个核心动词的搭配分析过程。

## 版本更新
2024.10：完成核心功能开发，支持 show/suggest/indicate/argue/demonstrate 5 个动词的搭配提取；
2024.09：初始版本，实现基础的名词短语筛选与语料读取功能。

## 备注
若需处理更多论证类动词，可修改代码中的 keyverb 参数（如 proposition_noun(linel, 'indicate')）；
建议结合 AntConc 的 “关键词索引” 功能使用，先通过 AntConc 筛选高频动词，再用本代码精准提取搭配成分，提升研究效率；
For academic reference, please cite the thesis: "Identifying Verb Collocational Patterns in LinDEAP Corpus from the Perspective of FrameNet" (2024).
