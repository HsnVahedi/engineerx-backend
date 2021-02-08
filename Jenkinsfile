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
        stage('Deploy Unittest') {
            agent {
                docker {
                    image 'hsndocker/cluster-unittest:latest'
                    args '-u root:root'
                }
            }
            steps {
                sh 'pwd'
                sh 'cd /root'
                sh 'ls -a'
            }
        } 
    }
}