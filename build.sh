

# Build the project
echo "Building the project..."
python3.9 pipenv install

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

echo "Build End"

