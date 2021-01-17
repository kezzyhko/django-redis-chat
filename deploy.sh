for SERVER_IP in $SERVER_IPS
do

    OPT="-i ${SSH_CRED} -o StrictHostKeyChecking=no"
    SITE="${SSH_CRED_USR}@${SERVER_IP}"

    envsubst < web_remote.sh | ssh $OPT $SITE
    
done
echo deployed $BRANCH_NAME

