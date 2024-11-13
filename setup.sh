python3 -m venv venv
.venv/bin/activate
pip install --upgrade pip
pip install pip-tools pip-chill
pip-chill --no-version > requirements.in
pip-compile requirements.in
pip-sync
