from urllib.request import urlretrieve

SOMETHING = 'a36072f2e4ab4839875c8bfdcaa386dd'
word = 'Derniere'

URL = f"http://api.voicerss.org/?key=a36072f2e4ab4839875c8bfdcaa386dd&hl=fr-fr&c=wav&f=16khz_16bit_stereo&v=Axel&src={word}"

filename = f'./output/{word}.wav'
urlretrieve(URL, filename)
