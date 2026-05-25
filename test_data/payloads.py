# Valid user creation payload
CREATE_USER = {
    "name": "Madhavi",
    "job": "QA Automation Engineer"
}

# Valid update payload
UPDATE_USER = {
    "name": "Madhavi Katte",
    "job": "Senior QA Engineer"
}

# Valid registration
VALID_REGISTER = {
    "email": "eve.holt@reqres.in",   # ReqRes only accepts specific emails
    "password": "pistol"
}

# Missing password - negative tests
REGISTER_MISSING_PASSWORD = {
    "email": "eve.holt@reqres.in"
}

# Valid login
VALID_LOGIN = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

# Wrong credentials - negative tests
INVALID_LOGIN = {
    "email": "wrong@email.com",
    "password": "wrongpass"
}