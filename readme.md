# inital setting.
```
1. 원하는 폴더 생성
2. pipenv shell
3. pipenv install channels
4. setting corfirm :  
    python 치고, 터미널에 import channels 그리고 print(channels.__version__)'
5. pipenv install Django==3.2.7(버전은 선택사항)
6. django-admin startproject config
7. config 폴더 최상단에 빼옴.
8. python manage.py startapp chat
```
  

```
# mysite/settings.py
INSTALLED_APPS = [
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```
chat/
    __init__.py
    templates/
        chat/
            index.html
    views.py
```
