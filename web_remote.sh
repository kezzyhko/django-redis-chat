sudo docker load -i /tmp/image.tar
sudo docker stop django-redis-chat
sudo docker rm django-redis-chat
sudo docker run -p 80:8000 -v webapp:/web --name django-redis-chat -d --env POSTGRES=$DATABASE_ADDR --env REDIS=$DATABASE_ADDR --env NODE_ID=$NODE_ID redis-chat:$BUILD_ID bash -c "python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 -u manage.py runserver 0.0.0.0:8000 --noreload"
rm /tmp/image.tar
