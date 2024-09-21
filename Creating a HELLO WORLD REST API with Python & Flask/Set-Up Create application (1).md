# Set-up : Create application
 - Open a terminal window by using the menu in the editor: Terminal > New Terminal.
new_terminal

 - Change to your project folder, if you are not in the project folder already.
1
 cd /home/project
Copied!
Run the following command to clone the Git repository that contains the starter code needed for this lab, if it doesn't already exist.
1
[ ! -d 'jmgdo-microservices' ] && git clone https://github.com/ibm-developer-skills-network/jmgdo-microservices.git
Copied!
Change to the directory jmgdo-microservices/CRUD to start working on the lab.
1
cd jmgdo-microservices/CRUD
Copied!
List the contents of this directory to see the artifacts for this lab.
1
ls
Copied!
Run the following command on the terminal to install the packages that are required.
1
python3 -m pip install flask flask_cors