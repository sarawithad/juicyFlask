import requests
from flask import Flask , render_template, request, url_for
import config

app = Flask(__name__)

juicyData = list()


def getJuicyData():

    appKey = config.appKey
    appId = config.appId

    request1 = requests.get('https://api.nutritionix.com/v1_1/search/?brand_id=51db37d0176fe9790a899db2&results=0%3A50&fields=*&appId=' + appId +'&appKey=' + appKey)
    request1 = request1.json()
    juicyData.append(request1)

    request2 = requests.get('https://api.nutritionix.com/v1_1/search/?brand_id=51db37d0176fe9790a899db2&results=51%3A100&fields=*&appId=' + appId +'&appKey=' + appKey)
    request2 = request2.json()
    juicyData.append(request2)

    request3 = requests.get('https://api.nutritionix.com/v1_1/search/?brand_id=51db37d0176fe9790a899db2&results=101%3A150&fields=*&appId=' + appId +'&appKey=' + appKey)
    request3 = request3.json()
    juicyData.append(request3)

    request4 = requests.get('https://api.nutritionix.com/v1_1/search/?brand_id=51db37d0176fe9790a899db2&results=151%3A200&fields=*&appId=' + appId +'&appKey=' + appKey)
    request4 = request4.json()
    juicyData.append(request4)


@app.route('/juicyproducts', methods=['GET','POST'])
def getProductCount():

    getJuicyData()

    product_count = juicyData[0]['total_hits']

    return render_template('juicyproducts.html', products=product_count)


@app.route('/juicycalories', methods=['GET', 'POST'])
def countAvgCalories():

    getJuicyData()

    results = juicyData[0]['hits']

    for item in results:
        calories_per_oz = list()
        avg_calories =  list()

        if item['fields']['nf_serving_size_unit'] == "fl oz":
            calories_per_oz.append(item['fields']['nf_calories'] / item['fields']['nf_serving_size_qty'])
            avg_calories = (sum(calories_per_oz)) / (len(calories_per_oz))

    return render_template('juicycalories.html', calories=avg_calories)


# @app.route('/juicyingredients')
# def indexIngredients():

#     getJuicyData()

#     results = juicyData[0]['hits']

#     ingredient_index = dict()

#     unique_ingredients = list()
#     product_list = list()


#     for item in results:
#         if item['fields']['nf_ingredient_statement'] != None:
#             unique_ingredients.append(item['fields']['nf_ingredient_statement'])
#     # print('unique_ingredients: ', unique_ingredients)
    
#     for ingredients in unique_ingredients:
#         ingredient = ingredients[0].split(',')
#         unique_ingredients = set(unique_ingredients)

#         print (unique_ingredients)


#     for ingredients in unique_ingredients:
#         if item['nf_ingredient_statement'] in results == ingredients:



#     # for item in results:
#     #     product_list.append(item['fields']['item_name'])
#     # print('product_list: ', product_list)


# #     for item in results:
# #         currentItem = item[0]
# #         for ingredient in unique_ingredients:
# #             currentIngredient = ingredient[0]
# #             for product in product_list:
# #                 currentProduct = product[0]
# #                 (if currentIngredient IS IN currentItem MAKE currentIngredient key and currentItem['fields']['item_name'] value for key)



    # for item in results:
    #     ingredients = item['fields']['nf_ingredient_statement']
    #     specific_ingredient = unique_ingredients[0]

    #     try:
    #         ingredient_index[ingredients].append(specific_ingredient)
    #     except KeyError:
    #         ingredient_index[ingredients] = list()
    #         ingredient_index[ingredients].append(specific_ingredient)


    # for item in results:
    #     product = item['fields']['item_name']
    #     specific_product = product_list[0]

    #     try:
    #         ingredient_index[product].append(specific_product)
    #     except KeyError:
    #         ingredient_index[product] = list()
    #         ingredient_index[product].append(specific_product)

# print('ingredient_index: ', ingredient_index)


    # return render_template('juicyingredients.html', ingredients=ingredient_index)





@app.route('/')
def index():
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)