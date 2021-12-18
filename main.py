#import required libraries
import nltk
import json
import re
import plotly.graph_objects as go
from nltk.corpus import stopwords
from textblob import TextBlob
from collections import defaultdict
from statistics import mean
from plotly.subplots import make_subplots
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#Download corpus
nltk.download('words')
nltk.download('stopwords')
nltk.download('wordnet')
words = set(nltk.corpus.words.words())
stop_words = set(stopwords.words('english'))

#Add extra words to the corpus so that they are not missed out

words.add('DOGE')
words.add('SHIB')
words.add('shib')
words.add('doge')
words.add('dogecoin')
words.add('shibcoin')

#Select Stemmer and Lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

#Filter text for English language only
def filter_text(message):
    result = " ".join(lemmatizer.lemmatize(stemmer.stem(w)) for w in nltk.wordpunct_tokenize(message) if
                      (w.lower() in words and w not in stop_words) or not w.isalpha())
    return result

#Refine data by removing white spaces and numbers
def refine_data(message_string):
    # remove whitespace
    message_string = message_string.strip()
    # lowercase
    message_string = message_string.lower()
    # remove numbers
    message_string = re.sub(r'\d+', '', message_string)
    # remove punctuation
    imessage_string = re.sub(r'[^\w\s]', '', message_string)
    return message_string

#Read Chat from json
def read_chat_json(path):
    map_result = defaultdict(list)
    with open(path, "r",encoding='utf8') as read_file:
        result_data = json.load(read_file)
        for document in result_data['messages']:
            #select appropriate date
            date = document['date'][0:10]
            #select text message
            text_message = document['text']
            #flatten the message in case of a list
            if type(text_message) is list:
                flattened_message = ''
                for i in range(len(text_message)):
                    if type(text_message[i]) is str:
                        flattened_message += (text_message[i])
                    else:
                        flattened_message += (text_message[i]['text'])
                map_result[date].append(refine_data(flattened_message))
            else:
                map_result[date].append(refine_data(text_message))
        return map_result

if __name__ == "__main__":
    filtered_messages = defaultdict(list)
    sentiment_dict = defaultdict(float)
    number_of_messages = defaultdict(int)
    #Relative path to the folder
    data = read_chat_json("./result.json")
    for date, list_of_messages in data.items():
        for sentence in list_of_messages:
            if 'DOGE' in sentence or 'SHIB' in sentence or 'doge' in sentence or 'shib' in sentence:
                filtered_messages[date].append(TextBlob(filter_text(sentence)).sentiment[0])
    #Sentiment analysis
    for date, list_sentiment in filtered_messages.items():
        sentiment_dict[date] = mean(list_sentiment)
        number_of_messages[date] = len(list_sentiment)

    #print the results to console
    print("Sentiments:")
    print(dict(sentiment_dict))
    print("Message Counts:")
    print(dict(number_of_messages))

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=list(number_of_messages.keys()), y=list(number_of_messages.values()), name="Number of Message over time"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=list(sentiment_dict.keys()), y=list(sentiment_dict.values()), name="Sentiment of messages over time"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text="Plot"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Date")

    # Set y-axis titles
    fig.update_yaxes(title_text="Number-Of-Messages", secondary_y=False)
    fig.update_yaxes(title_text="Sentiment", secondary_y=True)

    fig.show()



