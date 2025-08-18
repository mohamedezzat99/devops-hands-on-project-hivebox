node {
    String containerTag = 'myapp-hivebox'

    stage('Build') {
        checkout scm
        sh "docker build -t ${containerTag} ."
    }
    stage('Test') {
        sh "docker run --rm ${containerTag} pytest"
    }
    stage('Deploy') {
        withCredentials([
            usernamePassword(credentialsId: 'docker-hub-repo', passwordVariable: 'PASS', usernameVariable: 'USER')
            ]) {
            sh "echo ${PASS} | docker login --username ${USER} --password-stdin"
        }
        sh "docker push ${containerTag}"
    }
}
