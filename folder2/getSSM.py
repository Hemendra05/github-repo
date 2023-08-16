import boto3, json

session = boto3.Session()
ssm = session.client("ssm")

DEVELOPER_NAME = "/devops/dev/server"

developerName = ssm.get_parameter(
    Name=DEVELOPER_NAME, WithDecryption=True
)
NAMES = (
    developerName["Parameter"]["Value"]
)

print(NAMES)