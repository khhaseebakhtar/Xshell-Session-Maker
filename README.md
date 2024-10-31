# **Welcome to the Xshell Session Make page that... blah blah blah .. ** <br />
Being a Network Engineer, I can tell you—no matter what fancy title you’ve got, setting up SSH sessions is always a pain in the A**. Especially when you’re switching laptops, changing jobs, or just trying to remember which device is which! But don’t worry, this tool’s got you covered. Just drop your device IPs into an Excel file, make sure your credentials work, and BAM! Instant Xshell sessions, no hassle.<br />

(And yeah, I totally used ChatGPT to polish these lines because, just like my job, my English is aslo shi.. well, let’s just say it needed a firm smack on the back) why the hell are you still reading sll this , read the guidelines and go fix your crappy job!<br /><br />


**1-** Make an Xshell session that is working fine , save the username and password for the session. <br />
<br />
![image](images/1.png)<br />
<br />
<br />
<br />
**2-** Open that Xshell session file in note pad and search for 'Host=' , this line will look like this **Host= <ip_of_your_device>**<br />
![image](images/2.png)<br />
<br />
<br />
<br />
**3-** Remove the IP and store first part (till 'Host=') in 'part1' variable of the main.py file<br />
<br />
![image](images/3.png)<br />
<br />
<br />
<br />
**4-** Save the remaining session data in 'part2' variable of main.py file<br />
<br />
![image](images/4.png)<br />
<br />
<br />
<br />
**5-** Copy your excel device list (only .xlsx) in project folder (where the main.py is stored)<br />
<br />
![image](images/5.png)<br />
<br />
<br />
<br />
**6-** Your device list must have an 'IP' column header, under which all the device IPs are mentioned,order of columns does not matter as long as there is an IP column<br />
**7-** Device list can optionally have 'Hostname'  and 'City' columns as well to store sessions in relevant city folders <br />
<br />
![image](images/6.png)<br />
<br />
<br />
<br />
**8-** Run the main.py, the output session files will be stored in Sessions_files folders<br />
![image](images/8.png)<br />
<br />
<br />
<br />
I mean whats the point of having a public github repo if i'm not receving life threats, Go ahead:  Drop your creative susidal ideas at **khwajahaseeb@yahoo.com** <br />
