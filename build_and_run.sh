#!/usr/bin/env bash
smtp_info() {
        read -p "  SMTP Server Address: " smtp_server ; echo
        printf $smtp_server > ./.secret.server
      
        read -p "  SMTP Server Username: " username ; echo
        printf $username > ./.secret.from
      
        read -p "  SMTP Server Password (warning: plain-text): " smtp_pass ; echo
        printf $smtp_pass > ./.secret.pass
      
        read -p "  Send email to address: " send_to ; echo
        printf $send_to > ./.secret.to
}

secrets_check() {
    echo "Checking if .secret files exist..."
    for i in from pass server to; do 
        [ -e "./.secret.$i" ] && (echo OK: .secret.$i ; sleep 1) || (echo Did not find: .secret.$i - please setup secrets... ; sleep 1 ; smtp_info)
    done
}

dockersteps() {
    echo "Building Docker image, starting container and finally deleting image..." ; sleep 1
    tag=outerwilds_`date +%s `
    docker build -t $tag .
    docker run -it $tag
    docker image rm -f $tag
}

read -t 5 -n 1 -sp "Set/Change SMTP secrets? (y/n)" RESP ; echo
if [[ $RESP =~ ^[Yy]$ ]]; then
    smtp_info
    secrets_check
    dockersteps
else
    secrets_check
    dockersteps
fi