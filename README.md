# flask-app

## Developing locally
```bash
python3 -m venv venv
venv/bin/pip install -r requirements.txt
flask run
```

## Running in Docker locally
```bash
docker build -t public.ecr.aws/flynshue/flask-app:0.0.1 .

docker run --name flask-app --rm -p 5000:5000 public.ecr.aws/flynshue/flask-app:0.0.1 --env APP_NAME='FOO BAR'
```