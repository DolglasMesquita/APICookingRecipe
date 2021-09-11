from flask import Flask, request
from resources.recipes import recipes
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)

def findRecipe(id):  # HELPER BUSCA
    for recipe in recipes:
        if recipe['id'] == id:
            return recipe

@app.route('/recipes', methods=['GET']) # GET ALL
def getAll():
    return { 'recipes' : recipes }


@app.route('/recipes/<int:id>', methods=['GET']) #GET POR ID
def getById(id):
    recipe = findRecipe(id)
    if recipe:
        return recipe
    return {'message': 'Not found!'}, 404


@app.route('/recipes', methods=['POST']) # POST
def postRecipe():
    data = request.get_json()
    new_recipes = {
        'id':  random.randrange(1, 9999),
        'name': data['name'],
        'ingredients': data['ingredients'],
        'description': data['description']
    }
    recipes.append(new_recipes)
    return 'Cadastrado com sucesso', 201


@app.route('/recipes/<int:id>', methods=['PUT']) # PUT
def updateRecipe(id):
    data = request.get_json()
    recipe = findRecipe(id)
    new_recipes = {
        'id':  id,
        'name': data['name'],
        'ingredients': data['ingredients'],
        'description': data['description']
    }
    if recipe:
        recipe.update(new_recipes)
        return 'atualizado com sucesso!', 200
    return 'Not found!', 404


@app.route('/recipes/<int:id>', methods=['DELETE']) # DELETE
def gdeleteRecipe(id):
    recipe = findRecipe(id)
    if recipe:
        global recipes
        recipes = [recipe for recipe in recipes if recipe['id'] != id]
        return 'Deletado com sucesso!', 200    
    return {'message': 'Not found!'}, 404


if __name__ == '__main__':
    app.run(debug=True)
