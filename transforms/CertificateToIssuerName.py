from maltego_trx import entities
from maltego_trx import transform
import re


class CertificateToIssuerName(transform.DiscoverableTransform):
    """
    Returns the name (CN) of the certificate issuer.
    """

    @classmethod
    def create_entities(cls, request, response):
        response.addEntity(entities.Phrase, request.getProperty('issuer_name'))
