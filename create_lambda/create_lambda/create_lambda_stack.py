from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class CreateLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, "HelloHandler",
            runtime = _lambda.Runtime.PYTHON_3_8,
            code = _lambda.Code.from_asset('lambda'),
            handler = "hello.handler",

        )

        
