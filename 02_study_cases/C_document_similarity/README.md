# Document similarity

## Instruction

1. Download Indonesian stopwords from https://github.com/masdevid/ID-Stopwords
2. Download "Indonesian Food Recipes" dataset from https://www.kaggle.com/canggih/indonesian-food-recipes
3. Move those files to directory `dataset`

```
├── C_document_similarity
│   ├── dataset
│   │   ├── criminality_news.json
│   │   ├── id.stopwords.02.01.2016.txt
│   │   └── recipe
│   │        ├── dataset-ayam.csv
│   │        ├── dataset-telur.csv
│   │        └── ...
│   ├── 01_ktrain.ipynb
│   └── ...
```

4. Install these library

```
pip install pyod==0.9.5 gensim==4.1.2 python-Levenshtein==0.12.2
```

## Dataset

There are 2 datasets used in this study case. First dataset is "Indonesian Food Recipes". Second dataset is criminality news from media news detik.com. Below table show statistic and distribution of the datasets.


| Dataset                           | Train | Test  |
| --------------------------------- | ----- | ----- |
| Indonesian Food Recipes - Ayam    | 1916  |       |
| Indonesian Food Recipes - Ikan    | 1932  |       |
| Indonesian Food Recipes - Kambing | 1896  |       |
| Indonesian Food Recipes - Sapi    | 1958  |       |
| Indonesian Food Recipes - Udang   | 1994  |       |
| Indonesian Food Recipes - Tahu    |       | 1985  |
| Indonesian Food Recipes - Telur   |       | 1974  |
| Indonesian Food Recipes - Tempe   |       | 1986  |
| Criminality News                  |       | 10751 |
| **Total**                         | 9696  | 16696 |

First dataset is dataset about Indonesian food recipes. This dataset is categorized based on it's primary ingredients. Those recipes was taken from Cookpad at 23 February 2021 by Canggih P Wibowo. This dataset uses license CC0: Public Domain, so it can be used freely.

Second dataset is news with tag/topic criminality from news media detik.com. Date range of the news publication is 7 August 2015 to 16 March 2020, while scrapping process elapsed from 19 March 2020 to 20 March 2020. This dataset is created by lungavile, where i was given permission to use this dataset freely. This dataset is included in this repository under filename `criminality_news.json`.

## Performance evaluation

In this performance evaluation, metric accuracy is used. Document about food recipes is treated as similar document, while document about criminality news is treated as not similar. Both ktrain and Gensim/PyOD use same parameter whenever possible. Below table shows ktrain have better performance, while NMF is more suitable for this study case.

| Library     | Model | n_neighbor | Accuracy |
| ----------- | ----- | ---------- | -------- |
| Ktrain      | LDA   | 20         | 0.36     |
| Ktrain      | LDA   | 50         | 0.36     |
| Ktrain      | NMF   | 20         | 0.74     |
| Ktrain      | NMF   | 50         | **0.75** |
| Gensim/PyOD | LDA   | 20         | 0.26     |
| Gensim/PyOD | LDA   | 50         | 0.54     |
| Gensim/PyOD | NMF   | 20         | 0.62     |
| Gensim/PyOD | NMF   | 50         | 0.58     |

