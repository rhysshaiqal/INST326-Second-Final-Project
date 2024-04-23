import argparse

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Recipe Recommendation System')
    parser.add_argument('--ingredients', nargs='+', help='List of available ingredients separated by space', required=True)
    parser.add_argument('--diet', help='Dietary preference', choices=['vegan', 'vegetarian', 'gluten-free', 'none'], default='none')
    args = parser.parse_args()
    return args

# Sample "database" of recipes
recipes = [
    ('Tomato Soup', 'tomato, onion, garlic, basil', 'vegetarian'),
    ('Cheese Pizza', 'dough, tomato sauce, cheese', 'vegetarian'),
    ('Grilled Cheese Sandwich', 'bread, cheese, butter', 'vegetarian'),
    ('Tomato and Cheese Salad', 'tomato, cheese, basil, olive oil', 'vegetarian'),
    ('Vegan Salad', 'tomato, cucumber, lettuce, olive oil', 'vegan')
]

# Function to find recipes by available ingredients
def find_recipes_by_ingredients(available_ingredients, diet_preference):
    matched_recipes = []
    for name, ingredients, diet in recipes:
        if all(ingredient.strip() in ingredients for ingredient in available_ingredients) and (diet == diet_preference or diet_preference == 'none'):
            matched_recipes.append((name, ingredients))
    return matched_recipes

# Main function to execute the recipe recommender
def main():
    args = parse_arguments()
    available_ingredients = args.ingredients
    diet_preference = args.diet

    # Find recipes based on ingredients and dietary preference
    recipes = find_recipes_by_ingredients(available_ingredients, diet_preference)
    
    # Print the matched recipes
    if recipes:
        print("Found recipes based on your ingredients and dietary preference:")
        for name, ingredients in recipes:
            print(f"- {name}: Ingredients: {ingredients}")
    else:
        print("No recipes found that match the available ingredients and dietary preference.")

# Run the main function if this is the main module
if __name__ == "__main__":
    main()
