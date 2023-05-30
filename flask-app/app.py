Last login: Sun May 21 14:27:02 on console

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Sumedhas-MacBook-Air:~ Sumedha$ python3 --version
Python 3.11.3
Sumedhas-MacBook-Air:~ Sumedha$ mkdir flask-app
Sumedhas-MacBook-Air:~ Sumedha$ cd flask-app
Sumedhas-MacBook-Air:flask-app Sumedha$ mkdir ~/.venvs
Sumedhas-MacBook-Air:flask-app Sumedha$ python3 -m venv 1/.venv/flask
Sumedhas-MacBook-Air:flask-app Sumedha$ source ~/.venvs/flask/bin/activate
-bash: /Users/Sumedha/.venvs/flask/bin/activate: No such file or directory
Sumedhas-MacBook-Air:flask-app Sumedha$ 
Sumedhas-MacBook-Air:flask-app Sumedha$ source ~/.venvs/flask/bin/activate
-bash: /Users/Sumedha/.venvs/flask/bin/activate: No such file or directory
Sumedhas-MacBook-Air:flask-app Sumedha$ python3 -m venv 1/.venv/flask
Sumedhas-MacBook-Air:flask-app Sumedha$ ~/.venvs/flask/bin/activate
-bash: /Users/Sumedha/.venvs/flask/bin/activate: No such file or directory
Sumedhas-MacBook-Air:flask-app Sumedha$ mkdir ~/.venvs
mkdir: /Users/Sumedha/.venvs: File exists
Sumedhas-MacBook-Air:flask-app Sumedha$ python3 -m venv ~/.venvs/flask

Sumedhas-MacBook-Air:flask-app Sumedha$ 
Sumedhas-MacBook-Air:flask-app Sumedha$ source ~/.venvs/flask/bin/activate
(flask) Sumedhas-MacBook-Air:flask-app Sumedha$ pip install Flask gunicorn

Collecting Flask
  Downloading Flask-2.3.2-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.9/96.9 kB 1.3 MB/s eta 0:00:00
Collecting gunicorn
  Downloading gunicorn-20.1.0-py3-none-any.whl (79 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 79.5/79.5 kB 2.2 MB/s eta 0:00:00
Collecting Werkzeug>=2.3.3
  Downloading Werkzeug-2.3.4-py3-none-any.whl (242 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 242.5/242.5 kB 3.0 MB/s eta 0:00:00
Collecting Jinja2>=3.1.2
  Downloading Jinja2-3.1.2-py3-none-any.whl (133 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 133.1/133.1 kB 3.1 MB/s eta 0:00:00
Collecting itsdangerous>=2.1.2
  Downloading itsdangerous-2.1.2-py3-none-any.whl (15 kB)
Collecting click>=8.1.3
  Downloading click-8.1.3-py3-none-any.whl (96 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 96.6/96.6 kB 3.0 MB/s eta 0:00:00
Collecting blinker>=1.6.2
  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)
Requirement already satisfied: setuptools>=3.0 in /Users/Sumedha/.venvs/flask/lib/python3.11/site-packages (from gunicorn) (65.5.0)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.1.2-cp311-cp311-macosx_10_9_x86_64.whl (13 kB)
Installing collected packages: MarkupSafe, itsdangerous, gunicorn, click, blinker, Werkzeug, Jinja2, Flask
Successfully installed Flask-2.3.2 Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.3.4 blinker-1.6.2 click-8.1.3 gunicorn-20.1.0 itsdangerous-2.1.2

[notice] A new release of pip available: 22.3.1 -> 23.1.2
[notice] To update, run: pip install --upgrade pip
(flask) Sumedhas-MacBook-Air:flask-app Sumedha$ 
(flask) Sumedhas-MacBook-Air:flask-app Sumedha$ pip freeze > requirements.txt

(flask) Sumedhas-MacBook-Air:flask-app Sumedha$ 
(flask) Sumedhas-MacBook-Air:flask-app Sumedha$ nano app.py

  UW PICO 5.09                      File: app.py                      Modified  

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sammy!' 
  













^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
