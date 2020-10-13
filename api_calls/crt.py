import requests
import json


def fetch_certificates_from_domain(domain_name):
    http_response = requests.get(
        'https://crt.sh/',
        params = {
            'CN': domain_name,
            'output': 'json'
        }
    )
    if not http_response.ok:
        raise ConnectionError(
            'Status code: {}'.format(http_response.status_code)
        )
    return json.loads(http_response.text)