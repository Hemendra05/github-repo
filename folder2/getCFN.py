import boto3, json

session = boto3.session.Session()

cfn = session.client("cloudformation")
s3 = session.client("s3")

cfnStacks = cfn.list_stacks(
    #NextToken = "vovg/sWdmHkwO4f/RIxd3w+s88iS9LeU2ZZkzHQPh0CN/JG3j0icHZmEbY8ip/uejyX5pPhCYiSFDKReE2TEw20aBVGaXXA3QeNxy3Nd2xF2wnGfdKS64bZ4j285MK5vR4reqSfKQzIipaNAJ/FrEZon5iGFA6K70RRidU3WclT4YNHURVQLuOP8ueM45FgC8Mjy9Jc0okrPEppEvB/uf7B1rVIFmDo1aG239qxJVWX27OyiaaOnavyAUtixgnHrv7U1KHJq9Q/ZJBUiSL3B8R1LwLJw2unxmdvvcI4l4UW/0MSwUQSdB7ukmI1C67RxIrF5Jc8LVbEo+GMcAqJ9OSy+WO33veqqs5j8+i2qQ5/uZghTYOwYADJaXEx9S8VkKWuvYddArNRceXqso8yDUOmQu4jo42Jt+fFXFLBV81QUbUT6FGLWJfW/b4U0DWFbf7I8UUiGyCWlAF6s2EmBbCy0ttqtZHwIBsz3wAEfSzK0DAZr1jf2XMcupi+pGv4E+eOjlnv3E03osZyvdOVK64nJHSxC1S+nZKBz5aa6lg811dRzycG42f5HFExUaxPWRE+41htbSLdibkCo0a+vcqCGfLUCKWbQqLeRpLsBzKe5WLin5/5YBp2CA9dcTCTmR9dqpa8LdzUCZm+t8I2Dfgc9Fm2+97Ie2CgyA788N6md7609iCJvF5VtoPG/kdPnKIJQk5FbGkKKJNeTShjLEg==|A2GN0WUJzIJ5Cf6Osh6BqA==|1|02ae361b107efa8ab097af97c930caa69ab614ab49f813ab95958dbd0e0eb86e",    
    #NextToken = "L7pb6ocLQLkUCyRQH0feFCheouYGl+VJ8qW0lpTUvKTijkyjIyWl5u6NYKjXcWmykCH0AklQYx+2PvxCIxdVI0JzYjod4B/VO+taqlDc/P8HNW5rxSbJnZwVTP99ka/xn4VLy9wTTxxheC7oKutGfwYM7/bL22zoaq8JvQ730ZsKDT8MQ8VuO+Ega4TNsIA8617o9pp8g8bQysCGR/PKfnuffK6fLTVRCFNhBK5imuu3oDx2dl+RYySzvdsE4x5Ck/KlxlbnJkhHLHs2CwKRlAx1awVgNEGaCJZ2H0k4yAc/yJRyD6T70Vjnl285fFA+NBIBdBVAZ54CZ4NBjlSXHQA3IYOcNUNjqwQY36BEM2zMMMEPJ+zw2GYKNbTZJXZ0v5JPwkqy+Y9DTD6OdGsBL8wP7zQlPMN0hXAAnNocofa8S77E3yYcH0COMbv6VOVUgCNCg4PaJEO3MSud6SokZHqHLAIjXS5cYGISxvC/YnwO1eQBdV03XI4sS36wacx7Bvd3lSGFFhV9/HRuOsgVNMwADjVsizaZktVFpaVAJgm8fntxbCRAAlIYYVYQgvnp7JOp+uzDTH9xxlbSTwH861njJv5ode56Qpxg7JeDUVJw5GkbjQwhRByIfnbYgJWwQ6aG+WURcAh6kP00CDdqrXGXqnJQ0CG7wiHGfB/aha7SaLgOfaXwrN9zFx8T0qhE|vk/DQeYyguD9vAR56Mxsqg==|1|164d598b4b204668bf6ba12d8186241740094bc051f086f3b33f3216f9d70f51",
    StackStatusFilter=[
        'CREATE_COMPLETE',
        'ROLLBACK_COMPLETE',
        'UPDATE_COMPLETE',
        'UPDATE_ROLLBACK_COMPLETE'
    ]
)

s3Buckets = s3.list_buckets()

print(len(cfnStacks["StackSummaries"]))
print(len(s3Buckets["Buckets"]))


# for i in range(len(cfnStacks["StackSummaries"])):
#     stackName = cfnStacks["StackSummaries"][i]["StackName"]

for j in range(len(s3Buckets["Buckets"])):
    if "myways" in s3Buckets["Buckets"][j]["Name"].lower():
        print(s3Buckets["Buckets"][j]["Name"])


# print(json.dumps(cfnStacks, sort_keys=True, indent = 1, default=str))