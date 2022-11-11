from sentiment import sentimentCalculator as sentiment
from ner import Ner

def main():
    # Task 1
    task1_file = open('./datasets/tiny_movie_reviews_dataset.txt', 'r')
    task1_lines = task1_file.readlines()
    for i in range(len(task1_lines)):
        print(i + 1, sentiment(task1_lines[i]))

    # Task 2
    ner_model = Ner('')

if __name__ == '__main__':
    main()
