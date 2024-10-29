import json
from channels.generic.websocket import WebsocketConsumer

class ScrapeStatusConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def send_scrape_status(self, event):
        # Enviar mensaje cuando el scraping termine
        self.send(text_data=json.dumps({
            'status': 'completed',
            'data': event['data'],
        }))
