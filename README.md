# EIRB'IA Tal
## Github repo for DataChallenge 2022

Subject : https://live.iapau.fr/docs/sujetsdc/apiconseil.pdf

Doc about XAI : https://arxiv.org/pdf/2111.14260.pdf

## To make it work :

First you need data in format : \
``__label__class1 [__label__class2 ...] Text data``

Script *csv_to_fasttext* can help you generate it.

Then you can divide your data in 2 sets for training and testing.
Script *slice_data* does it for you and randomizes data. \
Usage : ``./slice_data.sh data_file %train %test`` \
where %train and %test are numbers between 0 and 100 defining how many data lines will be used.
Two files will be generated : ``train_set`` and ``test_set`` in ``classifier`` directory.

To create the model, use fasttext : 
https://fasttext.cc/docs/en/supervised-tutorial.html

Here is an example : 
  ```bash
    fasttext supervised -input train_set -out model_name [-epoch number] [-lr learning_rate]
  ```
  This will generate two files : ``model.bin`` and ``model.vec``. To test your model, you can do :
  ```bash
    fasttext test model.bin test_set
  ```
