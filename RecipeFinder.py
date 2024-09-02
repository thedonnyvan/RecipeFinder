import requests # To retrieve data from Spoonacular API
import re #
from colorama import Fore, Style, init # Colorama will add color to the ouputed text

init(autoreset=True) #Resets the color to default after prints

api = "3cac6a8ce8fb428a96343ed623455f7c" #Insert your own OpenWeatherMap API

def find_recipes(query, number=10, offset=0):
    url = f'https://api.spoonacular.com/recipes/complexSearch?query={query}&number={number}&offset={offset}&apiKey={api}'
    response = requests.get(url) # Sends a GET request to the API
    
    if response.status_code == 200: # Checks if request was successful
        data = response.json() # Parse the JSON data returned by the API
        return data['results']
    else:
        print(Fore.RED + "Error: Cannot Fetch Data")
        return None
    
def get_recipe_info(recipe_id):
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?includeNutrition=false&apiKey={api}'

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        title = data['title']
        ready_in_minutes = data['readyInMinutes']
        servings = data['servings']
        instructions = data['instructions']
        ingredients = [(ingredient['name'], ingredient['amount'], ingredient['unit']) for ingredient in data['extendedIngredients']]
        
        vegetarian = data['vegetarian']
        vegan = data['vegan']
        gluten_free = data['glutenFree']
        dairy_free = data['dairyFree']
        
        return title, ready_in_minutes, servings, instructions, ingredients, vegetarian, vegan, gluten_free, dairy_free
    else:
        print(Fore.RED + "Error: Cannot Fetch Data")
        return None


def format_instructions(instructions):
    instructions = re.sub(r'<[^>]+>', '', instructions) #removes HTML tags
    instructions = instructions.replace('\n', ' ').strip() #removes empty spaces and newlines
    #makes sure periods after units do not append another instruction
    pattern = re.compile(r'(?<!\b(?:in|cm|mm|ft)\b)\.\s+(?=[A-Z0-9])') 
    steps = pattern.split(instructions)
    
    combined_steps = []
    for step in steps:
        if combined_steps and step.strip().lower() in ["and", "then", "next", "after"]:
            combined_steps[-1] += " " + step.strip()
        else:
            combined_steps.append(step.strip())

    formatted_instructions = ""
    for i, step in enumerate(combined_steps, 1):
        if step:
            formatted_instructions += f"{i}. {step.strip()}.\n"
    return formatted_instructions


def main():
    print(Fore.YELLOW + "Welcome to the Recipe Finder! This program allows you to search for delicious \nrecipes based on the type of dish you want to make. Not only does it provide detailed \ninstructions and ingredients, but it also offers dietary considerations, \nsuch as whether the dish is vegan, gluten-free, or dairy-free. Simply enter a dish \ntype, and discover the perfect recipe tailored to your needs!\n")
    
    offset = 0
    while True:
        query = input("Enter the type of dish you want to find recipes for: ")
        if query.lower() == 'exit':
            print(Fore.GREEN + "\nThank you for using the Recipe Finder. Goodbye!")
            break
        
        while True:
            recipes = find_recipes(query, offset=offset)
            
            if not recipes:
                print(Fore.RED + "\nNo recipes found.")
                break  # Break out of the loop if no recipes are found

            for i, recipe in enumerate(recipes):
                print(f"{offset + i + 1}. {recipe['title']}")

            choice = input("\nEnter the number of the recipe you want more information about or type 'next' to see more recipes: ")
                
            if choice.lower() == 'next':
                offset += 10
            elif choice.isdigit() and int(choice) in range(offset + 1, offset + len(recipes) + 1):
                recipe_id = recipes[int(choice) - offset - 1]['id']
                recipe_info = get_recipe_info(recipe_id)
                
                if recipe_info:
                    title, ready_in_minutes, servings, instructions, ingredients, vegetarian, vegan, gluten_free, dairy_free = recipe_info
                    print(Fore.CYAN + "\nRecipe Details:")
                    print(Fore.CYAN + f"Title: {title}")
                    dietary_considerations = []
                    if vegetarian:
                        dietary_considerations.append("Vegetarian")
                    if vegan:
                        dietary_considerations.append("Vegan")
                    if gluten_free:
                        dietary_considerations.append("Gluten-Free")
                    if dairy_free:
                        dietary_considerations.append("Dairy-Free")
                    
                    if dietary_considerations:
                        print(Fore.CYAN + f"Dietary Considerations: {', '.join(dietary_considerations)}")
            
                    print(Fore.CYAN + f"Ready in {ready_in_minutes} minutes")
                    print(Fore.CYAN + f"Servings: {servings}")
                    print(Fore.CYAN + "Ingredients:")
                    for name, amount, unit in ingredients:
                        print(Fore.CYAN + f"  - {name}: {amount} {unit}")
                    if instructions:
                        print(Fore.CYAN + "\nInstructions:")
                        print(Fore.CYAN + format_instructions(instructions))
                    else:
                        print(Fore.RED + "\nNo instructions available for this recipe.")
                        
                    break  
            else:
                print(Fore.RED + "\nInvalid choice. Please select a valid recipe number or type 'next'.")

        offset = 0
        
        print(Fore.GREEN + "\nType 'exit' if you would like to leave the program.\n")      

if __name__ == "__main__":
    main()