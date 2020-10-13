from maltego_trx import transform


class DomainToCertificates(transform.DiscoverableTransform):
    """
    SSL Certificates that match the domain name according to crt.sh.
    """

    @classmethod
    def create_entities(cls, request, response):
        raise NotImplementedError()