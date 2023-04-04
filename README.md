# Proj3

>**Jenkins:** 


![alt text][logo]
[logo]: https://user-images.githubusercontent.com/5036939/92243072-ceaf0500-eefb-11ea-8006-1f7034b4167d.png "Jenkins"




<pre>sudo docker run -itd --name jenkins --restart=always \
-p 8080:8080 -p 50000:50000 \
-v "/home/bckp/Desktop/jenkins:/var/jenkins_home" \
-v "/var/run/docker.sock:/var/run/docker.sock" \
jenkins/jenkins:lts-jdk11  
</pre>

>**Sonarqube**
<pre>sudo docker run -d --name sonarqube --restart=always -p 9000:9000 -p 9092:9092 sonarqube</pre>

  >___/var/jenkins_home___ contains credentials for aws and dockerhub  
  >    ___.aws___ folder for aws , with credentials and config files as per aws format  
  >    ___.dockerhub___ folder for dockerhub, with dockerhub-credentials.properties file that contains username and password  


- [ ] tidy
- [ ] submit
