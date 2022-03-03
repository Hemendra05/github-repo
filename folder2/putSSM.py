import fileinput
import boto3, json, fileinput

session = boto3.Session()
ssm = session.client("ssm")

inputValue = fileinput.input(files="developersList.txt")

for line in inputValue:
    print(line)

    response = ssm.put_parameter(
        Name='/devops/dev/servers',
        Value=str(line),
        Type='String',
        Overwrite=True,
    )