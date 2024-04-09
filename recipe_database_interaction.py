def find_recipes_by_ingredients(available_ingredients):
    # Sample "database" of recipes
    recipes = [
        ('Tomato Soup', 'tomato, onion, garlic, basil'),
        ('Cheese Pizza', 'dough, tomato sauce, cheese'),
        ('Grilled Cheese Sandwich', 'bread, cheese, butter'),
        ('Tomato and Cheese Salad', 'tomato, cheese, basil, olive oil')
    ]
    
    # Find recipes that match the available ingredients
    matched_recipes = []
    for name, ingredients in recipes:
        if all(ingredient in ingredients for ingredient in available_ingredients):
            matched_recipes.append((name, ingredients))
    
    return matched_recipes

# Example usage
if __name__ == "__main__":
    available_ingredients = ['tomato', 'cheese']
    recipes = find_recipes_by_ingredients(available_ingredients)
    print("Found recipes:", recipes)
