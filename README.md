# frittenburger.de


## Installation
```
pip install -r requirements.txt
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

