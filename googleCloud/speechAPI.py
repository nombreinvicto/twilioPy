import json, requests, base64


class SpeechRequest:
    def __init__(self):
        self.data = {
            'config': {
                'encoding': '',
                'sampleRateHertz': 0,
                'languageCode': ''
            },
            'audio': {
                'content': '',
            }
        }

    def populateSpeechObject(self, encoding: str, sampleRateHertz: int, languageCode: str, byteRecording):
        self.data['config']['encoding'] = encoding
        self.data['config']['sampleRateHertz'] = sampleRateHertz
        self.data['config']['languageCode'] = languageCode
        self.data['audio']['content'] = (str(base64.b64encode(byteRecording)))[2:-1]


def transcribe(encoding: str, sampleRateHertz: int, languageCode: str, byteRecording, speechURL: str) -> dict:
    speechReq = SpeechRequest()
    speechReq.populateSpeechObject(encoding, sampleRateHertz, languageCode, byteRecording)

    j = json.dumps(speechReq.data)
    speechApiReply = requests.post(url=speechURL, data=j)
    transcript = (speechApiReply.content.decode('utf-8'))
    jsonTranscript = json.loads(transcript)

    return jsonTranscript
