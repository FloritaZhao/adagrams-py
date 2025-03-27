from random import randint

# #### Distribution of Letters

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():

# The first step is to create an empty list to store all the letters.
# But LETTER_POOL is a dictionary, we need to convert it into a list that represents the entire distribution of letters.
# Then, randomly select 1 letter from the letter pool (LETTER_POOL) using random.choice(), but we can not use .choice()
# So, let's use randint
# Check if the count of a specific letter exceeds the number assigned to that letter in the pool. If it does, redraw until a valid letter is selected. 
# This continues until the length of the empty list is greater than 10, so the condition was previously while len(empty_list) < 10.
# If the letter meets the criteria, append it to the list.

    all_letters = []
    for letter, count in LETTER_POOL.items():
        all_letters.extend([letter] * count)

    sel_ten = []
    # while len(sel_ten) < 10:
    #     sel_letter = all_letters[randint(0, len(all_letters) - 1)]
    #     if sel_ten.count(sel_letter) < LETTER_POOL[sel_letter]:
    #         sel_ten.append(sel_letter)

    while len(sel_ten) < 10:
        index = randint(0, len(all_letters) - 1)
        selected_letter = all_letters.pop(index)
        sel_ten.append(selected_letter)
    return sel_ten



def uses_available_letters(word, letter_bank):
# This function takes two parameters: word and letter_bank.
# First, convert the player's word to uppercase and split it into characters.
# Then, split letter_bank into individual characters and convert it into a dictionary with key of the letter and value of the count.
# Check each character in word:
# If the character is not in letter_bank, return False immediately.
# If the character is in letter_bank, decrease the count of that letter in the letter_bank dictionary by 1. 
# If this count becomes less than 0, return False immediately.
# If the loop completes without returning False, return True.

    letter_bank_dic = {}
    for char in letter_bank:
        letter_bank_dic[char] = letter_bank_dic.get(char, 0) + 1
    
    for char in word.upper():
        if letter_bank_dic.get(char, 0) == 0:
            return False
        letter_bank_dic[char] -= 1
    
    return True


def score_word(word):
# This function takes one parameter, Word.
# If Word is None, thenreturns 0.
# The score is calculated based on the letters used in the word, where each letter has a fixed point value.
# If the word length is ≥ 7, an additional 8 points are added to the score.
   
    SCORE_CHART = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }

    credit = 0
    for char in word.upper():
        credit += SCORE_CHART.get(char, 0)
    
    bonus_min_length = 7
    length_bonus_point = = 8
    
    if len(word) >= bonus_min_length:
        credit += length_bonus_point
    return credit


def get_highest_word_score(word_list):

# Has one parameter: `word_list`, which is a list of strings
# - Returns a tuple that represents the data of a winning word and it's score.  
# The tuple must contain the following elements:
# index 0 ([0]): a string of a word
#index 1 ([1]): the score of that word
# In the case of tie in scores, use these tie-breaking rules:
#     - prefer the word with the fewest letters...
#     - ...unless one word has 10 letters. If the top score is tied between multiple words and one is 10 letters long, choose the one with 10 letters over the one with fewer tiles
#     - If the there are multiple words that are the same score and the same length, pick the first one in the supplied list
    
    # highest_score = -1
    # best_word = word_list[0]

    # Step 1: Score all words and find the max score
    scored_words = [(word, score_word(word)) for word in word_list]
    max_score = max(score for word, score in scored_words)

    
    # Step 2: Filter all words with the max score
    top_words = [word for word, score in scored_words if score == max_score]

    # Step 3: Apply tie-breaking rules - 2 rules
    
    # Rule 1: Prefer word with length 10

    for word in top_words:
        if len(word) == 10:
            return (word, max_score)
            
    # Rule 2: Prefer word with fewest letters
    
    shortest_word = min(top_words, key=len)
    return (shortest_word, max_score)
    
    # for word in word_list:
    #     score = score_word(word)
    #     if score > highest_score:
    #         highest_score, best_word = score, word
        
    #     if score == highest_score:
    #         if len(word) == 10 and len(best_word) != 10:
    #             highest_score, best_word = score, word
                
    #         elif len(best_word) != 10 and len(word) < len(best_word):
    #             highest_score, best_word = score, word
    #         else: 
    #             highest_score, best_word
    # return (best_word, highest_score)
