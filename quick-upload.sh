python setup.py sdist bdist_wheel
twine upload dist/*
rm -rf dist build *.egg-info
git add .
git commit -m "quick upload"
git push
