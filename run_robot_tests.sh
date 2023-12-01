#!/bin/bash

# käynnistetään Flask-palvelin taustalle
cd src
ls
poetry run flask run &
cd ..
ls

echo "Checking server status..."
# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w '%{http_code}' localhost:5000/)" != "200" ]];
  do sleep 1;
done

# suoritetaan testit
poetry run robot src/backend/tests

status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status
