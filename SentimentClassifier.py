def strip_punctuation(word):
    for ch in word:
        if ch in punctuation_chars:
            word=word.replace(ch,"")
    return word

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(sent1):
    sent1 = strip_punctuation(sent1).split()
    pos=0
    for ch in sent1:
        ch=ch.lower()
        if ch in positive_words:
            pos+=1
    return pos

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(str):
    str = strip_punctuation(str).split()
    k = 0
    for i in str:
        if i in negative_words:
            k += 1
    return k 

resultfile = open("resulting_data.csv", "w")
resultfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
resultfile.write('\n')


csv_file = open('project_twitter_data.csv', "r")
lines = csv_file.readlines()
headerDontUsed= lines.pop(0)
for line in lines:
    line_list = line.strip().split(",")
    resultfile.write('{},{},{},{},{}'.format(line_list[1], line_list[2], get_pos(line_list[0]), get_neg(line_list[0]), (get_pos(line_list[0]) - get_neg(line_list[0]))))
    resultfile.write("\n")

csv_file.close()
resultfile.close()
