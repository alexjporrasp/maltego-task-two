from maltego_trx import maltego

class Certificate(maltego.MaltegoEntity):
    """
    Describes an SSL Certificate as a node in Maltego.
    """

    def __init__(self, cert_id, subject_name,
                    issuer_name, issuer_id, expiry_date):
        if not cert_id:
            raise ValueError('Certificate ID is required.')
        super().__init__('alexporras.Certificate', cert_id)
        self.addProperty(
            fieldName='certificate_id',
            displayName='Certificate ID',
            value=cert_id
        )
        self.addProperty(
            fieldName='subject_name',
            displayName='Subject Name',
            value=subject_name
        )
        self.addProperty(
            fieldName='issuer_name',
            displayName='Issuer Name',
            value=issuer_name
        )
        self.addProperty(
            fieldName='issuer_id',
            displayName='Issuer ID',
            value=issuer_id
        )
        self.addProperty(
            fieldName='expiry_date',
            displayName='Expiry Date',
            value=expiry_date
        )
