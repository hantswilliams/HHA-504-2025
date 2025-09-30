from flask import Flask

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>AHI 504 Flask VM Demo</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            color: #333;
            text-align: center;
            margin: 50px;
          }
          h1 {
            color: #c8102e; /* Stony Brook red */
          }
          p {
            font-size: 1.2em;
          }
          .footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #777;
          }
        </style>
      </head>
      <body>
        <h1>🚀 Flask is Running on Your Cloud VM!</h1>
        <p>
          Congratulations — you’ve deployed a Python Flask app on port 5003.<br>
          If you can see this page, your networking and Flask setup worked!
        </p>
        <div class="footer">
          <p>AHI 504 — Cloud Foundations for Health Informatics</p>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    # Run on all interfaces (so it's accessible via public IP), port 5003
    app.run(host="0.0.0.0", port=5003)