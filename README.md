# **Welcome to the Xshell Session Make page that... blah blah blah .. ** <br />
Being a Network Engineer, I can tell you—no matter what fancy title you’ve got, setting up SSH sessions is always a pain in the A**. Especially when you’re switching laptops, changing jobs, or just trying to remember which device is which! But don’t worry, this tool’s got you covered. Just drop your device IPs into an Excel file, make sure your credentials work, and BAM! Instant Xshell sessions, no hassle.<br />

(And yeah, I totally used ChatGPT to polish these lines because, just like my job, my English is aslo shi.. well, let’s just say it needed a firm smack on the back) why the hell are you still reading sll this , read the guidelines and go fix your crappy job!<br /><br />


**1-** Make an Xshell session that is working fine , save the username and password for the session. <br />
<br />
![image](https://github.com/user-attachments/assets/7ac7dc3b-9c70-4202-8cd6-e4cf035363b5)<br />
<br />
<br />
<br />
**2-** Open that Xshell session file in note pad and search for 'Host=' , this line will look like this **Host= <ip_of_your_device>**<br />
![image](https://github.com/user-attachments/assets/ea70653f-a811-495e-beb5-6f8769e350e7)<br />
<br />
<br />
<br />
**3-** Remove the IP and store first part (till 'Host=') in 'part1' variable of the main.py file<br />
<br />
![image](https://github.com/user-attachments/assets/ee196d2b-fe24-4101-b8c2-3dd5cc47348d)<br />
<br />
<br />
<br />
**4-** Save the remaining session data in 'part2' variable of main.py file<br />
<br />
![image](https://github.com/user-attachments/assets/363d0083-572f-4cb0-bca1-c2fe77394794)<br />
<br />
<br />
<br />
**5-** Copy your excel device list (only .xlsx) in project folder (where the main.py is stored)<br />
<br />
![image](https://github.com/user-attachments/assets/58f2b708-a653-45c1-bcbd-94b2ba79a522)
<br />
<br />
<br />
**6-** Your device list must have an 'IP' column header, under which all the device IPs are mentioned,order of columns does not matter as long as there is an IP column<br />
**7-** Device list can optionally have 'Hostname'  and 'City' columns as well to store sessions in relevant city folders <br />
<br />
![image](https://github.com/user-attachments/assets/9a54531b-b667-4201-b9dc-bd68fc2019a4)<br />
<br />
<br />
<br />
**8-** Run the main.py, the output session files will be stored in Sessions_files folders<br />
    ![image](https://github.com/user-attachments/assets/edd9a314-9458-4e8c-919d-62302c9f7875)
<br />
<br />
<br />
I mean whats the point of having a public github repo if i'm not receving life threats, Go ahead:  Drop your creative susidal ideas at **khwajahaseeb@yahoo.com** <br />
