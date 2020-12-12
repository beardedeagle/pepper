PYVERSION?=py38
SALT?=v3002.2
BACKEND?=cherrypy
DEBIAN_FRONTEND=noninteractive

install:
	apt update && apt install -y libc6-dev libffi-dev gcc git openssh-server libzmq3-dev
	pip install tox

test: install
	tox -e flake8,$(PYVERSION)-$(BACKEND)-$(SALT)
