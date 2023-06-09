def call() {    
    pipeline {
        agent any
        triggers {
            cron('*/5 * * * *')
        }
        environment {
            imageName = 'rzlinux0/proj3'
            jobName = 'BuildDockerfileRun-Jenkinsfile'
        }
        stages {
            stage('Get Last Successful Build') {
                steps {
                    script {
                        def permalinksFile = "../../jobs/${env.jobName}/builds/permalinks"
                        env.lastSuccessfulBuildNum = sh(script: "cat ${permalinksFile} | grep lastSuccessfulBuild | awk '{print \$2}'", returnStdout: true).trim()
                        env.latestImage = "${env.imageName}:${env.lastSuccessfulBuildNum}"      
                    }
                }
            }
            stage('DockerHub Login') {
                steps {
                    script {
                        // Read the DockerHub credentials from the properties file
                        def dockerhubCredentials = readFile('/var/jenkins_home/.dockerhub/dockerhub-credentials.properties').trim()
                        // Split the contents of the file into an array of lines
                        def credentials = dockerhubCredentials.tokenize("\n")
                        // Set the DockerHub username and password as environment variables
                        env.DOCKERHUB_USERNAME = credentials[0].trim().split("=")[1].trim()
                        env.DOCKERHUB_PASSWORD = credentials[1].trim().split("=")[1].trim()
                        sh "docker login -u ${env.DOCKERHUB_USERNAME} -p ${env.DOCKERHUB_PASSWORD} https://index.docker.io/v1/"

                    }
                }
            }
            stage('Run Latest Docker Image') {
                steps {
                    script {
                        sh "docker pull ${env.latestImage}"
                        sh "docker run ${env.latestImage}"
                    }
                }
            }
        }
    }
 

}
