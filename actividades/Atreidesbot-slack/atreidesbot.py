import random

class AtreidesBot:
    HOLA_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Hola! "
            )

        }
    }

    def __init__(self, channel):
        self.channel = channel


    def _choose_message(self):
        rand_int = random.randint(0,1)
        if rand_int == 0:
            results = "buenos días"
        else:
            results = "buenas tardes"
        
        text = f"{results}"

        return {"type": "section", "text":{"type":"mrkdwn","text":text}},
    
    def get_message_payload(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.HOLA_BLOCK,
                *self._choose_message(),

            ],
        } 