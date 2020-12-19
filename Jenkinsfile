pipeline {
    agent any
    stages {
        stage("build") {
            steps {
                script {
                
                    def app_image = docker.build("redis-chat:${env.BUILD_ID}")
                
                }
            }
        }
    }
}
