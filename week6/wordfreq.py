# wordfreq.py

def byFreq(pair):
    return pair[1]

def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = input("File to analyze: ")
    text = open(fname,'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()
    # add stopwords list
    stopwords = ['a','an','and','as','at','be','but','etc','for','if','in','it','its','is','of','or','so','such','the','this','to','with']
    # open the file for negative words and positive words
    negWords = open('negative-words.txt','r', encoding='utf-8', errors='ignore').read().splitlines()[35:]
    posWords = open('positive-words.txt','r', encoding='utf-8', errors='ignore').read().splitlines()[35:]
    # construct a dictionary of word counts, negative word counts and postive word counts
    counts = {}
    negCounts ={}
    posCounts = {}
    # add score variable to keep track of sentiment score. Increment for negative words and decrement for positive words.
    score = 0
    for w in words:
        # check if word is a stop word. If so don't add to counts dictionary
        if w not in stopwords:
            counts[w] = counts.get(w,0) + 1
        # check if word is a negative word. If so add to negCounts dictionary 
        if w in negWords:
            negCounts[w] = negCounts.get(w,0) + 1
            score -= 1
        # check if word is a positive word. If so add to posCounts dictionary
        if w in posWords:
            posCounts[w] = posCounts.get(w,0) + 1
            score += 1
    # output analysis of n most frequent words.
    n = int(input("Output analysis of how many words? "))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))
    # output analysis of 5 most negative frequent words.
    negitems = list(negCounts.items())
    negitems.sort()
    negitems.sort(key=byFreq, reverse=True)
    print("The top 5 negative words in these reviews are: ")
    for n in range(5):
        word, count = negitems[n]
        print("{0:<15}{1:>5}".format(word, count))
    # output analysis of 5 most positive frequent words.
    positems = list(posCounts.items())
    positems.sort()
    positems.sort(key=byFreq, reverse=True)
    print("The top 5 positive words in these reviews are: ")
    for n in range(5):
        word, count = positems[n]
        print("{0:<15}{1:>5}".format(word, count))
    # print the sentiment score
    print("The sentiment score for these reviews is",score)
if __name__ == '__main__':  main()