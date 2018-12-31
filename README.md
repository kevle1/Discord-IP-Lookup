# Discord IP Info Bot
Checks for messages sent to Discord server containing an IP and looks up according information. Sending embed with details to channel message sent. 

Requires [IP Info Python Library](https://github.com/ipinfo/python). Install with `pip install ipinfo`
Requires [IP Info Account](http://ipinfo.io) for API key, found on dashboard. 1000 queries per day with free account. 

Known Issues: Exceptions thrown when embed requires info that IP lookup does not return. Exception not caught, program continues running for now. 