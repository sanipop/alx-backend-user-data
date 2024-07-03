# Project: Authentication and Personal Data Handling

## Table of Contents
1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Tasks](#tasks)
   - [Task 0: Regex-ing](#task-0-regex-ing)
   - [Task 1: Log Formatter](#task-1-log-formatter)
   - [Task 2: Create Logger](#task-2-create-logger)
   - [Task 3: Connect to Secure Database](#task-3-connect-to-secure-database)
   - [Task 4: Read and Filter Data](#task-4-read-and-filter-data)
   - [Task 5: Encrypting Passwords](#task-5-encrypting-passwords)
   - [Task 6: Check Valid Password](#task-6-check-valid-password)
6. [Repository Structure](#repository-structure)

## Introduction

This project focuses on handling personal data with a strong emphasis on data privacy and security. You will learn how to obfuscate sensitive information, implement secure logging, manage database connections securely, and handle password encryption and validation.

## Resources

Read or watch:
- [What Is PII, non-PII, and Personal Data?](#)
- [Logging Documentation](#)
- [bcrypt Package](#)
- [Logging to Files, Setting Levels, and Formatting](#)

## Learning Objectives

By the end of this project, you should be able to explain:
- Examples of Personally Identifiable Information (PII).
- How to implement a log filter to obfuscate PII fields.
- How to encrypt a password and validate it.
- How to authenticate to a database using environment variables.

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should follow the `pycodestyle` style guide (version 2.5).
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All modules, classes, and functions should have proper documentation.
- All functions should be type annotated.

## Tasks

### Task 0: Regex-ing

Write a function `filter_datum` to return an obfuscated log message using regex.

**Arguments:**
- `fields`: List of strings representing fields to obfuscate.
- `redaction`: String to replace the field value.
- `message`: The log line.
- `separator`: The character separating the fields in the log line.

**Example:**
```python
fields = ["password", "date_of_birth"]
message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
print(filter_datum(fields, 'xxx', message, ';'))
# Output: name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
```

**File:** `filtered_logger.py`

### Task 1: Log Formatter

Update the `RedactingFormatter` class to filter values in log records using `filter_datum`.

**Example:**
```python
message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))
# Output: [HOLBERTON] my_logger INFO 2019-11-19 18:24:25,105: name=Bob; email=***; ssn=***; password=***;
```

**File:** `filtered_logger.py`

### Task 2: Create Logger

Implement `get_logger` to return a `logging.Logger` object configured to use `RedactingFormatter`.

**Example:**
```python
print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))
# Output:
# <class 'logging.Logger'>
# PII_FIELDS: 5
```

**File:** `filtered_logger.py`

### Task 3: Connect to Secure Database

Implement `get_db` to return a connector to a secure MySQL database using environment variables for credentials.

**Example:**
```python
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
# Output: 2
```

**File:** `filtered_logger.py`

### Task 4: Read and Filter Data

Implement a `main` function to read and display all rows from the `users` table with filtered PII fields.

**Example:**
```shell
# Output:
# [HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=...; last_login=...; user_agent=...
```

**File:** `filtered_logger.py`

### Task 5: Encrypting Passwords

Implement `hash_password` to return a salted, hashed password using `bcrypt`.

**Example:**
```python
print(hash_password(password))
# Output: b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
```

**File:** `encrypt_password.py`

### Task 6: Check Valid Password

Implement `is_valid` to validate if a password matches a hashed password using `bcrypt`.

**Example:**
```python
print(is_valid(encrypted_password, password))
# Output: True
```

**File:** `encrypt_password.py`

## Repository Structure

```plaintext
alx-backend-user-data/
├── 0x00-personal_data/
│   ├── filtered_logger.py
│   ├── encrypt_password.py
│   └── README.md
```
