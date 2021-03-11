pipeline {
    agent any
    stages {
        stage('Build Backend Images') {
            parallel {
                stage('Build Backend Microservice') {
                    steps {
                        dir('engineerx') {
                            script {
                                withDockerRegistry([ credentialsId: "dockerhub-repo", url: "" ]) {
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
                stage('Build Backend Postgres') {
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
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}")
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
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}")
                ]
            }
        }
        stage('Invoke Production Deployment') {
            steps {
                build job: 'deployment', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}")
                ]
            }
        }
    }
}
