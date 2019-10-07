# -*- coding: utf-8 -*-

import mongoengine as me
from mongoengine_mate import ExtendedDocument
from mongoengine import connect

client = connect(
    db="nyc_sls_hack",
    host="ds331558.mlab.com",
    port=31558,
    username="admin",
    password="sls_hack_2019",
    alias="nyc_sls_hack",
)


class BaseModel(ExtendedDocument):
    meta = {
        "abstract": True,
    }


class CrimeRecord(BaseModel):
    _id = me.StringField()

    meta = {
        "db_alias": "nyc_sls_hack",
        "collection": "crime_record"
    }
