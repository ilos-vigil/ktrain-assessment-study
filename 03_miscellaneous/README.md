# Miscellaneous

## 1. Visualize ktrain modules

This script contain script to visualize ktrain modules along with it's dependency. This visualization is based on ktrain 0.21.3 (which is outdated by now). Most visualiation use engine "dot" which indicated by `engines[1]`. Output file (Graphviz file and visualization image) is included in this repository.

```py
>>> from graphviz import ENGINES
>>> engines = list(ENGINES)
>>> engines.sort()
>>> engines
['circo', 'dot', 'fdp', 'neato', 'osage', 'patchwork', 'sfdp', 'twopi']
```

## 2. Non-negative matrix factorization (NMF)

This notebook demonstrate Non-negative matrix factorization (NMF) as Topic model. Algorithm used for demonstration is theorem 1 of Lee and Seung's "multiplicative update rule" from paper [Algorithms for Non-Negative Matrix Factorization](https://proceedings.neurips.cc/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf).

## 3. Local Outlier Factor (LOF) 

This notebook demonstrate Local Outlier Factor (LOF) for similarity detection. The input is weight of each topic, while the output represent score of document similarity.

## 4. Layer Normalization (LN)

This notebook demonstraste how to calculate Layer Normalization manually. Torch library is used to verify the calculation process is correct.

## 5. Gaussian Error Linear Units (GELU)

This notebook demonstraste Gaussian Error Linear Units (GELU). GELU formula used is first GELU approximation which defined on paper [Gaussian Error Linear Units (GELUs)](https://arxiv.org/abs/1606.08415) which usually used on Machine Learning library. Torch library is used to verify the calculation process is correct.

## 6. Visualize HuggingFace Transformers model

This notebook demonstrate how to visualize HuggingFace Transformers model. Library [torchviz](https://github.com/szagoruyko/pytorchviz/) is used to visualize the model which also show backward process. In this notebook, BERT model with smaller size and fewer encoder layer is used as example.
