# Proj3

Jenkins:  
- [x] sudo docker run -itd --name jenkins --restart=always \
-p 8080:8080 -p 50000:50000 \
-v "/home/bckp/Desktop/jenkins:/var/jenkins_home" \
-v "/var/run/docker.sock:/var/run/docker.sock" \
jenkins/jenkins:lts-jdk11  

>//apt-get install -y python && apt-get install -y python3-pip  


  /var/jenkins_home contains credentials for aws and dockerhub  
    .aws folder for aws , with credentials and config files as per aws format  
    .dockerhub folder for dockerhub, with dockerhub-credentials.properties file that contains username and password  

- [x] Write a blog
- [x] Make it interesting
- [ ] Publish it
