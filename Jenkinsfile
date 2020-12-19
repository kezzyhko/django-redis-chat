pipeline {
    agent any
    stages {
        stage("build") {
            step {
                node {
                
                    def app_image = docker.build("redis-chat:${env.BUILD_ID}")
                
                }
            }
        }
    }
}
