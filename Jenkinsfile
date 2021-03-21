pipeline {
    agent any
    parameters {
        string(name: 'CLUSTER_NAME', defaultValue: 'engineerx')
        string(name: 'REGION', defaultValue: 'us-east-2')
    }
    environment {
        REGION = "${params.REGION}"
        CLUSTER_NAME = "${params.CLUSTER_NAME}"
    }
    stages {
        stage('Build Backend Images') {
            parallel {
                stage('Backend Microservice') {
                    steps {
                        dir('engineerx') {
                            script {
                                withDockerRegistry([ credentialsId: "dockerhub-repo", url: "" ]) {
                                    def backendImage = docker.build("hsndocker/backend:${env.BUILD_ID}")
                                    backendImage.push()
                                }
                                sh('mv Dockerfile prod.Dockerfile')
                                sh('mv dev.Dockerfile Dockerfile')
                                withDockerRegistry([ credentialsId: "dockerhub-repo", url: "" ]) {
                                    def backendImage = docker.build("hsndocker/backend-dev:${env.BUILD_ID}")
                                    backendImage.push()
                                }
                            }
                        }
                    }
                }
                stage('Backend Nginx') {
                    steps {
                        dir('nginx') {
                            script {
                                withDockerRegistry([ credentialsId: "dockerhub-repo", url: "" ]) {
                                    def backendImage = docker.build("hsndocker/backend-nginx:${env.BUILD_ID}")
                                    backendImage.push()
                                }
                            }   
                        }
                    
                        dir('nginx/integration') {
                            script {
                                withDockerRegistry([ credentialsId: "dockerhub-repo", url: "" ]) {
                                    def integrationImage = docker.build("hsndocker/backend-integration-nginx:${env.BUILD_ID}")
                                    integrationImage.push()
                                }
                            }
                        }
                    }
                }
                stage('Backend Postgres') {
                    steps {
                        dir('postgres') {
                            script {
                                withDockerRegistry([ credentialsId: "dockerhub-repo", url: "" ]) {
                                    def backendImage = docker.build("hsndocker/backend-postgres:${env.BUILD_ID}")
                                    backendImage.push()
                                }
                            }       
                        }
                    }
                }
            }
        }
        stage('Invoke Unittest Pipeline') {
            steps {
                build job: 'backend-test', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}"),
                    string(name: "REGION", value: "${env.REGION}"),
                    string(name: "CLUSTER_NAME", value: "${env.CLUSTER_NAME}")
                ]
            }
        }
        stage('Invoke Integration Test Pipeline') {
            steps {
                build job: 'integration-test', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}")
                ]
            }
        }
        stage('Invoke Setting latest tags') {
            steps {
                build job: 'backend-latest-tag', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}"),
                ]
            }
        }
        stage('Invoke Production Deployment') {
            steps {
                build job: 'aws-deployment', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}"),
                    string(name: "REGION", value: "${env.REGION}"),
                    string(name: "CLUSTER_NAME", value: "${env.CLUSTER_NAME}")
                ]
            }
        }
    }
}
