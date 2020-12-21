pipeline {
    agent any
    environment {
        SSH = credentials('ssh_key')
    }
    stages {
        stage("build") {
            steps {
                script {
                
                    def app_image = docker.build("redis-chat:${env.BUILD_ID}")
                
                }
            }
        }
        stage("test") {
            steps {
                script {
                    def database_addr = '10.0.0.129'
                    def node_id = '1'
                    docker.image("redis-chat:${env.BUILD_ID}").inside {
                        sh'python3 manage.py test'   
                    }
                   
                }
            }
        }
        
        stage("deploy") {
            steps {
                input(message:"Deploy?", ok:"Yes")
                script {
                    
                    
                    
                    sh 'deployed'
                }
            }
        }
    }
}
