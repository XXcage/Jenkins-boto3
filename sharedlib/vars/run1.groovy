def call() {
    pipeline {
        agent any
        stages {
            stage('Run1 Function') {
                steps {
                    echo 'Run1 success'
                }
            }
        }
    }
}
