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

    # Grab user's query input
    # Select the top 3 recipes and store their id in selection
    query = request.form['query']
    selection = search.get_recipe_top3(query)

    jpg = list()
    recipe_data = list()
    for recipe_id in selection:
        # Sebscraping and making query using recipe_id
        url = search.scrape(recipe_id)
        recipe = mongo.find_one("recipe_id": recipe_id)

        # appending data into arrays.
        jpg.append(url)
        recipe_data.append(recipe)
    
    return render_template('index.html', top1=selection[0], top2=selection[1], top3=selection[2])

if __name__ == '__main__':
    app.run(debug=True)