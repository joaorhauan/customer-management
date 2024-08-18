from flask import Flask
from configuration import allConfig

app = Flask(__name__)

allConfig(app)

app.run(debug=True)