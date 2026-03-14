import openwakeword
from openwakeword.model import Model

openwakeword.utils.download_models()
model = Model()
print("Model initialized correctly")