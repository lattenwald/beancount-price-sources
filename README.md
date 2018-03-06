Additional importers for beancount plaintext accounting

Installation
------------
python setup.py install

CryptoCompare price source
------------------------

ETH to USD:

	bean-price -e 'USD:lattenwaldsources.cryptocompare/ETH:USD'


WavesPlatform price source
------------------------

CryptoBazar (CBT) to BTC:

	bean-price --no-cache -v -e "BTC:lattenwaldsources.waves/HfTchexAmETtGoPCU1V72t6WNgPPoEsLjBTpeeBzC46L:BTC:BTC"

Most likely you will beed Waves Platform's currency ID, there `HfT...` is ID for CBT.
