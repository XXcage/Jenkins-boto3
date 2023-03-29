def call() {
  pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                cleanWs()
                echo 'Hello World'
            }
        }
        

        stage('Checkout') {
            steps {
                sh 'git clone -b main https://github.com/XXcage/Proj3.git'
            }
        }
        stage('Build') {
            steps {
                dir('Proj3') {
                  //sh 'pip install boto3'
                  //sh 'python3 ec2listbuckets.py'
                  sh 'pip show boto3'
                  sh 'python3 ec2InstanceDetails-json.py'
                }
                
            }
        }
    }
  }
}



