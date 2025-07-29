python setup.py sdist bdist_wheel
twine upload dist/*
git commit -m "quick upload"
git push