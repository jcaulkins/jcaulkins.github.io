git pull
python update_content.py
git add .
git commit -m "Automatic website update"
git push -f origin HEAD:gh-pages
