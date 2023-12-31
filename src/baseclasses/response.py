from src.enums.global_enums import GlobalErrorMessages
from collections import defaultdict

class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validateTotalSchema(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)
        return self
    
    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self
    
    def assert_operation_code(self, operation_code):
        assert operation_code in self.response_json['responses'].keys(), self
        # assert operation_code in self.response_json['responses'].keys(), "\n Код " + operation_code + " отсутствует в ответе"
    
    def __str__(self):
        return \
        f"\nStatus code: {self.response_status} \n" \
        f"Requested URL: {self.response.url} \n" \
        f"Requested body: {self.response_json}"

    
   