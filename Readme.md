Some fiddling around with https://github.com/azlux/pymumble and https://github.com/matrix-org/matrix-python-sdk

## Using it
You can test it with docker/docker-compose or directly on you mashine.
After cloning the repo you need to modify mtrix.py with a usable Matrix Account (and change the matrix_server variable accordingly)

## Using it via Docker-Compose
git clone https://github.com/vorletzter/mtrix/

cd mtrix

docker-compose up

## Runing it on localhost with Virtuel Environment

git clone https://github.com/vorletzter/mtrix/
cd mtrix/app
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt 
python mtrix.py
