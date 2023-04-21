# 2023/04/20
Much progress has been made
- Restructured database
  - host
  - users
  - groups
  - networks
  - rules
  - totp
  - file_auth
  - config
- JavaScript
  - async code to display and send form data to API
- API
  - Starting to write database queries for updating entries
    - only for users so far
- UI
  - MAJOR UI overhauls.  Using tailwind and flowbite for css and form controls
  - Notifications
- More
  - Lots more than I can remember at this point.  I should have written this as I go...


# 2022/12/18
Initial code dump to database
- Database Models created
    - acc_networks - holds network definitions
    - acc_rules - holds rules definitions
    - config - holds main configuration.yml contents (other than networks and rules)
- API Blueprint created
    - Routes:
        - /api - Lists api endpoints
        - /api/initdb - Initializes Database
        - api/config `GET` - lists current config
            - For now in JSON format, will make it look pretty once the core code is done
        - api/config `POST` - NOT YET CREATED - This will be the endpoint that updates the database with a POST message.
- helpers
    - argon2 - generates an argon2 password given input.  See app/helpers/argon2.py for more info
    - rndpwd - generates a random passphrase or seed. See app/helpers/rndpwd.py for more info
        - taken and slightly modified from beardedtek-com/fevr (another one of my projects)
