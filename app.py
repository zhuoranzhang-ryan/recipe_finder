from flask import Flask, redirect, render_template
# from flask_pymongo import PyMongo

app = Flask(__name__)


# read csv into pandas
# set up the mongo connection
# calculate the tfidf matrix

@app.route('/')
def index():
    
    return render_template('index.html')



# # @app.route('/about)
# def search(search query):

#     python search.py

    #   NLP.py    run get_recipe(search_query)


    """read the csv into pandas"""
    """NLP tfidf """

#     return (id)


if __name__ == '__main__':
    app.run(debug=True)