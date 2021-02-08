pipeline {
    agent any

    stages {
        stage('Build Backend Microservice') {
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
    }
}