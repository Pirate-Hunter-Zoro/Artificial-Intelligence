# About
This is a repository of various artificial intelligence algorithm implementations. To see them in action, you'll want to run each '.ipynb' notebook and observe the output. My instructions apply only to Mac and Linux users - Windows users are unfortunately on their own in getting this code to run on their machines!

## Instructions
I would highly recommend using VSCode to experiment with these notebooks should one choose to do so. Download here: https://code.visualstudio.com/download<br>
These extensions are also MAD useful: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter<br>
These instructions assume that one has "pip" installed on their pc. If that is not the case, see the following link for instructions on how to install pip: https://pip.pypa.io/en/stable/installation/<br>
I'm also going to assume you have Python installed:
https://www.python.org/downloads/<br>
Finally, I'm assuming you have "git" installed:
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git<br>
To run these notebooks, perform the following tasks, which will include cloning this repository and creating a Python virtual environment containing the necessary libraries:
1. Navigate to a folder on your computer where you would like to clone this project via the command line and run the following command:<br>
   ```git clone https://github.com/Pirate-Hunter-Zoro/Artificial-Intelligence.git```<br>
This will create a folder called "Artificial-Intelligence" in your current folder. 
2. Navigate into this folder.<br>
   ```cd Artificial-Intelligence```
3. Create a python virtual environment named "ai_env" (or whatever you want to call it) via the following command:<br>
   ```python -m venv ai_env```
4. Activate the virtual environment:<br>
   ```source ai_env/bin/activate```
5. Install the necessary Python libraries:<br>
   ```pip install -r requirements.txt```
6. At this point feel free to open the repository in VSCode:<br>
   ```code .```
7. You should be able to open any notebook and navigate your mouse near the top right to click on the "Select Kernel" box, choose "Python Environments", and select the virtual environment you just created as a kernel:
![](images/Kernel_Select_1.png)
![](images/Kernel_Select_2.png)
8. Now have fun running the cells!

## Useful Note
To write all of the requirements in the Python virtual library into "requirements.txt", run the following command:<br>
```pip freeze > requirements.txt```
