#!/usr/bin/env python3

import aws_cdk as cdk

from learn_aws_cdk.learn_aws_cdk_stack import LearnAwsCdkStack


app = cdk.App()
LearnAwsCdkStack(app, "LearnAwsCdkStack")

app.synth()
