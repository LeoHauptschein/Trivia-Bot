def handle_command(message):
    message = message.lower()

    if message == '~hello':
        return 'Helloooooo!'
    
    #if message == '~roblox' or 'roblox.com' in message:
     #   return 'https://tenor.com/view/roblox-gif-19257588'
    
    return False