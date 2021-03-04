from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import vk
import random

session = vk.Session(access_token='e6b774fe0f96b2182282931e37815818a0e3347d073f8eebca1a077809305907cab80b334d42e318b61f7')
vk_api = vk.API(session)
@csrf_exempt
def index(request):
    body = json.loads(request.body)
    print(body)
    if body["type"] == 'message_new':
        user_id = body["object"]["message"]["from_id"]
        if body["object"]["message"]["text"]!='':
            messages = "no u, " + body["object"]["message"]["text"]
            vk_api.messages.send(user_id=user_id, message=messages, random_id=random.randint(1,5000000000000000000000), v=5.103)
    return HttpResponse('ok')

@csrf_exempt
def init(request):
    body = json.loads(request.body)
    if body == { "type": "confirmation", "group_id": 196551450 }:
        return HttpResponse("94f39373")
        
    
