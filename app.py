from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load recipes from JSON
with open("recipes.json", "r", encoding="utf-8") as file:
    recipes = json.load(file)


def find_best_recipe(user_input):
    """
    Find the recipe that matches the highest number
    of ingredients entered by the user.
    """

    words = set(user_input.lower().split())

    best_recipe = None
    best_score = 0

    for recipe in recipes:

        ingredients = set(
            ingredient.lower()
            for ingredient in recipe["ingredients"]
        )

        score = len(words.intersection(ingredients))

        if score > best_score:
            best_score = score
            best_recipe = recipe

    return best_recipe


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_input = data.get("message", "")

    recipe = find_best_recipe(user_input)

    if recipe:

        reply = f"""
<h2>🍽️ {recipe['name']}</h2>

<p><b>⏱️ Preparation Time:</b> {recipe['time']}</p>

<p><b>👨‍👩‍👧 Serves:</b> {recipe['serves']}</p>

<h3>🛒 Ingredients</h3>

<ul>
"""

        for ingredient in recipe["ingredients"]:
            reply += f"<li>{ingredient}</li>"

        reply += "</ul>"

        reply += "<h3>👨‍🍳 Cooking Steps</h3><ol>"

        for step in recipe["instructions"]:
            reply += f"<li>{step}</li>"

        reply += "</ol>"

        reply += """
<hr>

<p><b>💡 SmartChef Tip:</b>
Serve hot with fresh chapati or steamed rice for the best taste.
</p>
"""

        return jsonify({
            "reply": reply
        })

    return jsonify({
        "reply": """
<h2>❌ Recipe Not Found</h2>

<p>
Sorry! I couldn't find a matching recipe.
</p>

<p>
Try ingredients like:
</p>

<ul>
<li>potato onion tomato</li>
<li>paneer butter</li>
<li>rice carrot beans</li>
</ul>
"""
    })


if __name__ == "__main__":
    app.run(debug=True)