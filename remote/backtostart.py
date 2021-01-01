from samsungtvws import SamsungTVWS
import os



# Autosave token to file 
token_file = os.path.dirname(os.path.realpath(__file__)) + '/tv-token.txt'
print(token_file)
tv = SamsungTVWS(host='10.35.0.13', port=8002, token_file=token_file)

 