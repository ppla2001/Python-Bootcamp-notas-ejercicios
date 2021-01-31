import smtplib 
#para gmail
smtp_object = smtplib.SMTP('smtp.gmail.com',port=587) #si port me da error puedo probar con port 465 y si eso tampoco funciona puedo probar de no pasarle port number
#establish connection
smtp_object.ehlo() #me tiene que devolver un codigo q basicamente connection successful
#para que sea encrypted
smtp_object.starttls() #esto es si uso port 587, si uso port 465 me puedo saltear este paso
#password = input('Password:') asi me pueden ver la contra si me estan mirando la computadora, en cambio lo q puedo hacer:
import getpass
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')#la password tiene q ser app generated password,no mi password del mail en si #getpass.getpass hace que no salga los caracteres, en este caso me salio invisible el texto, pueden salir las pelotitas
smtp_object.login(email,password) #me deberia decir accepted
from_address = email
to_address = email #me voy a mandar un mail a mi mismo
subject = input('Subject del mail: ')
message = input('Mensaje a mandar: ')
msg = 'Subject: '+subject+'\n'+message #formato para mandar el mail

smtp_object.sendmail(from_address,to_address,msg)
#si me devuelve {} significa que se mando sin problema, si me da un error probablemente sea por la conexion 
smtp_object.quit()