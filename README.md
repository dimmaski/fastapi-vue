
## Serve Backend locally

```sh
cd api

# setup virtualenv
virtualenv -p python3.10 -v venv
pip install -r requirements.txt

# serve
uvicorn main:app --reload
```

## Serve FrontEnd locally
```sh
cd ui

# install dependencies
npm run install

# serve
npm run watch
```
