import nltk
import nltk.corpus
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
import spacy
import string
from googletrans import Translator
import googletrans
from langdetect import detect


html_reg = re.compile('<.*?>')
lem = WordNetLemmatizer()
sp_parser = spacy.load('en_core_web_sm', disable=['parser','ner'])


def remove_emoji(review_string):
    review_string = review_string.translate(str.maketrans('', '', string.punctuation))
    return review_string

def remove_html_tag(review):
    cleanReview = re.sub(html_reg,'',review)
    return cleanReview

def convert_to_lowercase(line):
    low_sent = []
    for l in line:
        low_sent.append(l.lower())
    return low_sent

def remove_stop_words(low_output):
    stop_word_remove_output = []
    for word in low_output:
        if word not in remove_words:
            stop_word_remove_output.append(word)
    return stop_word_remove_output


def lemmaization(review):
    sent = sp_parser(review)
    return " ".join(word.lemma_ for word in sent)

        
text_data = pd.read_csv('vaibhav.csv')
count=1
review_list = []


review_df = text_data[text_data['translated'].notna()]
# first_20 = review_df.head(20)
comments = review_df["translated"]




for comment in comments:
    print("Review number:{}\n".format(count))

    # try:
    print("Comment", comment)
    print("\n")
    # if comment!='' and comment!='NA' and len(comment)>0:
    comment_without_tags = remove_html_tag(comment)
    comment_no_emoji = remove_emoji(comment_without_tags)
    lem_str = lemmaization(comment_no_emoji)

    tokenizer = CountVectorizer().build_tokenizer()
    output = tokenizer(lem_str)

    remove_words = set(stopwords.words('english'))
    low_output = convert_to_lowercase(output)
    final_word = remove_stop_words(low_output)

    print("What is final word", final_word)

    final_com = " ".join(final_word)

    review_list.append(final_com)
    count+=1


    # except Exception as e:
    #     print("Exception", e)

print("length of list", len(review_list))

# # for word in review_list:
# #     print(word)
# #     print("\n")
# print(text_data.head())

review_df['tokenized_text'] = review_list
review_df.to_csv("tokenized_v2.csv")


