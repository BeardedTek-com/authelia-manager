#!/usr/bin/env bash
RED=$'\033[0;31m'
LRED=$'\033[1;31m'
CYAN=$'\033[0;36m'
NC=$'\033[0m' # No Color
LABEL="${LRED}[ ${RED}Authelia-Manager ${LRED}]${CYAN}"
if [ ! -d "./.venv" ]; then
    echo "${LABEL} Creating Python Virtual Environment${NC}"
    python3 -m venv .venv
else
    echo "${LABEL} Python Virtual Environment Exists at .venv${NC}"
fi
echo "${LABEL} Activating Python Virtual Environment${NC}"
source .venv/bin/activate
[ ! -f '.pip' ] && echo "${LABEL} Installing Python Requirements${NC}" && python -m pip install -r requirements.txt
if [ "$?" == "0" ]; then
    echo "${LABEL} Creating .pip to bypass installing Python Requirements next time${NC}"
    touch .pip
else
    echo "${LABEL} Python Requirements already installed.  Skipping."
fi
echo "${LABEL} Starting UWSGI Web Server${NC}"
uwsgi --http 0.0.0.0:5000 --wsgi-file authelia-manager.py --callable app --workers 4 --uid 1000 --gid 1000
