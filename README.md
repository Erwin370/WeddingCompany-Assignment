# Wedding Assignment Backend Service

This project is a backend service built using FastAPI to manage organizations in a multi-tenant architecture with MongoDB as the database.

## Features
- Create, retrieve, update, and delete organizations.
- Dynamic MongoDB collection creation for each organization.
- Admin authentication using JWT.

## Requirements
- Python 3.9+
- MongoDB

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```env
   MONGO_URI="your_mongo_connection_string"
   JWT_SECRET="your_jwt_secret"
   ```
4. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints
- **POST /org/create**: Create an organization.
- **GET /org/get**: Retrieve organization details.
- **PUT /org/update**: Update organization details.
- **DELETE /org/delete**: Delete an organization.
- **POST /admin/login**: Admin login.

## Folder Structure
- `main.py`: Entry point of the application.
- `models/`: Contains Pydantic models.
- `routes/`: Contains API route handlers.
- `services/`: Contains business logic.
- `utils/`: Contains utility functions (e.g., authentication, database connection).

## License
This project is licensed under the MIT License.