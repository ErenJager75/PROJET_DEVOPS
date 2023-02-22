import requests
import pymongo
from datetime import datetime
import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "448b62f2e18a30dbd789c8ec56f3724a"

# Make API call to get profile information for Apple Inc.
response = requests.get("https://financialmodelingprep.com/api/v3/profile/AAPL", params={"apikey": api_key})
# Extract the stock price and rating from the response
data1 = response.json()


response = requests.get("https://financialmodelingprep.com/api/v3/rating/AAPL", params={"apikey": api_key})
# Extract the stock price and rating from the response
data2 = response.json()



print(data1)

print("-------------------------------")

print(data2)

"""
data_dict = {
    "rating": {
        "score": data2[0]["ratingScore"],
        "recommendation": data2[0]["ratingRecommendation"]
    },
    "profile": {
        "companyName": data1[0]["companyName"],
        "sector": data1[0]["sector"],
        "industry": data1[0]["industry"],
        "website": data1[0]["website"],
        "description": data1[0]["description"],
        "ceo": data1[0]["ceo"],
        "mktCap": data1[0]["mktCap"],
        "lastDiv": data1[0]["lastDiv"],
        "price": data1[0]["price"],
        "changes": data1[0]["changes"],
        "exchange": data1[0]["exchange"],
        "country": data1[0]["country"]
    },
    "timestamp": datetime.now()
}
"""
data_dict2={"pro":data1,"rating":data2,"time":datetime.now()}

print('--------------------------')
#print(data_dict)
print('--------------------------')
print(data_dict2)



# Define the MongoDB connection string and database name
mongo_uri = 'mongodb://localhost:27017/'
db_name = 'test_db'

# Connect to the MongoDB server
client = pymongo.MongoClient(mongo_uri)

# Select the database and collection
db = client[db_name]
collection = db['test_collection']


result = collection.insert_one(data_dict2)

# Print the ID of the inserted document
print('Inserted document ID:', result.inserted_id)


