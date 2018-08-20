import requests, os
from flask import Flask, Response, request
from twilio import messages
from googleCloud.speechAPI import transcribe

app = Flask(__name__)
speechURL = "https://speech.googleapis.com/v1/speech:recognize?key=" + os.environ['apiKey']


@app.route('/', methods=['GET', 'POST'])
def handleTwilioCall():
    RecordingUrl = request.form.get('RecordingUrl')

    if RecordingUrl is None:
        response = Response(response=messages.welcomeMessage, mimetype='text/xml')
    else:
        res = requests.get(url=RecordingUrl)

        if int(res.status_code) != 200:
            response = Response(response=messages.transcribeErrorMessage, mimetype='text/xml')
        else:
            byteRecording = res.content
            replyFromGoogleApi = transcribe(encoding="LINEAR16", sampleRateHertz=8000, languageCode="en-US",
                                            byteRecording=byteRecording, speechURL=speechURL)

            if replyFromGoogleApi.get('results', None) != None:
                passcode = replyFromGoogleApi['results'][0]['alternatives'][0]['transcript']
                if passcode == os.environ['passcode']:
                    response = Response(response=messages.comeInMessage, mimetype='text/xml')
                else:
                    response = Response(response=messages.goAwayMessage, mimetype='text/xml')

            else:
                response = Response(response=messages.noSpeechInRecordMessage, mimetype='text/xml')

    return response


if __name__ == '__main__':
    app.run()
