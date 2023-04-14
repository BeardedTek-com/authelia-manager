# authelia-manager
Flask Web UI for Authelia Management

This will eventually be a web based UI to configure authelia.

See [CHANGELOG.md](CHANGELOG.md) for current progress
## What will it configure?
### Base Config
### Authentication
##### For not ONLY text file user database (yml file)
### Access Control
##### Define Networks
##### Define Rules

## Requirements
- Python (3.10 or above recommended)
- UWSGI already installed or full development environment including python-devel for your version of python
- Tested on Linux, but *should* work on Windows in theory

## More Info
Take a look at the issues to find more information about what I plan to implement.

## Testing
To test, take the following steps:
#### Clone Repository
```
git clone https://github.com/beardedtek-com/authelia-manager
```
#### Entery authelia-manager directory
```
cd authelia-manager
```

### Start it up
```
./run.sh
```
### run.sh takes the following actions:
- Creates a new virtual environment in .venv if it does not exist: `python3 -m venv .venv`
- Activates the virtual environment: `source .venv/bin/activate`
- Installs python requirements: `pip install -r requirements.txt`
- Starts up uWSGI on port 5000

At this point, you should have the following output at the bottom of your terminal:
```
*** Starting uWSGI 2.0.21 (64bit) on [Mon Dec 19 14:06:39 2022] ***
compiled with version: 12.2.1 20221020 [revision 0aaef83351473e8f4eb774f8f999bbe87a4866d7] on 19 December 2022 20:06:43
os: Linux-5.15.79.1-microsoft-standard-WSL2 #1 SMP Wed Nov 23 01:01:46 UTC 2022
nodename: DESKTOP-E1K894R
machine: x86_64
clock source: unix
detected number of CPU cores: 12
current working directory: /home/localadmin/Github/authelia-manager
detected binary path: /home/localadmin/Github/authelia-manager/venv/bin/uwsgi
!!! no internal routing support, rebuild with pcre support !!!
*** WARNING: you are running uWSGI without its master process manager ***
your processes number limit is 63811
your memory page size is 4096 bytes
detected max file descriptor number: 1048576
lock engine: pthread robust mutexes
thunder lock: disabled (you can enable it with --thunder-lock)
uWSGI http bound on 0.0.0.0:5000 fd 4
spawned uWSGI http 1 (pid: 14174)
uwsgi socket 0 bound to TCP address 127.0.0.1:43817 (port auto-assigned) fd 3
Python version: 3.10.9 (main, Dec 08 2022, 14:49:06) [GCC]
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0xe2f970
your server socket listen backlog is limited to 100 connections
your mercy for graceful operations on workers is 60 seconds
mapped 291616 bytes (284 KB) for 4 cores
*** Operational MODE: preforking ***
WSGI app 0 (mountpoint='') ready in 1 seconds on interpreter 0xe2f970 pid: 14173 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI worker 1 (pid: 14173, cores: 1)
spawned uWSGI worker 2 (pid: 14185, cores: 1)
spawned uWSGI worker 3 (pid: 14186, cores: 1)
spawned uWSGI worker 4 (pid: 14187, cores: 1)
```
#### Try it out:
[http://localhost:5000/api](http://localhost:5000/api)

This will allow you to see the work that's been done in the API so far.  It's getting there, but still a long ways away.

# Screenshots
## Main Landing / Info Page
![Main Landing Page](https://github.com/BeardedTek-com/authelia-manager/blob/main/docs/images/ui_main-screenshot.png)

## Login Page
![Login Page](https://github.com/BeardedTek-com/authelia-manager/blob/main/docs/images/ui_login-screenshot.png)