# About
A python script that scrapes to check if Outer Wilds is available yet on the Nintendo Switch, sends an email with the result.
# Requirements
- Docker or Python 3 (with `beautifulsoup4` and `requests` installed)
- SMTP server with STARTTLS on port 587
# Usage 
First clone the repo

	git clone https://github.com/mrysn/switch_outerwilds_availability
	cd switch_outerwilds_availability

## Run using Docker via bash script
Using the bash script `build_and_run.sh` is recommended, it will check for secret files used to authenticate with the SMTP server and if they do not exist it will  prompt for the needed information:

	# ./build_and_run.sh

## Alternatives
Alternatively you can manually run this in Docker with these commands

	docker build -t outerwilds .
	docker run -it outerwilds
  
And alternativelty to using Docker you can run this in your local machine if Python 3 is installed, get the dependancies first

	pip3 install beautifulsoup4 requests
	python3 ./switch_outerwilds.py

Both alternatives manually require you to create .secret files

	# printf "smtp.mydomain.com" > ./.secret.server  # your smtp server
	# printf "email@mydomain.com" > ./.secret.from   # your smtp login username (and email sender/from address)
	# printf "myAMAZINGpassword" > ./.secret.pass    # yoyr smtp login password (in plain-text)
	# printf "alert@mydomain.com" > ./.secret.to     # email address to send to
