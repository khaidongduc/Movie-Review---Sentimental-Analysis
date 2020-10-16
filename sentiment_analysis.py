# Khai Dong
# the purpose of the program is to determine the general attitude of a writer given some text they have
# written.

def make_word_sentiment_dictionary(file_name):
    """
    take the name of a file with movie reviews as a parameter and return a word
    sentiment dictionary. The keys in this dictionary are individual words, and the values are
    small dictionaries that assemble the following information about the word:
    - the sum of the sentiment scores of the movie reviews in which the word appears (key:
      "total score")
    - the number of movie reviews in which the word appears (key: "count")
    - the average sentiment score of the movie reviews in which the word appears (key: "average score")
    """
    file = open(file_name, "r")
    word_sentiment_dict = {}
    for line in file:
        score, review = int(line[0]), line[2:].strip()
        for word in review.split():
            word = word.lower()
            if word not in word_sentiment_dict:
                word_sentiment_dict[word] = {'total score': 0, 'count': 0}
            word_sentiment_dict[word]['total score'] += score
            word_sentiment_dict[word]['count'] += 1
    file.close()
    for key in word_sentiment_dict:
        total, count = word_sentiment_dict[key]['total score'], word_sentiment_dict[key]['count']
        word_sentiment_dict[key]['average score'] = total / count
    return word_sentiment_dict

def predict_sentiment_score(reivew, word_sentiment_dict):
    """
    Given a movie review as a string and a word sentiment dictionary,
    return an estimated sentiment score for the review.
    """
    total_score, count = 0, 0
    for word in reivew.split():
        word = word.lower()
        total_score += (2 if (word not in word_sentiment_dict) else
                        word_sentiment_dict[word]['average score'])
        count += 1
    return total_score / count

def is_positive(review, word_sentiment_dict):
    """
    takes a movie review and a word sentiment dictionary and classifies the review as either positive
    (i.e. humans would give it a score of 3 or 4 ) or not.
    """
    return (predict_sentiment_score(review, word_sentiment_dict) >= 2)

## Evaluation

def evaluate(word_sentiment_dict, filename):
    f = open(filename, "r")
    correct = 0
    incorrect = 0
    for line in f:
        line = line.strip()
        score = int(line[0])
        words = line[2:]
        predicted_positive = is_positive(words, word_sentiment_dict)
        if score > 2 and predicted_positive:
            correct += 1
        elif score <= 2 and not predicted_positive:
            correct += 1
        else:
            incorrect += 1
    f.close()
    print("predicted correctly:", correct, "("+str(correct/(correct+incorrect))+")")
    print("predicted incorrectly:", incorrect, "("+str(incorrect/(correct+incorrect))+")")


### DO NOT DELETE THIS LINE: beg testing
    
word_sentiment_dictionary = make_word_sentiment_dictionary("movie_reviews_training.txt")

print("nice", word_sentiment_dictionary["nice"])
print("story", word_sentiment_dictionary["story"])

print(predict_sentiment_score("This movie is awesome !", word_sentiment_dictionary))

evaluate(word_sentiment_dictionary, "movie_reviews_dev.txt")
