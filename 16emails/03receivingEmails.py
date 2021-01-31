import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')
M.login(email,password)
M.list() #todo lo que puedo chequear en el mail
M.select('inbox') #selecciono lo que quiero
#vamos a buscar un mail con subject line 
# typ, data = M.search(None,'BEFORE 01-Nov-2000') ejemplo de como se buscaria algo, esto buscaria todos los mails recibidos antes del 01 nov 2000
typ, data = M.search(None,'SUBJECT "NEW TEST PYTHON"') #lo de adentro del string tiene que ser mayuscula
typ #deberia decir ok
data #deberia tener un numero, si no tiene numero significa que no encontro ningun mensaje, si hay multiples numeros encontro multiples mensajes
#para encontrar el mensaje en si
email_id = data[0]
result, email_data = M.fetch(email_id,'(RFC822)') #hay que pasarle el protocolo '(RFC822)'
email_data #aca me da toda la info
#quiero solo el mensaje 
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
import email
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain': #'text/plain' es si espero que solo sea texto, puedo cambiar a 'text/html' si alguien dejo un link en el mail
        body = part.get_payload(decode=True)
        print(body)

M.quit()