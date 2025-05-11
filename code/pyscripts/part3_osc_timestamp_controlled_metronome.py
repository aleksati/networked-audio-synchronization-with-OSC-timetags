# Part 3 - OSC Timestamp Controlled Metronome
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

    # using the current time once and increment ticks over every while Loop is a more predicable metronome for creating custom timestamp based on a fixed tempo. 
    start_time = time.time()
    beat_number = 0

    while True:
        # Custom timestamp = start time + current while Loop round /tick_numb)
        custom_timestamp = start_time + (beat_number * BEAT_INTERVAL)

        # open a OSC bundle
        # add our timestamp to the bundle builder object
        bundle = osc_bundle_builder.OscBundleBuilder(custom_timestamp)

        # Create and add message
        msg = osc_message_builder.OscMessageBuilder(address="/tick")
        
        msg.add_arg("tick")
        
        bundle.add_content(msg.build())

        # Send the bundle
        client.send(bundle.build())

        # increment the beat number for every loop
        beat_number += 1

        # Wait for the next beat
        time.sleep(BEAT_INTERVAL)


if __name__ == "__main__":
    # Start sending messages to remote client in a thread
    t_client1 = threading.Thread(target=sendMsg, args=(client1,), daemon=True)
    t_client1.start()

    print("Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
