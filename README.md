# ASST - Automated Society Security Task

For our final year project, considering this covid-19 pandemic, we wanted to build a contactless tool that could curb the spread of the virus and to identify any potential carriers so that we can avoid its spread by taking necessary measures to keep society safe. Our projects name is automated society security task, which is an IoT based security system. We've used raspberry pi for this project. The authentication process is done using facial recognition and thus the whole security process is touchless which helps to curb the spread of covid. Visitor temperature is also recorded using mlx infrared temperature sensor. So if the temperature of the visitor is above the threshold,  an alert mail is sent to the society head so that virus spread can be efficiently tracked. We've also built a web app using Django and created rest API endpoints. Information like visitor name, entry time and their temperature recorded from our raspberry pi is stored in our backend by making post requests from raspberry to the rest API endpoints. We have also implemented an authentication system in our web app so that society members and security can log in and view visitor information.

[Website](https://asst-tech.herokuapp.com/login?next=/)

[Technical paper](https://github.com/ItsRish06/ASST/blob/main/ASST.pdf)


## Hardware used -

  - Raspberry pi 3 module
  - Ultrasonic sensor 
  - Raspberry pi 3 camera module
  - Infrared temperature sensor
  - LCD display

## Technologies used - 

  - OpenCV
  - Django  
  - HTML / CSS (SCSS)

## Testing -

TDD based automated tests are written using Selenium and Nunit.Extent Report is used for logging and generating html reports.

Page Object Model, also known as POM, is used in this project. POM is a design pattern in Selenium that creates an object repository for storing all web elements.

  ### Technologies used-
    - Selenium
    - NUnit
    - Extent Report
    
 ### Report Screenshots -
 ![Report1](./project_imgs/asst-test-report-ss.png)
 ![Report2](./project_imgs/asst-test-report-ss2.png)

## Flowchart

![flowchart](./project_imgs/Flowchart.png)


### Face recognition flowchart
![faceflow](./project_imgs/faceflow.png)

## Website screenshots
![1](./project_imgs/web1.png)
![2](./project_imgs/web2.png)
![3](./project_imgs/web3.png)
![4](./project_imgs/web4.png)
![5](./project_imgs/web5.png)
![7](./project_imgs/web7.png)







