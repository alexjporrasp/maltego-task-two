# maltego-task-two

Maltego transforms examples.

## Requirements

1. Install Python 3 with Pip.
2. Install virtualenv.
```
python -m pip install --user virtualenv
```
3. Create virualenv
```
python -m virtualenv env
```
4. Activate environment
```
# Windows
..\env\Scripts\activate

# Unix
source ../env/bin/activate
```

5. Install maltego-trx
```
(env) pip install maltego-trx
```

6. Add local transforms to Maltego [like this.](https://docs.maltego.com/support/solutions/articles/15000017605-writing-local-transforms-in-python)

## Transforms

### DomainToCertificates
SSL Certificates that match the domain name according to crt.sh.

### CertificateToIssuerName
Returns the name (CN) of the certificate issuer.

## Custom Entities
Add custom entites to Maltego [like this.](https://docs.maltego.com/support/solutions/articles/15000010462-create-new-entity#additional-properties-0-3)

### alexporras.Certificate
Describes an SSL Certificate as a node in Maltego.