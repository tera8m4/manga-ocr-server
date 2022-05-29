from flask import Flask
from flask  import request
from flask_cors import CORS
from PIL import Image
import re
from io import BytesIO
import base64
from manga_ocr import MangaOcr

app = Flask(__name__)
CORS(app)
mocr = MangaOcr()

@app.route("/decode", methods=['POST'])
def hello_world():
    content = request.get_json(silent=True)
    text = 'Failed'
    try:
        data = content.get('data')
        image_data = re.sub('^data:image/.+;base64,', '', data)
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        text = mocr(image)
    except:
        text = 'Failed'
    return text

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)