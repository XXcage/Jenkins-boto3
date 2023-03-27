pipeline {
  agent any

  stages {
    stage('Clone Git Repo') {
      steps {
        git 'https://github.com/XXcage/Proj3.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          docker.build('proj3:latest', '.')
        }
      }
    }

    stage('Lint Test') {
        steps {
            script {
            def lint_output = docker.image('my-image:latest').inside {
                sh 'pylint Linting.py'
            }

                if (lint_output.contains('Your code has been rated at 10.00')) {
                    echo 'Lint test passed!'
                } else {
                echo "WARNING: Lint test failed. Lint output: \n${lint_output}"
                }
            }
        }
    }
    
    stage('Push Docker Image to Dockerhub') {
      steps {
        script {
          withCredentials([[
              $class: 'UsernamePasswordMultiBinding',
              credentialsId: 'my-dockerhub-creds',
              usernameVariable: 'DOCKER_USERNAME',
              passwordVariable: 'DOCKER_PASSWORD'
          ]]) {
            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
              docker.image('my-image:latest').push("${env.DOCKER_USERNAME}/my-image:latest")
            }
          }
        }
      }
    }
  }
}
