# import os

# def handler(event, context):
#     # os.system("pip install boto3")
#     return { 
#         "statusCode": 200,
#         "body": "Hello World!!!!!!!!!"
#     }


import requests

count = 0

while True:
    req = requests.get('https://0lhl9fhb61.execute-api.ap-south-1.amazonaws.com/prod')
    count+=1
    if req.status_code == 200:
        continue
    else:
        print(req.status_code)
        break

print(count)

