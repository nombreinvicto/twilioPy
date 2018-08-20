welcomeMessage = r"""
                <Response>
                    <Say voice="man">Hello Guest. Tell me the passcode!</Say>
                <Record timeout="5" playBeep="true" />
                </Response>"""

comeInMessage = r"""
                <Response>
                    <Say voice="man">Gate Open! Access Granted.</Say>
                </Response>"""

goAwayMessage = r"""
                <Response>
                    <Say voice="man">Not going to let you in. Access Denied.</Say>
                </Response>"""

transcribeErrorMessage = r"""
                <Response>
                    <Say voice="man">Transcribe Error. Access Denied. Try Again</Say>
                </Response>"""

noSpeechInRecordResponse = r"""
                <Response>
                    <Say voice="man">No voice detected</Say>
                </Response>"""

debugResponse = r"""
                <Response>
                    <Say voice="man">This is Debug Response.</Say>
                </Response>"""
