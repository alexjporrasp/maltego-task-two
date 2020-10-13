from api_calls import crt
from custom_entities import custom_entities
from maltego_trx import transform
import re

class DomainToCertificates(transform.DiscoverableTransform):
    """
    SSL Certificates that match the domain name according to crt.sh.
    """

    @classmethod
    def create_entities(cls, request, response):
        try:
            api_response = crt.fetch_certificates_from_domain(request.Value)

            for certificate in api_response:
                issuer_name = certificate.get('issuer_name', '')
                match = re.match(r".*CN=(.*)", issuer_name)
                if match:
                    issuer_name = match.group(1)
                response.entities.append(
                    custom_entities.Certificate(
                        certificate.get('id', ''),
                        certificate.get('name_value', ''),
                        issuer_name,
                        certificate.get('issuer_ca_id', ''),
                        certificate.get('not_after', '')
                    )
                )
        except ConnectionError as e:
            response.addUIMessage(str(e))