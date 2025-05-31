from flask import Flask, render_template, request
import fitz  # PyMuPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf' not in request.files:
        return "No file part", 400

    file = request.files['pdf']

    if file.filename == '':
        return "No selected file", 400

    # Read and extract text from PDF
    pdf_text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            pdf_text += page.get_text()

    return render_template('result.html', extracted=pdf_text)

if __name__ == '__main__':
    app.run(debug=True)
