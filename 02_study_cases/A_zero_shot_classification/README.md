# Zero Shot Classification

## Dataset

Dataset used on this study case is [Indonesian-Twitter-Emotion-Dataset](https://github.com/meisaputri21/Indonesian-Twitter-Emotion-Dataset). This dataset is part of paper [Emotion Classification on Indonesian Twitter Dataset](https://www.researchgate.net/publication/330674171_Emotion_Classification_on_Indonesian_Twitter_Dataset) by Mei Silviana Saputri, Rahmad Mahendra dan Mirna Adriani. This dataset use license [CC BY-NC-SA 4.0](https://github.com/meisaputri21/Indonesian-Twitter-Emotion-Dataset), so it can be used for this study case.

| Label       | Tweet count |
| ----------- | ----------- |
| Anger       | 1101        |
| Fear        | 649         |
| Happy       | 1017        |
| Love        | 637         |
| Sadness     | 997         |
| Total tweet | 4403        |

To add more performance evaluation types, this dataset optionally went through preprocessing. There are 5 different preprocessing, where 4 of them is performed with RegEx. Below table show all preprocesing with an example for each preprocessing.

| #   | Description                                                                       | Before preprocessing                                                | After preprocessing                                       |
| --- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------- |
| 1   | Tag removal                                                                       | Senang..... sekali kalau TIDAK wajib praktek [USERNAME]!!! #bahagia | Senang..... sekali kalau TIDAK wajib praktek !!! #bahagia |
| 2   | Remove number sign character (`#`) which followed by non-whitespace character     | Senang..... sekali kalau TIDAK wajib praktek !!! #bahagia           | Senang..... sekali kalau TIDAK wajib praktek !!! bahagia  |
| 3   | Remove period (`.`) character which occured 2 or times                            | Senang..... sekali kalau TIDAK wajib praktek !!! bahagia            | Senang sekali kalau TIDAK wajib praktek !!! bahagia       |
| 4   | Reduce continous occurance non-word character which appear 2 or more times. occur | Senang sekali kalau TIDAK wajib praktek !!! bahagia                 | Senang sekali kalau TIDAK wajib praktek ! bahagia         |
| 5   | Lowercase                                                                         | Senang sekali kalau TIDAK wajib praktek ! bahagia                   | senang sekali kalau tidak wajib praktek ! bahagia         |

## Performance evaluation

In this performance evaluation, metric F1 Score is used. Library HuggingFace Transformers and result from reference publication are used as comparison. Both ktrain and HuggingFace Transformers use model [joeddav/xlm-roberta-large-xnli](https://huggingface.co/joeddav/xlm-roberta-large-xnli), while best result from reference publication use Linear Regression with different preprocessing.

Based on below table, it's shown that ktrain and HuggingFace Transformers have identical performance with negligable difference. Preprocessing the dataset only improve the performance less than 0.5%. However treating the dataset as multi-label task improve the performance close to 5%. Model joeddav/xlm-roberta-large-xnli have lower performance than Linear Regression, but it's not surprising due to multiple factors. Model joeddav/xlm-roberta-large-xnli is trained on more than 100 language and only fine tuned on 15 language **excluding Indonesian Language**. Additionally this model isn't explicitly trained to classify emotion type of Indonesian tweet.

| #   | Library                  | Preprocessing | Multi-label | Anger    | Fear     | Happy    | Love     | Sadness  | Micro F1 Score |
| --- | ------------------------ | ------------- | ----------- | -------- | -------- | -------- | -------- | -------- | -------------- |
| 1   | Ktrain                   |               |             | 0.44     | 0.53     | 0.70     | **0.71** | 0.47     | 0.5690         |
| 2   | Huggingface Transformers |               |             | 0.44     | 0.53     | 0.70     | **0.71** | 0.47     | 0.5690         |
| 3   | Ktrain                   | V             |             | 0.44     | 0.54     | 0.70     | **0.71** | 0.48     | *0.5735*       |
| 4   | Huggingface Transformers | V             |             | 0.44     | 0.54     | 0.70     | 0.70     | 0.48     | 0.5726         |
| 5   | Ktrain                   |               | V           | 0.58     | **0.63** | 0.68     | 0.69     | 0.52     | 0.6171         |
| 6   | Huggingface Transformers |               | V           | 0.58     | **0.63** | 0.68     | 0.69     | 0.52     | *0.6174*       |
| 7   | Ktrain                   | V             | V           | 0.58     | **0.63** | 0.68     | 0.70     | 0.53     | *0.6205*       |
| 8   | Huggingface Transformers | V             | V           | 0.58     | **0.63** | 0.68     | 0.70     | 0.53     | 0.6203         |
| 9   | Reference publication    | V             |             | **0.70** | 0.59     | **0.69** | 0.69     | **0.80** | **0.6973**     |

### The importance of hyphotesis template

On Zero Shot Classification which utilize Natural Language Inference (NLI), it's common practice to use hyphotesis template. This study case also shows the importance of hyphotesis template, where experiment #7 is used as reference. Below table shows without hyphotesis template, performance of the model is decreased by 7% which is lowest among all experiment.

| Template       | "Kalimat ini mengekspresikan {}." | "{}."  |
| -------------- | --------------------------------- | ------ |
| Anger          | **0.58**                          | 0.52   |
| Fear           | **0.63**                          | 0.58   |
| Happy          | **0.68**                          | 0.58   |
| Love           | **0.70**                          | 0.63   |
| Sadness        | **0.53**                          | 0.46   |
| Micro F1 Score | **0.6205**                        | 0.5506 |
