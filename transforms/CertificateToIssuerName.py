from maltego_trx import entities
from maltego_trx import transform
import re


class CertificateToIssuerName(transform.DiscoverableTransform):
    """
    Returns the name (CN) of the certificate issuer.
    """

    @classmethod
    def create_entities(cls, request, response):
        issuer_dn = request.getProperty('issuer_dn')
        match = re.match('.*CN=(.*)', issuer_dn)
        main_value = issuer_dn if not match else match.group(1)
        entity = response.addEntity(entities.Phrase, main_value)
        entity.addProperty(
            fieldName='issuer_dn',
            displayName='Issuer DN',
            value=issuer_dn
        )
        entity.addProperty(
            fieldName='subject_cn',
            displayName='Subject CN',
            value=request.getProperty('subject_name')
        )
