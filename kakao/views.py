from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import pyrebase

config = {
    'apiKey': "AIzaSyAsAGGqVZ1bVlFh-Eu3o0yULHysGiJQ0Qk",
    'authDomain': "test-39511.firebaseapp.com",
    'databaseURL': "https://test-39511.firebaseio.com",
    'projectId': "test-39511",
    'storageBucket': "test-39511.appspot.com",
    'messagingSenderId': "881496749264"
  }

firebase=pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

email="woo4675@gmail.com"
password="kkcc1313"

user = auth.sign_in_with_email_and_password(email, password)

data = {
    "날짜": "2018년 5월 24일",
    "재산": "이백만원",
}



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
        def insert_data():
            db.child("users").child("지출").set(data)
    #db.child("users").push(data)
    #with key
        def update(string_key, string_data):
            db.child("users").child(string_key).update(string_data)

        def remove(string_key):
            db.child("users").child(string_key).remove()

        def get_data(string1):
            datatmp = db.child("users").child(string1).get()
            print(datatmp.val())

        insert_data()



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
