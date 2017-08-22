A Juicy Project

The Nutritionix API contains nutritional information for a wide variety of food products. Use the Python Flask package to satisfy the following requirements:
1) Return the total number of Juicy Juice products in JSON format.
2) Return average calories per fluid ounce for all Juicy Juice products in JSON format.
3) Create an index from all unique Juicy Juice ingredients to the products that contain them (e.g., the ingredient "mango puree" is in Tropical Mango Juice, Mango Blast, Banana Mango Punch). The data here is dirty; the final results don’t have to be perfect.
4) Build a simple web page to display the results of questions 1-3 and host it on Heroku (https://www.heroku.com/).  Include an exported jpg/png visualization of the Nutritionix data that shows something interesting about the data using a  visualization tool of your choice (an Excel chart is acceptable).  Make sure to include a brief explanation of the visualization.

For example the following GET request will return the first 50 results for Juicy Juice products (brand_id = 51db37d0176fe9790a899db2):

https://api.nutritionix.com/v1_1/search/?brand_id=51db37d0176fe9790a899db2&results=0%3A50&fields=*&appId=[YOURAPPID]&appKey=[YOURAPPKEY]

You will need to visit the Nutritionix website (https://developer.nutritionix.com) in order to obtain your own APPID and APPKEY.

Submit your Heroku site and a Github public repository link with your code for the project to mike@juiceanalytics.com.