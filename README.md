# django-redis-chat
A simple web chat app with registration, that operates through redis

It was initially a part of another project - [Vulnbox with OWASP Top 10 2017 vulnerabilities](https://github.com/kezzyhko/vulnexamples)



## Example of usage

Here is and [example of docker-compose config](docker-compose.yaml).

Basically, this project needs:
* a web app running on 8000 port
* redis running on 6379 port
* PostgreSQL database running on 5432

Ports, of course, can be changed through the config files
