node {
    String containerTag = 'myapp-hivebox'
    Boolean testResult = false

    stage('Build') {
        sh "docker build -t ${containerTag} ."
        sh "docker run -p 8000:8000 ${containerTag}"
    }
    stage('Test') {
        testResult = sh(script:'pytest', returnStdout:true)
    }
    stage('Deploy') {
        if (testResult) {
            withCredentials([
                usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')
                ]) {
                sh "echo ${PASS} | docker login --username ${USER} --password-stdin"
            }
            sh "docker push ${containerTag}"
        }
    }
}
