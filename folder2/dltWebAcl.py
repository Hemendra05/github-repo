import json, boto3, os

session = boto3.Session()
waf = session.client("wafv2")
api = session.client("apigateway")


restApis = api.get_rest_apis(limit=500)

count=0

for item in range(0, len(restApis["items"])):

    count+=1

    apiId = restApis["items"][item]["id"]

    apiStages = api.get_stages(
        restApiId=apiId,
    )

    apiStage = apiStages["item"][0]["stageName"]

    apiARN = f"arn:aws:apigateway:ap-south-1::/restapis/{apiId}/stages/{apiStage}"

    print(f"Removing...: {apiId}")

    os.system(f"aws wafv2 disassociate-web-acl --resource-arn {apiARN}")

    print(f"{count}-Removed: {apiId}")

# waf.disassociate_web_acl(
#         # WebACLArn="arn:aws:wafv2:ap-south-1:872436821098:regional/webacl/ApiWafAcl/cd0778bb-e28b-46b0-af39-0bc88e5d74dd",
#         ResourceArn="arn:aws:apigateway:ap-south-1::/restapis/w59cayse45/stages/prod",
#     )
