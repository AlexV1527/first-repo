"""
Assignment 5: Simple Sentiment Analyzer

Instructions:
1. Modify the `positive_words` and `negative_words` sets below:
   - **Add at least 15 positive words** and **15 negative words** of your choice.
   - Ensure words are lowercased and contain only alphabetic characters.
2. Print positive lexicon & negative lexicon
3. Compute simple sentiment score (hint: positive - negative count)
4. Print the output results
5. Add a short reflection as comments at the bottom:
   - Discuss **strengths** and **limitations** of this lexicon-based approach (2–3 sentences).

Deliverables:
- Completed Python script (`sentiment_analyzer.py`).

"""

# --- Grading Rubric (Total: 60 pts) ---
#
# | Criteria                                                          | Points |
# |:------------------------------------------------------------------|:-------|
# | Lexicon completeness (≥15 positive & ≥15 negative words)           |   20   |
# | Display of positive & negative lexicons                            |    5   |
# | Sentiment score computation & correct labeling                    |   15   |
# | Interactive testing functionality (I/O loop, 'exit' handling)     |   10   |
# | Code readability and comments                                     |    5   |
# | Reflection quality (insightful strengths & limitations)          |    5   |
#
# **Total Points:** 60

import re


def clean_text(text):
    """
    Lowercase, remove punctuation, and split into tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    tokens = text.split()
    return tokens

# 1. Add 15 positive and 15 negative to your expand the knowledge base


positive_words = {
    'happy', 'joyful', 'confident', 'kind', 'wondeful', 'amazing', 'fantastic', 'thankful', 'greatful', 'content', 'appreciative',
    'friendly', 'passionate', 'supportive', 'brave', 'impressive'
}
negative_words = {
    'sad', 'dishonest', 'impatient', 'mad', 'hurt', 'mean', 'nasty', 'angry', 'crazy', 'dead', 'disease', 'insane', 'jealous',
    'rude', 'controlling', 'sinister'
}

# 2. print positive lexicon & negative lexicon:
print('These are the positive lexicons: ', positive_words)
print('These are the negative lexicons: ', negative_words)

# --- Interactive Sentiment Testing ---
print("\nEnter sentences to analyze sentiment (type 'exit' to quit):")
while True:
    text = input('> ').strip()
    if text.lower() in ('exit', 'quit'):
        print("Goodbye!")
        break

    tokens = clean_text(text)
    pos_count = sum(1 for t in tokens if t in positive_words)
    neg_count = sum(1 for t in tokens if t in negative_words)
    total = len(tokens)

# 3. Compute simple sentiment score (hint: positive - negative count)
    score = 0

    # Determine sentiment label
    if score > 0:
        sentiment = 'Positive'
    elif score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # sentiment score
    score = pos_count - neg_count

# 4. print the output results
    print(f"Tokens: {tokens}")
    print(f"+ matches: {pos_count}, - matches: {neg_count}")
    print(f"Score: {score:.3f} => {sentiment}\n")
    print('Positive word count:', pos_count)
    print('Negative word count: ', neg_count)
    print('Sentiment total score: ', score)

# 5. Add a short reflection as comments at the bottom (2–3 sentences)
"""
It is very easy and simple to understand making it an easy approach to go by plus the addition of it being a fast process.
It is very time consuming if it were to be with more complicated phrases or where the negative or positive words are not in the database.
I say it makes it complicated because you have to manually put in the database like positive and negative words which there is a ton
of words out there that can be defined as positive or negative.

"""
