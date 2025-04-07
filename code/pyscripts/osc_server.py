# OSC Server
from pythonosc import dispatcher, osc_server
from playsound import playsound
import threading
import time

# Config
serverIp = '127.0.0.1'
serverPort = 8000
audio = "./tick.wav"

# OSC handler for incoming /tick OSC messages
def pyHandler(address, args):
    print(f'{address} {args}')
    
    if args == "tick":
        # If a tick message is recevied, play audio
        playsound(audio)

# OSC server
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/tick*", pyHandler)
server = osc_server.ThreadingOSCUDPServer((serverIp, serverPort), dispatcher)

def startOSCServer():
    print(f"Starting OSC server on {server.server_address[0]}:{server.server_address[1]}")
    server.serve_forever()


if __name__ == "__main__":
    # Start thread with OSC server and listen for messages
    t_server = threading.Thread(target=startOSCServer, daemon=True)
    t_server.start()

    print("Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")