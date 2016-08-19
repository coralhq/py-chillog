==========
SFE Logger
==========

Python logger library for SFE


How To Install
==============

- Download / clone this repo
- Run ``python setup.py install``


How To Use
==========

- Import ``from skylog.logger import skylog_init``
- Initialize this library with ``skylog_init(APP_NAME)``
- Use skylog logger --> ``from skylog import logger``

There are 4 logger you can use:

- ``info``
- ``warning``
- ``alert``
- ``critical``

e.g. : ``logger.info('log message')``

You can also pass additional data to logger, by kwargs param or just pass whole dict.

e.g. :

- Pass kwargs params --> ``logger.info('log message', key='value')``
- Pass dict --> ``logger.info('log message', **{'key': 'value'})``
