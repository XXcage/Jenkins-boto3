def call() {
  
  pipeline {
      agent any

      stages {
          stage('Hello') {
              steps {
                script {
                  sh 'echo hello world'
                }
                  echo 'Hello World'
              }
          }
      }
  }
}
