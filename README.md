# rfid-products-python
Subscriber MQTT e API Server do projeto

# Instalação do Serviço

## Pré-requisitos

* python3
* git

## Serviço

```shell
git clone https://github.com/misaelssantos/rfid-products-python.git

pip3 install -r requirements.txt
```

## SQLite

```shell
sudo apt-get update
sudo apt-get install sqlite3

cd db
python DB_Ini.py
```

## Iniciando o subscriber

```
# Preencher arquivo .env com MQTT_BROKER, MQTT_TOKEN e MQTT_PORT

chmod +x run.sh
./run.sh
```

## Iniciando a API

```shell
python3 main.py
```


# Testes MQTT

```shell
mosquitto_sub -h "industrial.api.ubidots.com" -t "/v1.6/devices/esp32/#" -u "TOKKKEENNNN" -p 1883 -q 1
```

# Referências

## DAO
http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte2.html

## Config
https://iotbytes.wordpress.com/sqlite-db-on-raspberry-pi/
http://zetcode.com/db/sqlitepythontutorial/

## CORS

https://pypi.org/project/Sanic-Cors/


