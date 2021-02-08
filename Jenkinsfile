pipeline {
    agent none 
    stages {
        stage('Build Backend Microservice') {
            agent any
            steps {
                // echo 'Building..'
                dir('engineerx') {
                    script {
                        withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
                            def backendImage = docker.build("hsndocker/backend:${env.BUILD_ID}")
                            backendImage.push()
                        }
                    }
                }
            }
        }
        stage('Build Backend Nginx') {
            agent any
            steps {
                dir('nginx') {
                    script {
                        withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
                            def backendImage = docker.build("hsndocker/backend-nginx:${env.BUILD_ID}")
                            backendImage.push()
                        }
                    }
                }
            }
        }
        stage('Build Backend Postgres') {
            agent any
            steps {
                dir('postgres') {
                    script {
                        withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
                            def backendImage = docker.build("hsndocker/backend-postgres:${env.BUILD_ID}")
                            backendImage.push()
                        }
                    }
                }
            }
        }
        stage('Build Backend Unittest') {
            agent any
            steps {
                dir('engineerx/dockerfiles/unittest') {
                    script {
                        withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
                            def backendImage = docker.build("hsndocker/backend-unittest:${env.BUILD_ID}")
                            backendImage.push()
                        }
                    }
                }
            }
        }
        stage ('Invoke Unittest Pipeline') {
            steps {
                build job: 'engineerx-backend-unittest', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}")
                ]
            }
        }
    }
}