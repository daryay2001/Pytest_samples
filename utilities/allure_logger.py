import json
import allure
from requests import Response


def log_json(data: dict, name: str = 'json_data'):
    allure.attach(json.dumps(data, indent=3), name=name, attachment_type=allure.attachment_type.JSON)


def log_response(resp: Response):
    data = dict()
    data['URL'] = resp.url
    data['HEADERS'] = dict(resp.headers)
    data['ELAPSED'] = resp.elapsed.seconds
    data['STATUS_CODE'] = resp.status_code
    data['RESPONSE_BODY'] = resp.json()
    _name = f"({data['STATUS_CODE']}) - {data['URL']}"
    allure.attach(json.dumps(data, indent=3), name=_name, attachment_type=allure.attachment_type.JSON)
