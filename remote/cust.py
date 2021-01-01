import base64
import json
import logging
import time
import websocket

class SamsungTV():

    _URL_FORMAT = 'ws://{host}:{port}/api/v2/channels/samsung.remote.control?name={name}'

    _KEY_INTERVAL = 1.5

    def __init__(self, host, port=8001, name='SamsungTvRemote'):
        self.connection = websocket.create_connection(
            self._URL_FORMAT.format(**{
                'host': host, 
                'port': port, 
                'name': self._serialize_string(name)
            })
        )

        response = json.loads(self.connection.recv())
        if response['event'] != 'ms.channel.connect':
            raise Exception(response)
            self.close()

    def __exit__(self, type, value, traceback):
        self.close()

    def _serialize_string(self, string):
        if isinstance(string, str):
            string = str.encode(string)
        return base64.b64encode(string).decode('utf-8')

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            logging.debug('Connection closed.')

    def send_key(self, key, repeat=1):
        for n in range(repeat):
            payload = json.dumps({
                'method': 'ms.remote.control',
                'params': {
                    'Cmd': 'Click',
                    'DataOfCmd': key,
                    'Option': 'false',
                    'TypeOfRemote': 'SendRemoteKey'
                }
            })

            logging.info('Sending key %s', key)
            self.connection.send(payload)
            time.sleep(self._KEY_INTERVAL)

    # power

tv = SamsungTV('10.35.0.13')


tv.send_key('KEY_VOLUP')
