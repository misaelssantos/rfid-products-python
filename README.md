# rfid-products-python
Subscriber MQTT e API Server do projeto

# Teste MQTT

```shell
mosquitto_sub -h "industrial.api.ubidots.com" -t "/v1.6/devices/esp32/ovo" -u "TOKKKEENNNN" -p 1883 -q 1
```

# SQLite

```shell
sudo apt-get update
sudo apt-get install sqlite3

cd db
python DB_Ini.py
```

## DAO
http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte2.html

## Config
https://iotbytes.wordpress.com/sqlite-db-on-raspberry-pi/
http://zetcode.com/db/sqlitepythontutorial/


