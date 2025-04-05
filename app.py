from flask import Flask, request;

app = Flask(__name__)

# Empty route Hello world test
@app.route("/")
def hello_world():
    return "<p>Hello version 4 published DEV branch</p>"

# POST-method for data endpoint. Print name-info presented in the request body
@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    input_data = request.json
    print(input_data)
    print("testString")
    # Sentiment alasysis here!


    return {'input_data': 'message', "data": "Message testing! HELLO!"}

if __name__ == '__main__':
    #app.run()
    app.run(host="0.0.0.0", port="5000", debug=False)