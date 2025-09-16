# Python Packages Required To Run The Tests -

The project root location contains the requirment.txt file which lists all the packages required to run the test after cloning the repositiory in the local system. Base python version is ##3.13.XX##.
Few of the major libraries that are used in this project are:

1) pip install requests
3) pip install json
4) pip install jsonpath
5) pip install pytest
6) pip install pytest-xdist
7) pip install pytest-html
8) pip install pytest-json-report
9) pip install pytest-cov
10) pip install openpyxl
11) pip install allure-pytest



# Setting Up GIT For Source Code Management -

1) Create a remote repository by login to GitHub on chrome. 
   Note the HTTPS URl to connect to it - git@github.com:XYZ/ABC.git

2) Now go to the folder where all your automation code is written.
   Create a local repository by initializing git = git init

3) Check status of untracked file by running below command - 
   git status
4) Add these files to staging area - 
   git add <filename> or git add .
5) Commit these changes -
   git commit -m "Updating project Files"
6) Then connect the local and remote repository by running the command - 
   git remote add origin git@github.com:XYZ/ABC.git
7) Set the branch to which code is to be pushed - 
   git branch -M main
8) Finally push your code using below command - 
   git push -u origin main

# Setting Up Jenkins On Local Machine -

1) Download Java on your local machine.
2) Download WAR file for Jenkins.
3) Go to the WAR file location, launch command prompt and run in command prompt = java -jar jenkins.war -httpPort=9090 (By default port is 8080)

4) Look for initialPassword in folder - C:\Users\User\.jenkins\secrets\initialAdminpassword
   Config file is there to change jenkins config.

5) Once all plugins are downloaded and installed, user will get screen to create username / password.
6) Create and login with the same.

7) Jenkins URL - https://localhost:9090

8) Once Jenkin is set up - 

    a) Under Manage Jenkins > Tools - 
        1) Set Java path - provide systems JDK path - C:\Program Files\Java\jdk-17
        2) Set GIT path - provide git.exe file path - C:\Program Files\Git\bin (Change it to C:/Program Files/Git/bin/git.exe)

    b) Under Manage Jenkins > System -

        1) Set Python path - 
           Python_Home - C:\Users\User\AppData\Local\Programs\Python\Python313;C:\Users\User\AppData\Local\Programs\Python\Python313\Scripts
           Python_Scripts - C:\Users\User\AppData\Local\Programs\Python\Python313\Scripts
     And add Chrome, Gecko and Edge driver to Python script folder - C:\Users\User\AppData\Local\Programs\Python\Python313\Scripts

    c) Setup Allure reporting on jenkins - 
       1) Manage Jenkins > plugins > allure
       2) Download allure command line from google > zip file (https://allurereport.org/docs/install-for-windows/)
       3) Manage Jenkins > Tools > At the bottom add Allure and its path from your system

# Troubleshooting - If Jenkins is showing error as below while starting  -

2025-09-09 07:40:50.078+0000 [id=1]     INFO    winstone.Logger#logInternal: Jetty shutdown successfully
java.io.IOException: Failed to start Jetty
        at Jenkins Main ClassLoader//winstone.Launcher.<init>(Launcher.java:192)
        at Jenkins Main ClassLoader//winstone.Launcher.main(Launcher.java:488)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.base/java.lang.reflect.Method.invoke(Method.java:568)
        at executable.Main.main(Main.java:335)
Caused by: java.io.IOException: Failed to bind to 0.0.0.0/0.0.0.0:8080
        at Jenkins Main ClassLoader//org.eclipse.jetty.server.ServerConnector.openAcceptChannel(ServerConnector.java:349)
        at Jenkins Main ClassLoader//org.eclipse.jetty.server.ServerConnector.open(ServerConnector.java:313)
        at Jenkins Main ClassLoader//org.eclipse.jetty.server.Server.lambda$doStart$0(Server.java:571)
        at java.base/java.util.stream.ForEachOps$ForEachOp$OfRef.accept(ForEachOps.java:183)
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197)
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179)
        at java.base/java.util.Spliterators$ArraySpliterator.forEachRemaining(Spliterators.java:992)
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509)
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499)
        at java.base/java.util.stream.ForEachOps$ForEachOp.evaluateSequential(ForEachOps.java:150)
        at java.base/java.util.stream.ForEachOps$ForEachOp$OfRef.evaluateSequential(ForEachOps.java:173)
        at java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)
        at java.base/java.util.stream.ReferencePipeline.forEach(ReferencePipeline.java:596)
        at Jenkins Main ClassLoader//org.eclipse.jetty.server.Server.doStart(Server.java:567)
        at Jenkins Main ClassLoader//org.eclipse.jetty.util.component.AbstractLifeCycle.start(AbstractLifeCycle.java:93)
        at Jenkins Main ClassLoader//winstone.Launcher.<init>(Launcher.java:188)
        ... 6 more
Caused by: java.net.BindException: Address already in use: bind
        at java.base/sun.nio.ch.Net.bind0(Native Method)
        at java.base/sun.nio.ch.Net.bind(Net.java:555)
        at java.base/sun.nio.ch.ServerSocketChannelImpl.netBind(ServerSocketChannelImpl.java:337)
        at java.base/sun.nio.ch.ServerSocketChannelImpl.bind(ServerSocketChannelImpl.java:294)
        at Jenkins Main ClassLoader//org.eclipse.jetty.server.ServerConnector.openAcceptChannel(ServerConnector.java:344)
        ... 21 more

Option 1: Find and Stop the Process Using Port 8080.

    On Windows:
    Open Command Prompt as Administrator.

    Run:
    netstat -aon | findstr :8080

    You’ll see something like:
    TCP    0.0.0.0:8080     0.0.0.0:0     LISTENING     1234

    The number at the end is the PID (e.g., 1234).

    Find the application using that PID:
    tasklist /FI "PID eq 1234"

    Stop it (if safe to do so):
    taskkill /PID 1234 /F

Option 2: Run jenkins on a different port number.
    In this case just try starting your jenkins on a different port. Use below command for the same:

    java -jar jenkins.war -httpPort=<port-number>

# Setting Up Allure For Generating Report -

1) Check for Java = java --version
2) Download Node.js 64 bit version from Google, executable with msi version should be downloaded, complete the setup.
3) Install allure command line tool by redirecting to C:\Windows\System32\cmd.exe (Where Node.js is installed) launch cmd and fire the below command -
   npm install -g allure-commandline --save-dev

4) To be sure, type in allure and see if help option are displayed.

5) Commands to run for generating allure report -

   pytest -s --alluredir="path of report folder" - To run test suite and generate JSON report
   allure serve "path of report folder" - To generate HTML reports

