# README

## Project Overview

This project extends the implementation of Basic Authentication to include Session Authentication for accessing user endpoints. The following tasks are included in this project:

1. **Implement a Basic Authentication** for user endpoints:
   - `GET /api/v1/users`
   - `POST /api/v1/users`
   - `GET /api/v1/users/<user_id>`
   - `PUT /api/v1/users/<user_id>`
   - `DELETE /api/v1/users/<user_id>`
   - `GET /api/v1/users/me` to retrieve the authenticated User object.

2. **Session Authentication**:
   - Create a `SessionAuth` class inheriting from `Auth`.
   - Implement methods for session creation and user identification using session IDs.
   - Create new views for Session Authentication, specifically for login.

## Directory Structure

- **api/v1/app.py**: The main application file.
- **api/v1/views/users.py**: Contains views for user-related endpoints.
- **api/v1/auth/session_auth.py**: Contains the `SessionAuth` class.
- **api/v1/views/session_auth.py**: Contains views for session authentication (login).
- **models**: Contains the `User` model and other necessary models.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/alx-backend-user-data.git
   cd alx-backend-user-data/0x02-Session_authentication
   ```

2. **Install dependencies**:
   Ensure you have the necessary Python packages installed:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**:
   - `API_HOST`: Set to `0.0.0.0`
   - `API_PORT`: Set to `5000`
   - `AUTH_TYPE`: Set to `session_auth` or `basic_auth`
   - `SESSION_NAME`: Set to `_my_session_id`

## Running the Application

1. **Start the application**:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
   ```

2. **Testing the endpoints**:
   Open another terminal and run the following `curl` commands:

   - Check the status:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/status"
     ```

   - Access user endpoints:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64_credentials>"
     ```

   - Retrieve authenticated user:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic <base64_credentials>"
     ```

   - Session login:
     ```bash
     curl -X POST "http://0.0.0.0:5000/api/v1/auth_session/login" -d "email=bob@hbtn.io&password=H0lbertonSchool98!"
     ```

   - Use session cookie:
     ```bash
     curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=<session_id>"
     ```

## Key Features and Implementation

1. **Session Management**:
   - `SessionAuth` class manages session creation and user identification.
   - Stores session IDs in memory and links them to user IDs.

2. **User Authentication**:
   - Basic Authentication for initial user endpoint access.
   - Session Authentication for user session management and login.

3. **User Endpoints**:
   - Standard CRUD operations on user data.
   - Retrieve the authenticated user using the `/users/me` endpoint.

4. **Session Authentication Views**:
   - Login view to authenticate users and create sessions.

## Notes

- Ensure the previous project (`0x06. Basic authentication`) is completed and all mandatory tasks are done.
- Be mindful of environment variables, especially `AUTH_TYPE` and `SESSION_NAME`.
- The `SessionAuth` class and methods must be correctly implemented and tested.

For any issues or contributions, feel free to open an issue or a pull request on the GitHub repository.
