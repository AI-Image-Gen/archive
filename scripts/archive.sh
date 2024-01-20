sudo apt update
sudo apt install -y p7zip-full git

git clone https://github.com/AI-Image-Gen/generator

mkdir -p ./tmp
mv ./generator/img/old/* ./tmp
rm -rf ./generator

current_date=$(date +"%Y-%m-%d")
mkdir -p "../archived/$current_date"

7z a -t7z -mx=9 "../archived/$current_date/$current_date.7z" "./tmp/*"

python archive.py "$current_date"

rm -rf ./tmp

cd ..
git config --global user.name archivizer
git config --global user.email github-actions@github.com
git add .
git commit -m "Archivize $current_date"