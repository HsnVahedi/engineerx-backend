pipeline {
    agent any

    stages {
        stage('Build Backend Microservice') {
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
            steps {
                dir('nginx') {
                    script {
                            docker.build("hsndocker/backend-nginx:${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Build Backend Postgres') {
            steps {
                dir('postgres') {
                    script {
                            docker.build("hsndocker/backend-postgres:${env.BUILD_ID}")
                    }
                }
            }
        }
        stage('Build Backend Unittest') {
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
                dir('kubectl') {
                    sh 'ls'
                    sh './kubectl get pods --all-namespaces'
                }
            }
        }
    }
}