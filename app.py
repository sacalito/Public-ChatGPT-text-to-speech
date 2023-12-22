from flask import Flask, request, render_template_string
import openai
import random

app = Flask(__name__)
openai.api_key = 'sk-openaikey'

form_template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Text to Speech</title>
</head>
<body>
    <h1>Enter text to synthesize</h1>
    <form method="post">
        <textarea name="text" rows="4" cols="50">{{ text }}</textarea><br>
        <select name="voice">
            <option value="{{voice}}">{{voice}}</option>
            <option value="echo">echo</option>
            <option value="alloy">alloy</option>
            <option value="fable">fable</option>
            <option value="onyx">onyx</option>
            <option value="nova">nova</option>
            <option value="shimmer">shimmer</option>
        </select>
        <input type="submit" value="Synthesize">
    </form>
    {% if audio_file %}
    <audio controls autoplay>
        <source src="{{ url_for('static', filename=audio_file) }}?id={{ random_number }}" type="audio/wav">
        Your browser does not support the audio element.
    </audio>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        voice = request.form['voice']
        response = openai.audio.speech.create(model="tts-1-hd", input=text, voice=voice)

        random_number = random.randint(1, 1000000)
        
        audio_file_path = "static/output.wav"
        response.stream_to_file(audio_file_path)

        # Append the text to history.txt
        with open('history.txt', 'a') as f:
            f.write('Voice: ' + voice + '\n' + text + '\n----------------------------------------------------------------------------------------\n')

        return render_template_string(form_template, audio_file="output.wav", random_number=random_number, text=text, voice=voice)
    else:
        return render_template_string(form_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)