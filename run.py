from src.sentiment import sentimentCalculator as sentiment
from src.ner import NER
from src.translators import GoogleTranslate, MicrosoftTranslator
from nltk.translate.bleu_score import sentence_bleu


def main():
    # Task 1
    print("Task 1:\n")
    task1_file = open('./datasets/tiny_movie_reviews_dataset.txt', 'r')
    task3_file = open('./datasets/europarl-v7es-en.txt', 'r')
    task3_test_file = open('./datasets/europarl-v7en-es.txt', 'r')
    google_bleu_score = []
    microsoft_bleu_score = []

    task1_lines = task1_file.readlines()
    for i in range(len(task1_lines)):
        print(i + 1, sentiment(task1_lines[i]))
    
    print("\n\n\n")

    # Task 2
    ner_model = NER()
    print("Task 2:\n")
    ner_model.train(0.3)
    ner_model.plot()
    
    print("\n\n\n")

    # Task 3
    print("Task 3:\n")
    microsoft_translator = MicrosoftTranslator()
    google_translate = GoogleTranslate()
    task3_lines = task3_file.readlines()
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
