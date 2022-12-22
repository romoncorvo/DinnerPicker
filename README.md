# Dinner Picker

#### Video Demo: <https://youtu.be/8qkqzFkOzGc>
#### Live Site: <http://romoncorvo.pythonanywhere.com/login>

#### Description:

The purpose of this app is to help you choose a random dinner recipe. With an account, you can store the recipes you want to use.

#### Tools Used:

- CSS and Bootstrap: Styling.
- Flask: Serving the app.
- HTML: Structure of the pages.
- Javascript: Buttons to add and remove DOM objects.
- Python: Backend logic of randomly picking a recipe.
- SQLite: Store the recipes.

#### Main Files:

#### `app.py:`

The backend code of the app. It configures the flask application, SQL database and routes for GET and POST. It is also responsible for the logic of randomly picking a recipe from the database and serving the pages.

#### `recommendations.db:`

The database has two tables. One for storing the users with hashed passwords and another for storing the recipes.

#### `static/main.js:`

The javascript code to add and remove ingredients and steps in the addRecipe.html page.

#### `templates/addRecipe.html:`

Page where you can add your own recipes to be saved in the database. This is the part I took the longest to complete because I had little experience with bootstrap and the layout was not behaving as I expected.

#### `templates/index.html:`

Main page where you can click a button and get a random recipe. This page served with GET only shows the button and clicking the button routes to this same page by POST, showing the recipe.
