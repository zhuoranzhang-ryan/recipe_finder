import os
import pandas as pd
import numpy as np
import random
import json
import pymongo
from pymongo import MongoClient
import dns

# Set up connection to interaction database
conn_interaction = 'mongodb+srv://ryan:ryan@cluster0-nt08n.mongodb.net/ReciPurrrr'
client_interaction = pymongo.MongoClient(conn_interaction)
db_interaction = client_interaction.ReciPurrrr
collection_interaction = db_interaction.metadata

# Set up connection to recipe database
conn_recipe = 'mongodb+srv://ryan:recipurrrrr_admin@cluster0-os0o2.mongodb.net/recipurrrrr'
client_recipe = pymongo.MongoClient(conn_recipe)
db_recipe = client_recipe.recipurrrrr

collection_recipe = db_recipe.recipes

def query_recipe(id):
    
    output_recipe = collection_recipe.find_one({'recipe_id':137739})

    return output_recipe

def query_interaction(id):
    
    output_interaction = collection_interaction.find_one({'recipe_id':137739})

    return output_interaction

def get_recipe_info(recipe, interaction):

    recipe_dict = dict()
    recipe_dict['recipe_id'] = recipe['recipe_id']
    recipe_dict['prep_time'] = recipe['prep_time']
    recipe_dict['nutrition_info'] = recipe['nutrition_info']
    recipe_dict['prep_steps'] = recipe['prep_steps']
    recipe_dict['description'] = recipe['description']
    recipe_dict['recipe_name'] = recipe['recipe_name']
    recipe_dict['rating'] = interaction['rating']
    recipe_dict['review'] = interaction['review']

    return recipe_dict