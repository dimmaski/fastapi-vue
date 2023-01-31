## About
This repo goes hand-in-hand with the following blog post
- [https://dimmaski.com/serve-vue-fastapi/](https://dimmaski.com/serve-vue-fastapi/)
## Serve Backend locally

```sh
cd api

# setup virtualenv
virtualenv -p python3.10 -v venv
pip install -r requirements.txt

# serve
uvicorn main:app --reload
```

## Serve Frontend locally
```sh
cd ui

# install dependencies
npm run install

# serve
npm run watch
```

## Run FE and BE in hot-reload mode
```
npm run watch --prefix ui & uvicorn api/main:app --reload && fg
```
