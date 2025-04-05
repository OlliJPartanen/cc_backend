from flask import Flask, request
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

# Empty route Hello world test
@app.route("/")
def hello_world():

    sid = SentimentIntensityAnalyzer()
    test1_comment = "BAD, SAD, NEGATIVE"
    test2_comment = "GOOD, LOVELY, SUPER"
    test3_comment = "MEH, OK, AVERAGE"
    test1 = sid.polarity_scores(test1_comment)
    test2 = sid.polarity_scores(test2_comment)
    test3 = sid.polarity_scores(test3_comment)

    # Lähde datasettien yhdistämiseksi https://datascience.stackexchange.com/questions/81617/how-to-combine-and-separate-test-and-train-data-for-data-cleaning
    main_df_test = pd.read_csv("dataset/test.csv", encoding='latin-1')
    main_df_train = pd.read_csv("dataset/train.csv", encoding='latin-1')

    # Yhdistetään train ja test datasetit
    main_df = pd.concat([main_df_test.assign(ind="test"), main_df_train.assign(ind="train")])
    # Tarkastetaan nullsum
    main_df.dropna(inplace=True)
    main_df.isnull().sum()

    return f"""
    <p>Test comment 1: {test1_comment} --- {test1}</p>
    <p>Test comment 2: {test2_comment} --- {test2}</p>
    <p>Test comment 3: {test3_comment} --- {test3}</p>"""

# POST-method for data endpoint. Print name-info presented in the request body
@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    input_data = request.json
    print(input_data)
    # Sentiment alasysis here!


    return {'input_data': 'message', "data": "Message testing! HELLO!"}

if __name__ == '__main__':

    #app.run()
    app.run(host="0.0.0.0", port="5000", debug=True)