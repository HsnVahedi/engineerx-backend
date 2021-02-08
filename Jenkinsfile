pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // echo 'Building..'
                dir('engineerx') {
                    sh 'ls'
                    script {
                        def backendImage = docker.build("hsndocker/backend:${env.BUILD_ID}")
                        backendImage.push()
                    }
                }
            }
        }
        // stage('Test') {
        //     steps {
        //         echo 'Testing..'
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         echo 'Deploying....'
        //     }
        // }
    }
}