# 0 - Create Python Virtual Environment
virtualenv --python=/usr/bin/python39 venv
source venv/bin/activate

# 1 - Install pytorch from website
# Go To website

# 2 - Install gym and ray[rllib]
pip install gym ray[rllib] tensorboard yaaf

# 3 - Install dependencies
yay -S cmake qt4 zlib libjpeg-turbo xorg-server-xvfb ffmpeg xorg-server-dev boost sdl2 swig

# 4 - Install HFO
git clone https://github.com/openai/gym-soccer.git
cd gym-soccer
pip install -e .

# 5 - Load server
python connect.py --offense-agents 2 --defense-agents 0 --defense-npcs 1 --server-port 6000
