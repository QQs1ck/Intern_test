from pyngrok import ngrok
def get_url():
  auth_token = '2kMyEotBfIixPcXvEx0ll1zeWu5_3wteHD4xu7sXytXEY8jY7'
  ngrok.set_auth_token(auth_token)
  ngrok.kill()
  ngstart = ngrok.connect(8000)
  ngrock_public_url = ngstart.public_url 
  print(ngstart)
  print(ngrock_public_url)
  return ngrock_public_url
