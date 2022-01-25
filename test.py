from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck


class test(BaseResourceCheck):
    def __init__(self):
        # This is the full description of your check
        description = "test"

        # This is the Unique ID for your check
        id = "CKV_AWS_199"

        # These are the terraform objects supported by this check (ex: aws_iam_policy_document)
        supported_resources = ['aws_lambda_function']

        # Valid CheckCategories are defined in checkov/common/models/enums.py
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=description, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        # Replace this with the custom logic for your check
        if conf.get("VpcConfig",[]):

            isEmpty = conf["VpcConfig"]
            if isEmpty != []:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = test()