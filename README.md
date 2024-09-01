# frittenburger.de


## Installation
```
pip install -r D:\Stuff\git\DIRK\frittenburger.de\requirements.txt
```

## Usage

```
uvicorn main:app --reload
```

## Usage with docker compose

```
docker network create -d bridge reverse-proxy
```

```
docker compose up --build
```

