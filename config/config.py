import os
import json
from pymongo import MongoClient

MONGO_SERVER = os.environ.get('MONGO_SERVER', 'localhost:27017')
MONGO_DB = os.environ.get('MONGO_DB', 'metis')
MONGO_USER = os.environ.get('MONGO_USER', 'user')
MONGO_PWD = os.environ.get('MONGO_PWD', 'password')
MONGO_AUTHDB = os.environ.get('MONGO_AUTHDB', 'metis')

print(MONGO_SERVER, MONGO_DB, MONGO_PWD)

uri = f"mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_SERVER}/?authSource={MONGO_AUTHDB}&authMechanism=SCRAM-SHA-1"
server = uri
print(server)
mongo = MongoClient(server)


def run_cities():
    f = open("city.json", "r+", encoding="utf-8")
    config_output = f.read()
    config_list = json.loads(config_output)['city']

    mongo_db = mongo[MONGO_DB]
    mongo_db.drop_collection('city')

    for config in config_list:
        config['country_code'] = 'PH'
        mongo_db.city.insert_one(config)


def run_citizenships():
    f = open("citizenship.json", "r+", encoding="utf-8")
    config_output = f.read()
    config_list = json.loads(config_output)['citizenship']

    mongo_db = mongo[MONGO_DB]
    mongo_db.drop_collection('citizenship')

    for config in config_list:
        config.pop('id')
        mongo_db.citizenship.insert_one(config)


def run_countries():
    f = open("country.json", "r+", encoding="utf-8")
    config_output = f.read()
    config_list = json.loads(config_output)['country']

    mongo_db = mongo[MONGO_DB]
    mongo_db.drop_collection('country')

    for config in config_list:
        mongo_db.country.insert_one(config)


def run_job_class():
    f = open("job_class.json", "r+", encoding="utf-8")
    config_output = f.read()
    config_list = json.loads(config_output)['job_class']

    mongo_db = mongo[MONGO_DB]
    mongo_db.drop_collection('job_class')

    for config in config_list:
        mongo_db.job_class.insert_one(config)


def run_provinces():
    f = open("province.json", "r+", encoding="utf-8")
    config_output = f.read()
    config_list = json.loads(config_output)['province']

    mongo_db = mongo[MONGO_DB]
    mongo_db.drop_collection('province')

    for config in config_list:
        config.pop('id')
        config.pop('region_id')
        mongo_db.province.insert_one(config)


def run_religions():
    f = open("religion.json", "r+", encoding="utf-8")
    config_output = f.read()
    config_list = json.loads(config_output)['religion']

    mongo_db = mongo[MONGO_DB]
    mongo_db.drop_collection('religion')

    for config in config_list:
        config.pop('id')
        mongo_db.religion.insert_one(config)


run_cities()
run_citizenships()
run_countries()
run_job_class()
run_provinces()
run_religions()

