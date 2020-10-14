import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('prod.conf')

def fetch_certificates_from_domain(domain_name: str) -> dict:
    http_response = requests.get(
        config.get('crt', 'endpoint_url'),
        params = {
            'CN': domain_name,
            'output': 'json'
        }
    )
    if not http_response.ok:
        raise ConnectionError(
            'Status code: {}'.format(http_response.status_code)
        )
    content_type = http_response.headers.get('Content-Type')
    if not content_type == 'application/json':
        raise ValueError(
            'Expected JSON body. Received: {}'.format(content_type)
        )
    return json.loads(http_response.text)