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
            environment {
	        SSH_CRED = credentials('aws-key')
	    }
            steps {
                input(message:"Deploy?", ok:"Yes")
                sh'ssh -i $SSH_CRED -o StrictHostKeyChecking=no $SSH_CRED_USR@18.219.119.51 touch abcd'
            }
        }
    }
}
