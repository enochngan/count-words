import pandas as pd
import numpy as np

def count_words_in_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Initialize a counter for the words
    word_count = 0
    words_com = np.array([])
    
    # Iterate through each cell in the DataFrame and count the words
    for column in df.columns:
        for item in df[column]:
            if pd.notna(item):  # Check if the cell is not NaN
                words = str(item).split()
                word_count += len(words)
                words_com = np.append(words_com, words)

    return word_count, words_com

def count_words(array):

    word_counter = pd.Series()

    for word in array:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    
    return word_counter

if __name__ == "__main__":
    file_path = '/Users/enochngan/Library/CloudStorage/OneDrive-BostonUniversity/Literary Epigraphs in Nora Roberts’ Novels/copy1.csv'
    total_words, words_com = count_words_in_csv(file_path)
    counter = count_words(words_com)
    print(f"Total number of words in the CSV file: {total_words}")
    print(counter)