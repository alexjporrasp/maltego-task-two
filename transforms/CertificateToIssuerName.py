from maltego_trx import entities
from maltego_trx import transform
import re


class CertificateToIssuerName(transform.DiscoverableTransform):
    """
    Returns the name (CN) of the certificate issuer.
    """

    @classmethod
    def create_entities(cls, request, response):
        # Issuer Name Example:
        # "C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3"
        match = re.match(r".*CN=(.*)", request.getProperty('issuer_name'))
        CN = request.getProperty('issuer_name')
        if match:
            CN = match.group(1)
        response.addEntity(entities.Phrase, CN)
