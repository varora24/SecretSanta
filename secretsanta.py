import copy
import random
import smtplib

#store names of people participating
names = ['Name_of_Person1','Name_of_Person2','Name_of_Person3']

#add emails of participants in same order as you did for names
emails = ['email_1', 'email_2','email_3']

#add your email details
sendermail="username"
senderemailpassword="password"

#function to allot names to participants
def make_draws(names):
    my_list = names.copy()
    choose = copy.copy(my_list)
    result = []
    for i in my_list:
        names = copy.copy(my_list)
        names.pop(names.index(i))
        chosen = random.choice(list(set(choose) & set(names)))
        result.append((i, chosen))
        choose.pop(choose.index(chosen))
    return result

#mail function to get names and send out emails
if __name__ == '__main__':
    ss_result = make_draws(names)
    final = zip(ss_result, emails) #this is done so that incase you are participating, you will not be able to see who has drawn whom and ruin the fun

    for x in final:
        subject = "Your Secret Santa Draw"
        mailtext="Hello, "+str(x[0][0])+"\n\n You drew"+str(x[0][1])+"to gift for secret santa !!"

        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.ehlo()
        server.starttls()
        server.login(sendermail, senderemailpassword)
        server.sendmail(sendermail, x, mailtext)
        server.quit()
        print("mail sent to:"+x[1])
        pass


