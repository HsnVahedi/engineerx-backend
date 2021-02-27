pipeline {
    agent any
    stages {
        stage('Build Backend Microservice') {
            steps {
                sh 'cat engineerx/unittest.sh'
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
	stage('Build Ingress Nginx') {
            steps {
                dir('minikube/ingress') {
                    script {
                        withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
                            def backendImage = docker.build("hsndocker/minikube-ingress:${env.BUILD_ID}")
                            backendImage.push()
                        }
                    }
                }
            }
        }
        // stage('Build Backend Unittest') {
        //     steps {
        //         dir('engineerx/dockerfiles/unittest') {
        //             script {
        //                 withDockerRegistry([ credentialsId: "dockerhub-credentials", url: "" ]) {
        //                     def backendImage = docker.build("hsndocker/backend-unittest:${env.BUILD_ID}")
        //                     backendImage.push()
        //                 }
        //             }
        //         }
        //     }
        // }
        stage ('Invoke Unittest Pipeline') {
            steps {
                build job: 'engineerx-backend-unittest', parameters: [
                    string(name: "BACKEND_VERSION", value: "${env.BUILD_ID}")
                ]
            }
        }
    }
}
