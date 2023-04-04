# Proj3

>**Jenkins:** 

<pre>sudo docker run -itd --name jenkins --restart=always \
-p 8080:8080 -p 50000:50000 \
-v "/home/bckp/Desktop/jenkins:/var/jenkins_home" \
-v "/var/run/docker.sock:/var/run/docker.sock" \
jenkins/jenkins:lts-jdk11  
</pre>

>**Sonarqube**
<pre>sudo docker run -d --name sonarqube --restart=always -p 9000:9000 -p 9092:9092 sonarqube</pre>

  `/var/jenkins_home` contains credentials for aws and dockerhub  
      `/.aws` folder for aws , with credentials and config files as per aws format  
      `/.dockerhub` folder for dockerhub, with dockerhub-credentials.properties file that contains username and password  

There are 2 main processes:
* Main pipeline that can be run using shared library function:   
```
@Library("proj3-sharedlib") _   
runBuildDockerfile()
```
or by SCM in jenkins using git and `Jenkinsfile`   
Build a dockerfile, lint test the code and rate it using sonarqube and publish the image to dockerhub.
* Second pipeline that can be run using shared library function:   
```
@Library("proj3-sharedlib") _   
runCronDockerfile()
```   
or by SCM in jenkins using git and `cronJenkinsfile`
