ENV=${1:-development}
export FLASK_APP=flaskr
export FLASK_ENV=$ENV
flask init-db
