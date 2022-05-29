from email.mime import application
from whitenoise import WhiteNoise

from index import app

application = WhiteNoise(app)