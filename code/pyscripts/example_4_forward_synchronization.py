# Forward Synchronization (requires the ""./osc_server.py" to also be running)
from pythonosc import udp_client
from pythonosc import osc_bundle_builder, osc_message_builder
import time
import threading

# Config
BPM = 100  # Beats per minute
BEAT_INTERVAL = 60 / BPM

# seconds into the future to schedule ticks
FORWARD_OFFSET = 4  

# Define two OSC clients
# Remote client (Pure Data)
clientIp = '127.0.0.1'
clientPort = 8001
client1 = udp_client.UDPClient(clientIp, clientPort)

# Local client (Python server)
client2Ip = '127.0.0.1'
client2Port = 8000
client2 = udp_client.UDPClient(client2Ip, client2Port)

# Message sending logic
def sendMsg(client):
    print(f'Sending messages to client.')
    
    start_time = time.time()
    beat_number = 0

    while True:
        # NEW custom timestamp = start time + current while Loop round /tick_numb) + forward sync offset
        custom_timestamp = start_time + (beat_number * BEAT_INTERVAL) + FORWARD_OFFSET

        # Create bundle with future timestamp
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
    # Start sending messages to two identical clients (local and remote), but in individual threads
    t_client1 = threading.Thread(target=sendMsg, args=(client1,), daemon=True)
    t_client2 = threading.Thread(target=sendMsg, args=(client2,), daemon=True)

    # start sending
    t_client1.start()
    t_client2.start()

    print("Press Ctrl+C to exit.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")