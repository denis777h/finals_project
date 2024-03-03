from django.apps import AppConfig
import redis

class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
    
    
main_redis = redis.Redis(
    host='redis-12060.c302.asia-northeast1-1.gce.cloud.redislabs.com',
    port='12060',
    password='zbYhs0G9171KwzEipzu6mczurksgCKY9',

)

