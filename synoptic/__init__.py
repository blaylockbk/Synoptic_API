## Brian Blaylock
## September 11, 2020

"""
============
Synoptic API
============

Retrieve and plot mesonet data from thousands of stations via the Synoptic Data
Mesonet API: https://developers.synopticdata.com/mesonet/.

Setup
-----
1. Include the ``Synoptic_API`` directory path in your PYTHONPATH. 
    - *or* add ``sys.path.append('/path/to/Synoptic_API/')`` in your script.
1. Obtain an API token and edit the file `synoptic.mytoken.py` with your Synoptic API token.
    - https://developers.synopticdata.com/mesonet/v2/getting-started/

Usage
-----
There are two recommended ways to import these functions.

``` python
# Method 1: Import full module
import synoptic.services as ss
import synoptic.plots as sp
```

``` python
# Method 2: Import individual functions
from synoptic.services import stations_timeseries
```
"""

__author__ = 'Brian Blaylock'
__email__ = 'blaylockbk@gmail.com'
__url__ = 'https://github.com/blaylockbk/Synoptic_API'


# 🙋🏻‍♂️ Thank you for using Synoptic!")
