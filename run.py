from src.sentiment import sentimentCalculator as sentiment
from src.ner import Ner
from src.translators import GoogleTranslate, MicrosoftTranslator
from nltk.translate.bleu_score import sentence_bleu


def main():
    # Task 1
    print("Task 1:\n")
    task1_file = open('./datasets/tiny_movie_reviews_dataset.txt', 'r') # put all filenames at top! and one nitpick, relative filenames will break on some OSes
    task1_lines = task1_file.readlines()
    for i in range(len(task1_lines)):
        print(i + 1, sentiment(task1_lines[i]))
    
    print("\n\n\n")

    # Task 2
    print("Task 2:\n")
    ner_model = Ner()
    ner_model.train(0.3)
    ner_model.plot()
    
    print("\n\n\n")

    # Task 3
    print("Task 3:\n")
    microsoft_translator = MicrosoftTranslator()
    google_translate = GoogleTranslate()
    google_bleu_score = []
    microsoft_bleu_score = []
    task3_file = open('./datasets/europarl-v7es-en.txt', 'r')
    task3_lines = task3_file.readlines()
    task3_test_file = open('./datasets/europarl-v7en-es.txt', 'r')
    task3_test_lines = task3_test_file.readlines()

    for i in range(len(task3_lines)- 90):
        microsoft_translation = microsoft_translator.translate(task3_lines[i])
        google_translation = google_translate.translate(task3_lines[i])
        ref_microsoft = [microsoft_translation.split()]
        ref_google = [google_translation.split()]
        test = task3_test_lines[i].split()
        microsoft_bleu_score.append(sentence_bleu(ref_microsoft, test))
        google_bleu_score.append(sentence_bleu(ref_google, test))

    print(
        f'Microsoft BLEU score: {sum(microsoft_bleu_score) / len(microsoft_bleu_score)}')
    print(
        f'Google BLEU score: {sum(microsoft_bleu_score) / len(microsoft_bleu_score)}')


if __name__ == '__main__':
    main()
    
    """And be sure to add tests for all pieces of functionality! 
Tests should check that the functionality/outputs are as expected, not just that the code runs! 
When writing code, I write the test for each class or piece of functionality as soon as I finish that piece.
It helps you develop incrementally, being sure that each piece of code is clean and works like you expect it to! 
for tests, best practices are to have a structure like this: 
https://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure"""
