# Jobify

Jobify is a dynamic platform to discover and apply for the best job opportunities in Cameroon. Find a job that matches your skills, preferences, and location. Simple, fast, and efficient.

## Features

- **User Management**: User registration, secure login with JWT, and profile management.
- **Job Management**: Create, update, delete, and search for job postings.
- **Region Management**: Add and manage regions associated with jobs.
- **Difficulty Levels**: Define and manage difficulty levels for jobs.
- **Secure API**: Robust authentication and authorization.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/jobify.git
   cd jobify
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   - By default, Jobify uses SQLite. You can modify the configuration in `jobify/database.py`.

5. Start the server:
   ```bash
   uvicorn jobify.main:app --reload
   ```

6. Access the interactive API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Usage

- Use the API endpoints to manage users, jobs, regions, and difficulty levels.
- Refer to the Swagger documentation for detailed API usage.

## Contribution

Contributions are welcome! Please submit a pull request or open an issue to report bugs or suggest improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
