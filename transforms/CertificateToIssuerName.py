from maltego_trx import transform


class CertificateToIssuerName(transform.DiscoverableTransform):
    """
    Returns the name (CN) of the certificate issuer as a maltego.Phrase entity.
    """

    @classmethod
    def create_entities(cls, request, response):
        raise NotImplementedError()