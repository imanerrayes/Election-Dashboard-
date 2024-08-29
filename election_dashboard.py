from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Sample election data
election_data = pd.DataFrame({
    'name': ['Election 2024', 'Election 2023'],
    'date': ['2024-11-05', '2023-11-07'],
    'voters': [100000, 90000],
    'counted': [75000, 85000],
    'results': ['Pending', 'Complete']
})

# HTML template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        h1 {
            text-align: center;
        }

        table {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
        }

        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }

        th {
            background-color: #f4f4f4;
        }
    </style>
    <title>Election Dashboard</title>
</head>
<body>
    <h1>Election Dashboard</h1>
    <table>
        <thead>
            <tr>
                <th>Election Name</th>
                <th>Date</th>
                <th>Number of Voters</th>
                <th>Votes Counted</th>
                <th>Results</th>
            </tr>
        </thead>
        <tbody>
            {% for election in elections %}
            <tr>
                <td>{{ election['name'] }}</td>
                <td>{{ election['date'] }}</td>
                <td>{{ election['voters'] }}</td>
                <td>{{ election['counted'] }}</td>
                <td>{{ election['results'] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(template, elections=election_data.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
