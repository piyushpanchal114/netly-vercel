

# Build the project
echo "Building the project..."
python pipenv install
python3.9 -m pip install -r requirements.txt

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build End"

