```shell
# create env
virtualenv -p python3 env
source env/bin/activate

# get project
git clone https://github.com/greyfenrir/cargo.git
cd cargo/back

# get requirements
pip install -r requirements.txt

# update db
python manage.py migrate
python manage.py createsuperuser

# run server
python manage.py runserver

# run unit tests
python manage.py test
```