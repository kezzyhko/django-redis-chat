
OPT="-i ${SSH_CRED} -o StrictHostKeyChecking=no"
SITE="${SSH_CRED_USR}@18.219.119.51"

docker save -o /tmp/image.tar redis-chat:$BUILD_ID
scp $OPT /tmp/image.tar $SITE:/tmp/image.tar
rm /tmp/image.tar
ssh $OPT $SITE sudo docker load -i /tmp/image.tar
ssh $OPT $SITE sudo docker stop django-redis-chat
ssh $OPT $SITE sudo docker rm django-redis-chat
ssh $OPT $SITE sudo docker run -p 80:8000 -v webapp:/web --name django-redis-chat -d --env POSTGRES=$DATABASE_ADDR --env REDIS=$DATABASE_ADDR --env NODE_ID=$NODE_ID django-redis-chat:$BUILD_ID bash -c "python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 -u manage.py runserver 0.0.0.0:8000 --noreload"

ssh $OPT $SITE rm /tmp/image.tar
echo deployed

