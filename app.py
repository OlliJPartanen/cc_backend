from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# ChatGPT was used to figure out how flask-CORS works. Check report for more info
app = Flask(__name__)
CORS(app)

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

    return f"""
    <p>Test comment 1: {test1_comment} --- {test1}</p>
    <p>Test comment 2: {test2_comment} --- {test2}</p>
    <p>Test comment 3: {test3_comment} --- {test3}</p>"""

# POST-method for data endpoint. Print name-info presented in the request body
@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    body_data = request.json

    # Define sid as a sentimelIntensityAnalysis variable
    sid = SentimentIntensityAnalyzer()
    
    # print comment to console and create variable of is
    comment = body_data["comment"]
    print(comment)

    # Create polarity score and print it
    comment_polarity = sid.polarity_scores(comment)
    print(comment_polarity)

    # Return comment_polarity to frontend
    return {'response': comment_polarity}

if __name__ == '__main__':

    #app.run()
    app.run(host="0.0.0.0", port="5000", debug=True)