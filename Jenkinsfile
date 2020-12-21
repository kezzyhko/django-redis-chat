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
                    docker.image("redis-chat:${env.BUILD_ID}").withRun(){
                        c ->
                        sh 'python3 manage.py test'
                    }
                }
            }
        }
    }
}
