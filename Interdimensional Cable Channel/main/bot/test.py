import os




folder = 'main/bot/images'

for file in os.listdir(folder):
        f = os.path.join(folder, file)

        if os.path.isfile(f):
            # Sends images to discord
            print(f)