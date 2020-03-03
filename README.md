# 장고 공부 시작

### 개발 환경
* python 3.8
* django 3.0.3
* mysql 8.x

### 가상화
작업 공간으로 이동: `cd ~/workspace/django`
가상화 생성: `python -m venv .venv`
가상화 실행: `. .venv/bin/activate`
가상화 종료: `deactivate`

### package 설치
pip 업그레이드: `python -m pip install --upgrade pip`
django 설치: `pip install django`
django 설치(특정 버전): `pip install django~=2.0.0`

### 장고 기본 설정 구성
기본 설정 구성: `django-admin startproject mysite .`

### settings.py 설정 추가 및 변경
```python
TIME_ZONE = 'Asia/Seoul'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'django',
       'USER': 'root',
       'PASSWORD': '',
       'HOST': '127.0.0.1',
       'PORT': '3306'
    }
}
```

### Mac에서 mysql 준비
* mysql 설치: `brew install mysql`
* mysql client 설치 (Mac에서 원래 그냥 pip 설치하면 되었는데 버그로 인하여 openssl을 이용해야한다고 함)
    * `brew install openssl`
    * `cd ~/workspace/django`
    * `LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient`


### django run ~
* migrate: `python manage.py migrate`
* run: `python manage.py runserver`



