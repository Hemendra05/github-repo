from aws_cdk import (
    Stack,
    aws_stepfunctions as stepfunctions,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_s3_notifications as s3_notify,
    aws_s3 as s3,
    aws_dynamodb as dynamodb
)
from constructs import Construct
from aws_cdk.aws_lambda_event_sources import S3EventSource, DynamoEventSource

class CdkSfnStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        layer_arn = "arn:aws:lambda:ap-south-1:872436821098:layer:ApLrNm:2"

        fn = lambda_.Function(self, "MyFunc",
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda/"),
        )

        fn.add_layers(lambda_.LayerVersion.from_layer_version_arn(self, "importedLayer", layer_arn))

        bucket = s3.Bucket.from_bucket_name(self, "Bucket", "codepipeline-anchovy")

        api = apigateway.RestApi(self, "widgets-api",
            rest_api_name="Widget Service",
            description="This service serves widgets.")

        get_widgets_integration = apigateway.LambdaIntegration(fn,
            request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_widgets_integration)