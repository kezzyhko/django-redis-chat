pipeline {
    agent any
    stages {
        stage("buikd") {
            steps {
                sh 'docker build https://github.com/kezzyhko/django-redis-chat.git#main --tag django-redis-chat'
            }
        }
    }
}
