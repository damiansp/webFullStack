# if app is called hello.py; not needed if app.py or wsgi.py
#export FLASK_APP=hello
export FLASK_ENV=development # enable dev features (not secure for prod!)
flask run
