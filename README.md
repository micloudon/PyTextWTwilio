This app will send a text message using twilio.

Create a twilio account, they have free trials.

Once the account is created install twilio,
use the command: 
pip install twilio
or
pipenv install twilio
if you are using a virtual environment
or
install twilio
if you don't use pip.

After you install twilio, simply copy and paste 
the account sid and auth token from your twilio account.
Under to="" enter your twilio phone number.
Under from_="" enter the number you wish to text
Under body="" enter the message you wish to send

Run the program and your message will be sent


The api security keys
account_sid
auth_token
would ideally be hidden in a .gitignore file,
but for the purposes of this project they are exposed.
Don't upload any private info to github.