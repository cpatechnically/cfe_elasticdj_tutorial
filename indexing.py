import elasticsearch
from elasticsearch_dsl import Search

ELASTIC_IDX_NAME = "cfe-posts"
ELASTIC_HOST = 'http://localhost:9231'


client = elasticsearch.Elasticsearch()

post_1={
    "id":1,
    "title": "This is awesome",
    "content":"Here is my data bout dj"
}

client.index(index=ELASTIC_IDX_NAME,body=post_1)