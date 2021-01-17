for SERVER_IP in $SERVER_IPS
do

    OPT="-i ${SSH_CRED} -o StrictHostKeyChecking=no"
    SITE="${SSH_CRED_USR}@${SERVER_IP}"

    ssh $OPT $SITE sudo docker stop django-redis-chat && sudo docker rm django-redis-chat:$BUILD_ID
    ssh $OPT $SITE sudo docker build https://github.com/kezzyhko/django-redis-chat.git#$BRANCH_NAME --tag django-redis-chat
    ssh $OPT $SITE sudo docker run -p 80:8000 -v webapp:/web --name django-redis-chat -d --env POSTGRES=$DATABASE_ADDR --env REDIS=$DATABASE_ADDR --env NODE_ID=$NODE_ID redis-chat:$BUILD_ID bash -c "python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 -u manage.py runserver 0.0.0.0:8000 --noreload"
    
done
echo deployed $BRANCH_NAME

