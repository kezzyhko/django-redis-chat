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
				DATABASE_ADDR = '10.0.0.1'
				NODE_ID = 1
				SERVER_IPS = "18.217.216.221 10.0.0.9"
	    	}
            steps {
                input(message:"Deploy?", ok:"Yes")
				sh "chmod +x -R ${env.WORKSPACE}"
				sh './deploy.sh'
            }
        }
    }
}
