from maltego_trx import maltego

class Certificate(maltego.MaltegoEntity):
    """
    Describes an SSL Certificate as a node in Maltego.
    """

    def __init__(self, certificate: dict):
        if not 'name_value' in certificate:
            raise ValueError('Subject CN (name_value) is required.')

        super().__init__(
            'alexporras.Certificate', certificate.get('name_value'))
        self.addProperty(
            fieldName='certificate_id',
            displayName='Certificate ID',
            matchingRule='strict',
            value=certificate.get('id', '')
        )
        self.addProperty(
            fieldName='subject_name',
            displayName='Subject Name',
            value=certificate.get('name_value')
        )
        self.addProperty(
            fieldName='issuer_dn',
            displayName='Issuer DN',
            value=certificate.get('issuer_name', '')
        )
        self.addProperty(
            fieldName='issuer_id',
            displayName='Issuer ID',
            value=certificate.get('issuer_ca_id', '')
        )
        self.addProperty(
            fieldName='expiry_date',
            displayName='Expiry Date',
            value=certificate.get('not_after', '')
        )
