# Networked Controlled Metronome
from pythonosc import udp_client
from pythonosc import osc_bundle_builder, osc_message_builder
import time
import threading

# Config
BPM = 100
BEAT_INTERVAL = 60 / BPM

# Define OSC remote client (Pure Data)
clientIp = '127.0.0.1'
clientPort = 8001
client1 = udp_client.UDPClient(clientIp, clientPort)

# Message sending logic
def sendMsg(client):
    print('Sending messages to client.')
    while True:
        # Create bundle with IMMEDIATE timestamp
        bundle = osc_bundle_builder.OscBundleBuilder(
            osc_bundle_builder.IMMEDIATELY)

        # Create and add message
        msg = osc_message_builder.OscMessageBuilder(address="/tick")
        
        msg.add_arg("tick")
        
        bundle.add_content(msg.build())

        # Send the bundle
        client.send(bundle.build())

        # Wait for the next beat
        time.sleep(BEAT_INTERVAL)


if __name__ == "__main__":
    # introduce threading for better cleanup and keyboard control of endless while Loop.
    t_client1 = threading.Thread(target=sendMsg, args=(client1,), daemon=True)
    
    # Start sending messages to remote client in a thread
    t_client1.start()

    print("Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
