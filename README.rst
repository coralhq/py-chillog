==========
py-chillog
==========

Python logger library for SFE


How To Install
==============

- Download / clone this repo
- Run ``make install``


How To Test
===========

- Run ``make test``


How To Use
==========

- Import ``from chillog.logger import Chillog``
- Initialize this library with ``logger = Chillog()``
- Use Chillog logger using ``logger`` (object from previous step)

There are 5 logger you can use:

- ``debug``
- ``info``
- ``warning``
- ``alert``
- ``critical``

e.g. : ``logger.info('log message')``

You can also pass additional data to logger, by kwargs param or just pass whole dict.

e.g. :

- Pass kwargs params --> ``logger.info('log message', key='value')``
- Pass dict --> ``logger.info('log message', **{'key': 'value'})``
