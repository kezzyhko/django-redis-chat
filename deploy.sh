for SERVER_IP in $SERVER_IPS
do

    OPT="-i ${SSH_CRED} -o StrictHostKeyChecking=no"
    SITE="${SSH_CRED_USR}@${SERVER_IP}"

    docker save -o /tmp/image.tar redis-chat:$BUILD_ID
    scp $OPT /tmp/image.tar $SITE:/tmp/image.tar
    rm /tmp/image.tar
    cat web_remote.sh | ssh $OPT $SITE
    
done
echo deployed

