
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Car Manufacturing in India</title></head>
        <body>
            <h1>Indian Car Manufacturing Details</h1>
            <ul>
                <li>Maruti Suzuki - Gurgaon, Haryana</li>
                <li>Tata Motors - Pune, Maharashtra</li>
                <li>Hyundai - Sriperumbudur, Tamil Nadu</li>
                <li>Mahindra - Nashik, Maharashtra</li>
                <li>Kia - Anantapur, Andhra Pradesh</li>
            </ul>
        </body>
    </html>
    '''
