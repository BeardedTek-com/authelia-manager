# 2022/12/19

- Created a basic UI so things are easier to read
  - uses tailwind css cdn
  - NOTE: need to figure out building a custom tailwind css file out
- API Endpoints to read current configuration
  - Reads yaml config into a dict then displays as JSON or YAML
  - Needs better templating to remove html from code.

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
