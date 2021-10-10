from flask import Flask, request, jsonify
import smtplib # imported smtp lib . For you , smtplib is already installed , so you can directly import and use it in the code. 
app = Flask(__name__)

def send_email():
    s = smtplib.SMTP('smtp.gmail.com', 587) # creates SMTP session
    s.starttls() # start TLS for security
    s.login("sender_email_id", "sender_email_id_password") # Authentication
    message = "Message_you_need_to_send" # message to be sent
    s.sendmail("sender_email_id", "receiver_email_id", message) # sending the mail
    s.quit() #terminating the session 
    return

@app.route("/reminder", methods=['POST'])
def reminder():
    send_email()
    return jsonify({"success":True})

if __name__ == "__main__":
    app.run(debug = True)