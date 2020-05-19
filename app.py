from flask import Flask, request, redirect, render_template, jsonify
import json
# from flask_pymongo import PyMongo
import search
import mongo

app = Flask(__name__)

selection = ["Recipe_One", "Recipe_Two", "Recipe_Three"]
desc = ["Description_one", "Description_two", "Description_three" ]

# set up the connection

@app.route('/')
def index():

    return render_template('index.html', top1=selection[0], 
                                         top2=selection[1], 
                                         top3=selection[2],
                                         desc1=desc[0],
                                         desc2=desc[1],
                                         desc3=desc[2],)


@app.route('/search_recipe', methods=['POST'])

def search_recipe():

    # Grab user's query input
    # Select the top 3 recipes and store their id in selection
    query = request.form['query']
    selection = search.get_selection_top3(query)
    for i in range(len(selection)):
        mongo.query_recipe(int(selection[i]))

    # jpg = list()
    recipe_data = list()

    for recipe_id in selection:

        recipe = mongo.query_recipe(int(recipe_id))
        interaction = mongo.query_interaction(int(recipe_id))

        recipe_info = mongo.get_recipe_info(recipe, interaction)

        recipe_data.append(recipe_info)
    
    with open("static/data/top3_data.json", 'w') as f:
        json.dump(recipe_data, f)
    
    
    

    return render_template('index.html', top1=recipe_data[0]['recipe_name'], 
                                        top2=recipe_data[1]['recipe_name'], 
                                        top3=recipe_data[2]['recipe_name'],
                                        desc1=recipe_data[0]['description'],
                                        desc2=recipe_data[1]['description'],
                                        desc3=recipe_data[2]['description'],)

if __name__ == '__main__':
    app.run(debug=True)