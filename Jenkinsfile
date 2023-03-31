pipeline {
  agent any
  environment {
    //DOCKER_HOST = "unix:///var/run/docker.sock"
    IMAGE_NAME = 'rzlinux0/proj3:${BUILD_NUMBER}'
    awsPath = "/var/jenkins_home/.aws"
  }
  stages {
    stage('Checkout+aws creds') {
      steps {
        cleanWs()
        sh 'git clone -b main https://github.com/XXcage/Proj3.git'
        sh "cp -r ${env.awsPath} Proj3/"

      }
    }
    stage('Build Docker Image') {
      steps {
        dir('Proj3') {
          script {
            sh "docker build -t ${env.IMAGE_NAME} ."
          }      
        }
      }
    }

    stage('DockerHub Login') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHubID', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
        }
      }
    }
    stage('Push Docker Image') {
      steps {
        sh "docker push ${env.IMAGE_NAME}"
      }
    }
    stage('Run Docker Image') {
      steps {
        script {
          sh "docker run --rm ${env.IMAGE_NAME}"
        }
      }
    }    
  }
}
