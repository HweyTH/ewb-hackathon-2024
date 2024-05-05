import os
import openai
import json
from openai import OpenAI
from dotenv import load_dotenv
    
load_dotenv()
    
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

print(os.environ.get("OPENAI_API_KEY"))

# Set up OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Sample function to recommend recipes based on ingredients
def recommend_recipes(ingredients):
    # Prepare query for OpenAI API
    query = f"Recommend recipes with {', '.join(ingredients)}."

    # Call OpenAI API to get recipe recommendations
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": query}
            ]
    )

    # Extract and return recommended recipes from API response
    return response.choices[0].message.content

# obtain recipes from ingredients
ingredients = ["chicken", "garlic", "lemon", "parsley"]
recommended_recipes = recommend_recipes(ingredients)

# output the recommendations to json file
data = json.loads(recommended_recipes)  # Convert the response to JSON

# Store the JSON data in a file
with open("recommend.json", "w") as file:
    json.dump(data, file)

# report the recipes
print(recommended_recipes)
