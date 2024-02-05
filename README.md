---
author: Mohammad Esmaeili
title: Medis (PyInMemStore)
---

# Medis: another in memory datastore

-   a simple in memory store like redis
-   use redis-cli to connect
-   includes data persistense using pickle

## Requirements  (Prerequisites)
* Python 3.11 and up 
* pytest

## development setup guide:

-   setup virtual environment
```bash
 python3.11 -m venv venv && source venv/bin/activate
```

- install dependencies
```bash
pip install -r requirements.txt
```
- run server 
```bash
sudo chmod +x medis.sh
./medis.sh
```

- connect using redis cli
```bash
redis-cli -p 6689
```

## Running the tests
we are using pytest as testing library so easily run pytest to run tests
```bash 
    pytest
```


## How to Contribute
Mention how anyone can contribute to make this project more productive or fix bugs in it.  

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate. If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

Steps to contribute:
1. Fork this repository (link to your repository)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request



## OOP Design patterns:

- Command Pattern for redis commands
- Thread safe Singleton Pattern for db store
- mono (single) observer for db persistors