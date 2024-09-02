# RecipeFinder
Welcome to the Recipe Finder! This Python program allows users to search for delicious recipes based on their preferences. Leveraging the Spoonacular API, the app fetches and displays recipes, along with detailed information such as ingredients, instructions, and dietary considerations (e.g., vegan, gluten-free, dairy-free).

## Features
Search for Recipes: Enter the type of dish you want to find recipes for, and the app will return a list of matching recipes.
View Recipe Details: Select a recipe to view detailed information, including preparation time, servings, ingredients, and step-by-step instructions.
Dietary Considerations: The app highlights whether the recipe is suitable for specific dietary needs such as vegetarian, vegan, gluten-free, or dairy-free.
Pagination: If there are more recipes available than can be displayed at once, you can view additional recipes by typing next.
Error Handling: The app gracefully handles errors, such as invalid user input or when no recipes are found.
## Prerequisites
The following Python libraries:

requests: To make HTTP requests to the Spoonacular API.

re: For regular expression operations.

colorama: To add color to the terminal output.

## Installation
Clone the Repository:

```bash
git clone https://github.com/thedonnyvan/RecipeFinder.git
cd recipeFinder
```

## Install Dependencies: Install the required Python libraries using pip:
```bash
pip install requests 
pip install colorama
```

## Set Up the API Key:
Sign up on Spoonacular to obtain an API key.
Replace the placeholder api variable in the code with your actual Spoonacular API key.
Usage

## Run the Program:

```bash
python RecipeFinder.py
```
## Using the App:

Search: Type in a dish you’re interested in (e.g., "pasta", "iced coffee", "salad").
Navigate: Type the number corresponding to the recipe for more details, or type next to view more recipes.
Exit: Type exit at any time to leave the program.

## EXAMPLE
Welcome to the Recipe Finder! This program allows you to search for delicious 
recipes based on the type of dish you want to make. Not only does it provide detailed 
instructions and ingredients, but it also offers dietary considerations, 
such as whether the dish is vegan, gluten-free, or dairy-free. Simply enter a dish 
type, and discover the perfect recipe tailored to your needs!

Enter the type of dish you want to find recipes for: iced coffee

1. Classic Iced Coffee
2. Vanilla Iced Coffee
3. Iced Coffee with Coconut Milk

Enter the number of the recipe you want more information about or type 'next' to see more recipes: 1

Recipe Details:
Title: Classic Iced Coffee
Dietary Considerations: Vegan, Dairy-Free
Ready in 10 minutes
Servings: 1
Ingredients:
  - Coffee: 1 cup
  - Ice cubes: 1 cup
  - Almond milk: 1/2 cup
  - Sugar: to taste

Instructions:
1. Brew a cup of coffee and let it cool.
2. Fill a glass with ice cubes.
3. Pour the coffee over the ice.
4. Add almond milk and sugar to taste.
5. Stir well and enjoy.

Type 'exit' if you would like to leave the program.
