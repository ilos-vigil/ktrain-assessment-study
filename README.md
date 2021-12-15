# Assessment Study on ktrain Library for Text Processing

This reposistory contains fraction of software for thesis/[*skripsi*](https://id.wikipedia.org/wiki/Skripsi) with title "Assessment Study on ktrain Library for Text Processing"/"Studi Pengkajian Library ktrain untuk Area Text Processing". This thesis uses ktrain version 0.25.3 to 0.26.2, but all code on this repository tested with ktrain 0.28.3. Ktrain source code is available at https://github.com/amaiya/ktrain.

## Environment

### Hardware and system environment

* GNU/Linux OS based on [Debian 11 Testing](https://wiki.debian.org/DebianTesting).
* Python 3.8.7
* 6C/12T CPU
* 16GB RAM
* GTX 1060 6GB

### Library version

* You don't need to install all library if you only want to run specific notebook.
* You'll need to install Jupyter Notebook/Lab by yourself.
* Using virtual environment (such as [`venv`](https://docs.python.org/3/library/venv.html)) is strongly recommended.

```
pip install \
ktrain==0.28.3 \
torch==1.8.1 \
tensorflow==2.7.0 \
transformers==4.10.3 \
https://github.com/amaiya/stellargraph/archive/refs/heads/no_tf_dep_082.zip \
https://github.com/amaiya/eli5/archive/refs/heads/tfkeras_0_10_1.zip \
bokeh==2.3.0 \
wikiextractor==3.0.6 \
beautifulsoup4==4.9.3 \
graphviz==0.18 \
torchviz==0.0.2
```

## Directory overview

This repository is organized into three directories: 01_feature_demonstration, 02_study_cases and 03_miscellaneous. Each directory contains README file which give more detailed information.

### 01_feature_demonstration

This directory contain few Jupyter Notebook used to demonstrate feature on ktrain. Most notebook isn't included since it's similar with tutorial/example available on ktrain repository.

### 02_study_cases

This directory contain all Jupyter Notebook and script used for 3 study cases. The goal of these study cases to evaluate ktrain performance on real-life dataset. Different library and other research are used to evaluate ktrain performance. Tasks which used for study cases are,

1. Zero Shot Classification
2. Open Domain Question Answering
3. Document Similarity

### 03_miscellaneous

This directory contain some Jupyter Notebook and script which are helpful during my thesis.
