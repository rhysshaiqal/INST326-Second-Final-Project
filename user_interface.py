import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Recipe Recommendation System')
    parser.add_argument('--ingredients', nargs='+', help='List of available ingredients separated by space', required=True)
    parser.add_argument('--diet', help='Dietary preference', choices=['vegan', 'vegetarian', 'gluten-free', 'none'], default='none')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Available ingredients: {args.ingredients}")
    print(f"Dietary preference: {args.diet}")
    # Here, you would call your recommendation system function with these inputs
