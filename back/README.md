```shell
virtualenv -p python3 env
source env/bin/activate
git clone https://github.com/greyfenrir/cargo.git
cd cargo/backend/
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```