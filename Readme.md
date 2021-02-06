Some fiddling around with https://github.com/azlux/pymumble and https://github.com/matrix-org/matrix-python-sdk

# Disclaimer
All Cats will hate you, if you use this in anything resembling a production environment. 
**Do not use it for other purposes then testing**

# Using it
After cloning the repo you need to modify mtrix.py with a usable Matrix Account (and change the matrix_server variable accordingly)

## via Docker-Compose
```
git clone https://github.com/vorletzter/mtrix/
cd mtrix
docker-compose up
```

## Runing it on localhost with Virtuel Environment
```
git clone https://github.com/vorletzter/mtrix/
cd mtrix/app
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt 
python mtrix.py
```
