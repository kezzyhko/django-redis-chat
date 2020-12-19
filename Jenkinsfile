pipeline {
    agent any
    stages {
        stage("buikd") {
            steps {
                docker build --tag django-redis-chat
            }
        }
    }
}
