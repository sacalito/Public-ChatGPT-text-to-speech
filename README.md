# Public-ChatGPT-text-to-speech
Very basic python script to use openai text to speech with voice option
runs on port 5003

# docs
https://platform.openai.com/docs/guides/text-to-speech

# install

apt update && apt upgrade -y && apt install python3 python3.10-venv pip && pip install Flask && pip install openai
python3 -m venv env
source env/bin/activate

# export dependencies

pip freeze > requirements.txt

# run
python3 app.py 

# exit
Ctrl+C




