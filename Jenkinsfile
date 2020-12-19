pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                docker build --tag django-redis-chat
            }
        }
    }
}
