import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

   
server.login('mauryamanisha.9555@gmail.com', "iwifaiogbbposthi")

subject = "CHALLENGES COMPLETION"
  
body = " Name: Manisha Maurya \n Email: manisha.2125csit1173@kiet.edu\n Ph.No:9555840324 \n B.Tech IT \n 2nd year \n2100290110086\n photo: https://drive.google.com/file/d/1UGH0qilMAJiVifj9YVj10lA9xa6aTe8x/view?usp=drivesdk \n Gitrepo:https://github.com/manisha9555/challengecabin"

msg = f"subject: {subject} \n\n\n {body}"

server.sendmail(
        'mauryamanisha.9555@gmail.com',
        'sales@cabin4j.com',
    msg
    )
print('Message is sent succesfully!')


