
# FinAS-Backend

checkout [here](http://localhost:8000)


## Installation

start server at http://localhost:8000/

```bash
  docker-compose -f docker-compose-dev.yml up -d --build
```

close server at http://localhost:8000/

```bash
  docker-compose -f docker-compose-dev.yml down
```

Running Tests

```bash
  docker-compose -f docker-compose-dev.yml exec api bash Scripts/test_api.sh
```
