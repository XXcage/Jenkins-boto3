# Proj3

Jenkins:
//apt-get install -y python && apt-get install -y python3-pip
-v "/home/bckp/Desktop/jenkins:/var/jenkins_home" \
-v "/var/run/docker.sock:/var/run/docker.sock" \

  /var/jenkins_home contains credentials for aws and dockerhub
    .aws folder for aws , with credentials and config files as per aws format
    .dockerhub folder for dockerhub, with dockerhub-credentials.properties file that contains username and password
