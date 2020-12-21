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
        stage("test") {
            steps{
                script {
                    app_image.withRun(){
                        c ->
                        sh 'python3 manage.py test'
                    }
                }
            }
        }
    }
}
