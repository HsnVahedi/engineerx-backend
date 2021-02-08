pipeline {
    agent none 
    stages {
        stage('Build Backend Microservice') {
            agent any
            steps {
                // echo 'Building..'
                dir('engineerx') {
                    script {
                        // withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
                            // def backendImage = docker.build("hsndocker/backend:${env.BUILD_ID}")
                            docker.build("hsndocker/backend:${env.BUILD_ID}")
                            // backendImage.push()
                        // }
                    }
                }
            }
        }
        stage('Build Backend Nginx') {
            agent any
            steps {
                dir('nginx') {
                    script {
                            docker.build("hsndocker/backend-nginx:${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Build Backend Postgres') {
            agent any
            steps {
                dir('postgres') {
                    script {
                            docker.build("hsndocker/backend-postgres:${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Build Backend Unittest') {
            agent any
            steps {
                dir('engineerx/dockerfiles/unittest') {
                    script {
                            docker.build("hsndocker/backend-unittest:${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Backend Unittest') {
            agent {
                docker { image 'hsndocker/cluster-unittest:latest' }
            }
            steps {
                sh 'ls'
                sh './kubectl get pods --all-namespaces'
            }
        }
    }
}