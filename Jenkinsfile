pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                node {
                
                    def app_image = docker.build("redis-chat:${env.BUILD_ID}")
                
                }
            }
        }
    }
}
