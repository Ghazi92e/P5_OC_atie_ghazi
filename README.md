# [P5_OC](https://openclassrooms.com/fr/paths/68/projects/157/assignment)
![Image of Openfoodfact](https://stockagehelloassoprod.blob.core.windows.net/images/logos/open-food-facts_sb200x200_bb0x0x200x200.png)

### Use public data from OpenFoodFacts

The startup Pur Beurre works well knows French eating habits. Their restaurant, Ratatouille, is enjoying growing success and attracting more and more visitors to the Butte de Montmartre.

The team noticed that their users were keen on making a change in their diet but weren't sure where to start. Replace Nutella with a hazelnut paste, yes, but which one ? And in which store to buy it ? Their idea is therefore to create a program that would interact with the Open Food Facts database to retrieve the foods, compare them and offer the user a healthier substitute for the food they want.

### Specifications
#### Description of the user journey
The user is on the terminal. The latter displays the following choices:

1. What food do you want to replace ?
2. Find my substitute foods.

The user selects 1. The program asks the following questions to the user and the user selects the answers:

- Select the category [Several propositions associated with a number. The user enters the corresponding number and presses enter]
- Select the food. [Several propositions associated with a number. The user enters the number corresponding to the chosen food and presses enter]
- The program offers a substitute, its description, where to store or buy it (if applicable) and a link to the Open Food Facts page for that food.
- The user then has the possibility of saving the result in the database.

### Installation
1. Install MYSQL
2. Create a database with MYSQL
3. Create a .env file
```
touch .env
```
4. Add and configure the environment variables in file .env
```
DB_USER="", DB_NAME="", DB_PASSWORD="", DB_HOST=""
```
5. Run the application with the main.py file
```
python main.py
```
### Documentation project
Class | Method | Description 
------------ | ------------- | -------------
 DB | selectrequest             | select a request SQL
 DB | selectsubproductorproduct | select a subproduct and product
 DB | selectiduser              | select a user
 DB | insertsubproduct          | insert into DB a substitute product 
 DB | insertuser                | create a user
 DB | checkuserdb               | check if a user already exist in database
 DB | cursordb                  | create a cursor 
 DB | fetchall                  | display data DB
 DB | commit                    | create a commit
 DBsetup | createtables         | create tables for DB
 DBsetup | datacategory         | insert products category
 DBsetup | getapidata           | get API data
 DBsetup | filterdata           | filter API products without data
 DBsetup | insertproducts       | insert products into DB
 DBsetup | insertorupdateproducts | insert or update DB products
 DBsetup | updatedata           | update DB products
 DBshow  | showselectrequest    | display requests SQL
 DBshow  | showproductrequest   | display DB products 
 Menu    | home_menu1           | manage the first part of the menu
 Menu    | home_menu2           | manage the second part of the menu
 Menu    | check_userapp        | check if the user has an account
 Initapp | mainapp              | manage the main application