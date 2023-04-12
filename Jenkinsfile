pipeline {
    agent any
    environment {
      IMAGE_NAME = 'rzlinux0/proj3-consul:${BUILD_NUMBER}'
  //    awsPath = "/var/jenkins_home/creds/.aws"
  //    awsPath = "/y/jenkins/creds/.aws"
    }
    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                sh 'git clone -b Consul-Integration https://github.com/XXcage/Proj3.git'
            }
        }
        stage('Retrieve AWS credentials from Consul') {
            steps {
                script {
                    sh "ls -an"
                    sh "pwd"
                    // Retrieve AWS values from Consul
                    def aws_access_key_id = sh(returnStdout: true, script: 'consul kv get -http-addr=http://172.17.0.4:8500 aws/access_key_id').trim()
                    def aws_secret_access_key = sh(returnStdout: true, script: 'consul kv get -http-addr=http://172.17.0.4:8500 aws/secret_access_key').trim()
                    def aws_region = sh(returnStdout: true, script: 'consul kv get -http-addr=http://172.17.0.4:8500 aws/region').trim()
                    def aws_output = sh(returnStdout: true, script: 'consul kv get -http-addr=http://172.17.0.4:8500 aws/output').trim()
        
                    // Write values to aws files
                    dir('.aws') {
                        writeFile file: 'credentials', text: "[default]\naws_access_key_id=${aws_access_key_id}\naws_secret_access_key=${aws_secret_access_key}\n"
                        writeFile file: 'config', text: "[default]\nregion=${aws_region}\noutput=${aws_output}\n"
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {

                //copy aws creds for docker to be able to run .py using boto
                //sh "cp -r ${env.awsPath} Proj3/"
                sh "ls -an"
                sh "pwd"
                sh "cp -r /.aws Proj3/"
                dir('Proj3') {
                    script {
                    sh "docker build -t ${env.IMAGE_NAME} ."
                    }      
                }
            }
        }
        stage('DockerHub login and push') {
            steps {
                script {
                    // Fetch DockerHub username and password from Consul
                    env.DOCKERHUB_USERNAME = sh(returnStdout: true, script: 'consul kv get -http-addr=http://172.17.0.4:8500 dockerhub/DOCKER_USERNAME').trim()
                    env.DOCKERHUB_PASSWORD = sh(returnStdout: true, script: 'consul kv get -http-addr=http://172.17.0.4:8500 dockerhub/DOCKER_PASSWORD').trim()
                    sh "docker login -u ${env.DOCKERHUB_USERNAME} -p ${env.DOCKERHUB_PASSWORD} https://index.docker.io/v1/"
                    // sh "docker push ${env.IMAGE_NAME}"
                }
            }
        }
  
    }
  }
  
