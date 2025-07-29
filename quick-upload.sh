python setup.py sdist bdist_wheel
twine upload dist/*
git add .
git commit -m "quick upload"
git push