# Note: to use flair library you need to have a version of python < 3.10
from flair.data import Corpus
from flair.models import SequenceTagger
from flair.datasets import ColumnCorpus
from flair.embeddings import WordEmbeddings, StackedEmbeddings, TokenEmbeddings
from flair.trainers import ModelTrainer
from typing import List
from matplotlib import pyplot as plt
import pandas as pd


class Ner:
    def train(persent_of_dataset_to_train = 1):
        tag_type = 'ner'
        columns = {0: 'text', 1: 'ner'}
        data_folder = './datasets/'
        corpus: Corpus = ColumnCorpus(data_folder, columns, train_file='nerTrain.txt',test_file='nerTest.txt', dev_file='nerDev.txt')
        corpus.downsample(persent_of_dataset_to_train)
        tag_dictionary = corpus.make_label_dictionary(
            label_type=tag_type)
        embedding_types: List[TokenEmbeddings] = [WordEmbeddings('glove')]
        embeddings: StackedEmbeddings = StackedEmbeddings(
            embeddings=embedding_types)

        tagger: SequenceTagger = SequenceTagger(
            hidden_size=256, embeddings=embeddings, tag_dictionary=tag_dictionary, tag_type=tag_type, use_crf=True)

        trainer: ModelTrainer = ModelTrainer(tagger, corpus)
        trainer.train('logs',
                      learning_rate=0.1,
                      mini_batch_size=32,
                      max_epochs=15)

    def plot():
        logs = pd.read_csv('./logs/loss.tsv', sep='\t')
        figure = plt.figure()
        plt.plot(logs["EPOCH"], logs["TRAIN_LOSS"],
                 color='orange', label='loss')
        plt.plot(logs["EPOCH"], logs["DEV_LOSS"],
                 color='purple', label='dev_loss')
        figure.suptitle('Loss', fontsize=20)
        plt.legend(loc='upper left')
        plt.show()
