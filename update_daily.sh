git checkout gh-pages
git pull
python update_content.py
git add .
git commit -m "Automatic website update"
git push origin HEAD:gh-pages
