# EIRB'IA Tal
## Github repo for DataChallenge 2022

Subject : https://live.iapau.fr/docs/sujetsdc/apiconseil.pdf

## To make it work :

We have alreday created two models that you can download here :
https://we.tl/t-k2JRJx3AzH
One is for french and one for english.

You can also create yours but data preprocessing and formatting may not work properly.

First you need data in format to make it readable by fastText : \
``__label__class1 [__label__class2 ...] Text data``

Script *csv_to_fasttext* can help you generate it.
(The script has trouble running on all plateforms(maybe because of ram concerns), that's why we have sent you a subset of the data already formated.
(We also have the entirety of the data formated that way in final/data/ dir)

Then you can divide your data in 2 sets for training and testing.
Script *slice_data* does it for you and randomizes data. \
Usage : ``./slice_data.sh data_file %train %test`` \
where %train and %test are numbers between 0 and 100 defining how many data lines will be used.
Two files will be generated : ``train_set`` and ``test_set`` in ``classifier`` directory.

To create the model, use fasttext : 
https://fasttext.cc/docs/en/supervised-tutorial.html

Here is an example via CLI for conveniance of hyperparametre testing: 
  ```bash
    fasttext supervised -input train_set -out model_name [-epoch number] [-lr learning_rate]
  ```
  This will generate two files : ``model.bin`` and ``model.vec``. To test your model, you can do :
  ```bash
    fasttext test model.bin test_set
  ```
 
The interface has been done with QT in Python.
