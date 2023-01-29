
## Serve Backend locally

```sh
cd api
virtualenv -p python3.10 -v venv
pip install -r requirements.txt
uvicorn main:app --reload
```

## Serve FrontEnd locally
```sh
cd ui
npm run watch
```
