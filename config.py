 






# import motor.motor_asyncio
import pymongo
# MONGODB_URL = 'mongodb+srv://Kiran123:<Kiran123>@cluster0.tqocdec.mongodb.net/?retryWrites=true&w=majority'

# client =  motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# # connect to database python_db
# database = client.test



client = pymongo.MongoClient("mongodb+srv://Kiran123:Kiran123@cluster0.tqocdec.mongodb.net/?retryWrites=true&w=majority")
database = client["test"]
# # print results
# for i in result:
#     print(i)
 
# from urllib.parse import quote_plus
# username = quote_plus('<Kiran123>')
# password = quote_plus('<Kiran123>')
# cluster = '<Cluster0>'
# authSource = '<authSource>'
# authMechanism = '<authMechanism>'
# uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism
# client = pymongo.MongoClient(uri)
# result = client["<dbName"]["<collName>"].find()
# # print results
# for i in result:
#     print(i)