from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘 쓴 돈','남은돈']
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘 쓴 돈':
        today = "10000원입니다"

        return JsonResponse({
                'message': {
                    'text': today
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘 쓴 돈','남은돈']
                }

            })

    elif datacontent == '남은돈':
        remain = "12345678원 남았습니다."

        return JsonResponse({
                'message': {
                    'text': remain
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘 쓴 돈','남은돈']
                }

            })
