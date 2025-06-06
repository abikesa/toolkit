import requests

# Replace with your Flask app's running URL
url = "http://127.0.0.1:5000"

# Get rendered HTML from the live Flask app
response = requests.get(url)

# Save it as index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Export complete: ../index.html")

