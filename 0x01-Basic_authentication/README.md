# Basic Authentication Project

## Project Overview

In this project, you will learn about the authentication process and implement Basic Authentication on a simple API. While it's recommended to use existing modules or frameworks for authentication in production, this project is aimed at helping you understand the underlying mechanisms by building your own.

## Background Context

In the industry, it’s best practice to use well-established authentication modules or frameworks (e.g., Flask-HTTPAuth for Python-Flask). However, this project provides a hands-on experience to understand the process by implementing Basic Authentication from scratch.

## Learning Objectives

By the end of this project, you should be able to explain:

- What authentication means.
- What Base64 is and how to encode a string in Base64.
- What Basic Authentication means.
- How to send the Authorization header.

## Resources

- [REST API Authentication Mechanisms](#)
- [Base64 in Python](#)
- [HTTP header Authorization](#)
- [Flask](#)
- [Base64 - concept](#)

## Requirements

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code must follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- The length of files will be tested using `wc`.
- All modules should have documentation.
- All classes should have documentation.
- All functions (inside and outside a class) should have documentation.

## Project Structure

The project consists of multiple tasks, each building upon the previous one. Below is a brief summary of the tasks:

1. **Simple-basic-API**: Setup and start the provided API, verify it works with curl requests.
2. **Error handler: Unauthorized**: Implement an error handler for unauthorized requests (HTTP 401).
3. **Error handler: Forbidden**: Implement an error handler for forbidden requests (HTTP 403).
4. **Auth class**: Create a base class to manage API authentication.
5. **Define which routes don't need authentication**: Update the `require_auth` method to exclude specific paths from authentication.
6. **Request validation!**: Validate requests to secure the API, using the `authorization_header` method.
7. **Basic auth**: Create a `BasicAuth` class that inherits from `Auth`.
8. **Basic - Base64 part**: Implement a method to extract the Base64 part of the Authorization header.
9. **Basic - Base64 decode**: Implement a method to decode the Base64 string.
10. **Basic - User credentials**: Implement a method to extract user credentials from the decoded Base64 string.
11. **Basic - User object**: Implement a method to return the User instance based on email and password.
12. **Basic - Overload current_user**: Implement the `current_user` method to retrieve the User instance for a request, completing the Basic Authentication.

## Usage

To set up and run the API, follow these steps:

1. **Install dependencies**:
   ```sh
   pip3 install -r requirements.txt
   ```

2. **Start the server**:
   ```sh
   API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
   ```

3. **Use the API** (in another terminal or browser):
   ```sh
   curl "http://0.0.0.0:5000/api/v1/status"
   ```

## Example Commands

- To check the API status:
  ```sh
  curl "http://0.0.0.0:5000/api/v1/status"
  ```

- To trigger unauthorized error:
  ```sh
  curl "http://0.0.0.0:5000/api/v1/unauthorized"
  ```

- To trigger forbidden error:
  ```sh
  curl "http://0.0.0.0:5000/api/v1/forbidden"
  ```

- To authenticate a user:
  ```sh
  curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <Base64_encoded_credentials>"
  ```

## Repository Structure

- **GitHub repository**: alx-backend-user-data
- **Directory**: 0x01-Basic_authentication

## File Structure

- `api/v1/app.py`: Main application file.
- `api/v1/auth/__init__.py`: Auth package initializer.
- `api/v1/auth/auth.py`: Base Auth class.
- `api/v1/auth/basic_auth.py`: BasicAuth class.
- `api/v1/views/index.py`: API view endpoints.
- `models/user.py`: User model for storing user data.

## Conclusion

This project guides you through the process of implementing Basic Authentication from scratch, providing a deep understanding of the authentication mechanism and its components. By completing this project, you'll gain valuable knowledge applicable to real-world API security practices.
