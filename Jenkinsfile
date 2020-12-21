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
                    def database_addr = '10.0.0.129'
                    def node_id = '1'
                    def app_image = docker.build("redis-chat:${env.BUILD_ID}")
                    app_image.withRun("--env POSTGRES=${database_addr} --env REDIS=${database_addr} --env NODE_ID=${node_id}"){
                        с ->
                        sh'python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 -u manage.py runserver 0.0.0.0:8000 --noreload'
                    }
                }
            }
        }
    }
}
