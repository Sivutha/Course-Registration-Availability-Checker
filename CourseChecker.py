from urllib.request import Request
import bs4, requests, smtplib, sys, time

while True: 

    args = sys.argv[3: ]
    email = sys.argv[1]
    password = sys.argv[2]
    for i in args:

        url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=COMM&course='+ i
        res = requests.get(url)
        res.raise_for_status()
        print(res.status_code)

        # f = open("test", "w")r
        # f.write(res.text)
        # f.close()

        soup = bs4.BeautifulSoup(res.text,"html.parser")

        elems0 = soup.find_all(string="Full") + soup.find_all(string="Restricted") + soup.find_all(string="STT") 
        elems1 = soup.find_all(string="Lecture")
        # print(len(elems0))
        # print(len(elems1))

        if(len(elems1) - len(elems0) != 0): 
            # print("send email")

            course = "COMM " + i

            subject = "Subject: " + course + " Seat Open" 

            conn = smtplib.SMTP("smtp.gmail.com",587)

            conn.ehlo()
            conn.starttls()
            conn.login(email, password) #if google, app specific password
            conn.sendmail(email, email, subject)
            conn.quit()


    time.sleep(3600)