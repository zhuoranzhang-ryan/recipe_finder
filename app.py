from flask import Flask, request, redirect, render_template
# from flask_pymongo import PyMongo
import search

app = Flask(__name__)

print(search.get_recipe_top3('beef broccoli'))

selection = ["Recipe_One", "Recipe_Two", "Recipe_Three"]

@app.route('/')
def index():

    return render_template('index.html', top1=selection[0], top2=selection[1], top3=selection[2])


@app.route('/search_recipe', methods=['POST'])

def search_recipe():

    query = request.form['query']
    selection = search.get_recipe_top3(query)
    print(selection)
    
    return render_template('index.html', top1=selection[0], top2=selection[1], top3=selection[2])



if __name__ == '__main__':
    app.run(debug=True)