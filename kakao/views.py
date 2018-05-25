#git 오류나면 git stash save ""
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import pyrebase

#데이터베이스 설정
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


#챗봇 구현

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['사용법','현재 금액','+','-','정리']})

@csrf_exempt
def answer(request): #메세지함수

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '사용법':
        explain = "앱과 연동하여 쓰기 쉽도록 만들어졌습니다 어쩌고저쩌고"


        def insert_data():
            db.child("users").child("지출").set(data) # users>지출>data입력
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
                    'text': explain  #사용법설명
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['사용법','현재 금액','+','-','정리']
                }

            })

    elif datacontent == '현재 금액':
        remain = "12345678원 남았습니다."

        return JsonResponse({
                'message': {
                    'text': remain
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['사용법','현재 금액','+','-','정리']
                }

            })
    elif datacontent == '+':
        entermoney = "입금금액을 입력해주세요"

        return JsonResponse({
                'message': {
                    'text': entermoney + datacontent
                    },
                'keyboard' : {
                'type' : 'text' #텍스트로 입력받기 위하여 키보드 타입을 text로 설계
                 },
                 })
    elif datacontent == '-':
        spendmoney = "지출금액을 입력해주세요"

        return JsonResponse({
                'message': {
                    'text': spendmoney
                },
                'keyboard' : {
                'type' : 'text' #텍스트로 입력받기 위하여 키보드 타입을 text로 설계
                 },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['사용법','현재 금액','+','-','정리']
                }

            })
    elif datacontent == '정리':
        remain = "12345678원 남았습니다."

        return JsonResponse({
                'message': {
                    'text': remain
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['사용법','현재 금액','+','-','정리']
                }

            })
