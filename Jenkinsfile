pipeline {
  agent any
  environment {
    IMAGE_NAME = 'rzlinux0/proj3:${BUILD_NUMBER}'
    awsPath = "/var/jenkins_home/.aws"
  }
  stages {
    stage('Checkout+aws creds') {
      steps {
        cleanWs()
        sh 'git clone -b main https://github.com/XXcage/Proj3.git'

      }
    }
    stage('Build Docker Image') {
      steps {
        //copy aws creds for docker to be able to run .py using boto
        sh "cp -r ${env.awsPath} Proj3/"
        dir('Proj3') {
          script {
            sh "docker build -t ${env.IMAGE_NAME} ."
          }      
        }
      }
    }

    stage('DockerHub Login and push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHubID', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
          sh "docker push ${env.IMAGE_NAME}"
        }
      }
    }

//     stage('Run cat pylint output') {
//       steps {
//         script {
//           sh "docker run ${env.IMAGE_NAME} cat pylint-output.txt"
//         }
//       }
//     }

  }
}
