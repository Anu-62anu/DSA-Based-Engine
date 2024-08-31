# TF-IDF Search Engine

This project is a simple TF-IDF search engine implemented using Flask. It allows you to search for documents based on query terms and displays the most relevant results.

## Getting Started

To get started with this project, follow these steps:

### Prerequisites

1. **Python**: Ensure you have Python installed on your system.
2. **Dependencies**: You need to install the required Python packages.

### Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Anu-62anu/DSA-Based-Engine.git
    cd DSA-Based-Engine
    ```

2. **Install Dependencies**:

    Install the required Python packages. Since you’ve deleted the `requirements.txt` file, you need to manually reinstall the necessary packages. Based on the code, the required packages include:

    - `Flask`
    - `Flask-WTF`
    - `WTForms`

    You can install these packages using pip:

    ```bash
    pip install Flask Flask-WTF WTForms
    ```

3. **Add Missing Files**: Make sure the following files are present in the `tf-idf-final/` directory:

    - `links.txt`
    - `vocab.txt`
    - `idf-values.txt`
    - `documents.txt`
    - `inverted-index.txt`

    If these files are missing, please restore them or ensure they are correctly named and formatted.

### Running the Application

1. **Run the Flask Application**:

    Navigate to the project directory and run the Flask application:

    ```bash
    python app.py
    ```

    This will start the Flask development server.

2. **Access the Application**:

    Open your web browser and go to `http://127.0.0.1:5000`. You will see the search interface.

3. **Search for Documents**:

    Enter your search query in the input field and click "Search". The application will display the most relevant documents based on your query.

## Security Note

- **Do not use the Flask development server** in a production environment. For production use, consider deploying with a production WSGI server such as Gunicorn or uWSGI.

## Troubleshooting

- **If you encounter any issues**, make sure that all the required files are correctly named and located in the `tf-idf-final/` directory.
- **Check the terminal output** for any error messages to help diagnose problems.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


