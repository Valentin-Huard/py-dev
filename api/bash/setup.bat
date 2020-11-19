python -m venv env
./env/Scripts/activate
pip install -r requirements.txt
python manage.py loaddata quickstart/fixtures/lignes.json
python manage.py loaddata quickstart/fixtures/prediction.json