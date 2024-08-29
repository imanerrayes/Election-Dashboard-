# Election Dashboard

This project sets up a simple dashboard to display election numbers. The dashboard is built using Python and Flask.

## Features
- Display real-time election data
- Filter and search through different elections
- Interactive charts and visualizations

## Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/election-dashboard.git
    cd election-dashboard
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python run.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000/` to view the dashboard.

## Usage
- Add your election data in the `app/data/elections.csv` file.
- Customize the dashboard appearance in `app/templates/index.html` and `app/static/css/style.css`.

## Contributing
Feel free to submit issues or pull requests to enhance the dashboard.

## License
This project is licensed under the MIT License.
