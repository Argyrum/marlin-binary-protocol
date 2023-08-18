Provides implementation of the Marlin Binary Transfer Protocol Mark II as described here:
<https://github.com/MarlinFirmware/Marlin/pull/14817>

Requires:

* Marlin firmware from 2.0.x bugfix branch: <https://github.com/MarlinFirmware/Marlin/tree/bugfix-2.0.x>
* BINARY_FILE_TRANSFER feature enabled in Configuration_adv.h: <https://github.com/MarlinFirmware/Marlin/blob/8b637e436c775c7566820eb1defd00bb209d06b4/Marlin/Configuration_adv.h#L1198>

Usage:

* python -m binproto2.transfer [-h] [-p PORT] [-b BAUD] [-d BLOCKSIZE] [-r] [-t] [-c] [-x TIMEOUT] source [destination]
* python -m binproto2.transfer [-h] [-p PORT] [-c] source

As the comments in the PR state, the protocol is a work in progress and will change.

This code is essentially the same as the code provided by user p3p on that pull request.

Look at the provided transfer utility, transfer.py, for example usage.
