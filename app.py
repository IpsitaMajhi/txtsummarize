# app.py
from flask import Flask, request, jsonify,render_template
from text_summary import summarizer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        print("Triggered")
        # Get the text data from the frontend
        data = request.json['input_content']

        # Call the summarizer function to generate the summary
        summary = summarizer(data)

        # Return the summary as JSON
        return jsonify({'summary': summary})

    except Exception as e:
        # Handle exceptions as needed
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
