## How to run
```
docker-compose run --rm vendors
docker-compose up -d server
```

Server will run on port `5000` and any changes to ./src/api-sample.py will automatically be applied with no need to re-run the server

## Sample request
`GET` `http://localhost:5000/reports/123/sent-to`

## Response
```
{
  "sent-to": [
    {
      "email": "isadora@gmail.com"
    }
  ]
}
```
