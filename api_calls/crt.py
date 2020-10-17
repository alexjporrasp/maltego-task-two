import requests
import json
import config


def fetch_certificates_from_domain(domain_name: str) -> dict:
    http_response = requests.get(
        config.crt_endpoint_url(),
        params = {
            'CN': domain_name,
            'output': 'json'
        }
    )

    if not http_response.ok:
        raise ConnectionError(
            'Status code: {}'.format(http_response.status_code)
        )

    if not http_response.headers.get('Content-Type') == 'application/json':
        return []
    return json.loads(http_response.text)