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

Using it in your .beancount file
------------------------

    2017-07-06 commodity CBT
      price: "USD:lattenwaldsources.waves/HfTchexAmETtGoPCU1V72t6WNgPPoEsLjBTpeeBzC46L:Ft8X1v1LTa1ABafufpaCWyVj8KkaxUWE6xBhW6sNFJck:USD EUR:lattenwaldsources.waves/HfTchexAmETtGoPCU1V72t6WNgPPoEsLjBTpeeBzC46L:Gtb1WRznfchDnTh37ezoDTJ4wcoKaRsKqKjJjy7nm2zU:EUR BTC:lattenwaldsources.waves/HfTchexAmETtGoPCU1V72t6WNgPPoEsLjBTpeeBzC46L:474jTeYx2r2Va35794tCScAXWJG9hU2HcgxzMowaZUnu:BTC ETH:lattenwaldsources.waves/HfTchexAmETtGoPCU1V72t6WNgPPoEsLjBTpeeBzC46L:8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS:ETH"
