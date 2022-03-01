## Prerequisites

- Install Python 3
- Install [Docker](https://www.docker.com/community-edition#/download)
- Install [Docker Compose](https://docs.docker.com/compose/install/)

## Quick Start

To begin working with this project locally in dev mode you can simply:

```bash
# Start running these commands in this repo's directory

cd c:/Users/schristian/Desktop/test/SIO_SERVER/server.py # Location of server file

python3 server.py  # This command will start server
```

## What services run

```
       localhost:5000 - python server

http://0.0.0.0:5000 - Server running and waitting for client servers on development
pygateway - Server running and waitting for client servers on AWS

sudo service pygateway start - Start service
sudo service pygateway stop - Stop service
sudo service pygateway restart - Restart service
sudo service pygateway status - check status of service
```


### Backend

- Install `python3`, `virtualenv`, `virtualenv-wrapper`
- Create a `.env` file in the directory where the repo was cloned
- TODO: Other setup steps?

## Dependencies 

- pip install python-socketio

No need to install just for testing purpose if need it.
- pip install "python-socketio[client]"
- pip install "python-socketio[asyncio_client]"


## Deploying

Before deploying you might need to:

- Sign in to the aws cli
- Folder name Schristian will contain socketio server.py file

### Deploying Backend


"# schristian" 
"# schristian" 
