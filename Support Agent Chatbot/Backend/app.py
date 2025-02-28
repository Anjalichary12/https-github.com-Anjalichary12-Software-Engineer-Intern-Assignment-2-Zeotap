from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
CORS(app)

CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_cdp_docs(cdp, query):
    """
    Function to fetch relevant sections from the CDP documentation.
    """
    if cdp not in CDP_DOCS:
        return f"CDP '{cdp}' is not supported."

    url = CDP_DOCS[cdp]
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract text from the documentation
        all_text = soup.get_text().lower()

        # Check if query is present
        if query.lower() in all_text:
            return f"Relevant information found in {cdp} documentation: {url}"
        else:
            return f"No exact match found in {cdp} documentation. Try rephrasing your query."
    
    except requests.exceptions.RequestException as e:
        return f"Error fetching {cdp} documentation: {str(e)}"

@app.route("/ask", methods=["GET"])
def ask():
    """
    API endpoint to handle 'how-to' questions.
    Example request: /ask?cdp=segment&query=How to set up a new source?
    """
    cdp = request.args.get("cdp", "").strip().lower()
    query = request.args.get("query", "").strip().lower()

    if not cdp or not query:
        return jsonify({"error": "Please provide both 'cdp' and 'query' parameters"}), 400

    result = scrape_cdp_docs(cdp, query)
    return jsonify({"response": result})

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)