# Sentiment Analysis of Telegram Chat based on Crypto currency 
## Task for ISI MINDS 



This is the repository for sentiment analysis on Telegram chat. The data is taken from the channel Crypto.com covering the messages from May 1 to May 15, 2021.
I have downloaded the chat from the link: https://t.me/CryptoComOfficial
I have used python's Natural Language toolkit for the task. For plotting the graph I have used plotly and TextBlob was used for sentiment analysis.

### List of libraries required for the project

- nltk
- TextBlob 
- plotly
- re
- json


All the required libraries have been mentioned in requirements.txt

## Pre-processing
To avoid any issues, I have removed all the white spaces, numbers and punctuations from the text. I have also converted the text to lower case
```sh
def refine_data(message_string):
    message_string = message_string.strip()
    message_string = message_string.lower()
    message_string = re.sub(r'\d+', '', message_string)
    imessage_string = re.sub(r'[^\w\s]', '', message_string)
    return message_string
```
As required, I have filtered the messages and restricted them to English Language only.
```sh
def filter_text(message):
    result = " ".join(lemmatizer.lemmatize(stemmer.stem(w)) for w in nltk.wordpunct_tokenize(message) if
                      (w.lower() in words and w not in stop_words) or not w.isalpha())
    return result
```
## Steps to run the project
- Run: git clone https://github.com/yashshah15/sentiment-analysis.git
- Run: pip install -r requirements.txt to install the required packages
- Navigate to the folder sentiment-analysis
- Execute the command: python main.py

## Output
The output is a graph containing the sentiment level and count of the messages over time. The sentiment and message count is also printed to the console.
```sh
Sentiments:
{'2021-05-01': 0.05224510732323232, '2021-05-02': 0.03794871794871795, '2021-05-03': 0.03477011494252873, '2021-05-04': 0.011529401154401153, '2021-05-05': 0.024464172979797978, '2021-05-06': 0.04442239858906526, '2021-05-07': 0.04437412442881193, '2021-05-08': 0.026759159530048877, '2021-05-09': 0.04190592710209498, '2021-05-10': 0.02699087848196435, '2021-05-11': 0.04196743684695492, '2021-05-12': 0.039460712243731114, '2021-05-13': 0.04981399492763129, '2021-05-14': 0.03495374990071091, '2021-05-15': 0.05786441642772812}  
Mesage Count:
{'2021-05-01': 48, '2021-05-02': 13, '2021-05-03': 29, '2021-05-04': 120, '2021-05-05': 96, '2021-05-06': 72, '2021-05-07': 135, '2021-05-08': 709, '2021-05-09': 274, '2021-05-10': 773, '2021-05-11': 249, '2021-05-12': 159, '2021-05-13': 198, '2021-05-14': 109, '2021-05-15': 77}
```
The Graph generated for the result will pop up and the browserr windown on the address: http://127.0.0.1:53580/
![Output plot](output.png?raw=true "Sentiment and Message count comparison")
The above plot shows the sentiment of people compared to the count of messages from May 1 to May 15. The sentiment is neutral as shown by the graph. This is because the overall positive and negative sentiment was almost equal during the period. This may be because of the situation of the crypto market during that period