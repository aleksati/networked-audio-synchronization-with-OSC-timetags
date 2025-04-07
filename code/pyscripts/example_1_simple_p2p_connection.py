# Simple p2p Connection
from pythonosc import udp_client
from pythonosc import osc_bundle_builder, osc_message_builder
import time

# Define OSC remote client (Pure Data)
clientIp = '127.0.0.1'
clientPort = 8001
client1 = udp_client.UDPClient(clientIp, clientPort)

# Message sending logic
def sendMsg(client):
    print('Sending 10 messages to the client.')
    for i in range(10):
        # Create bundle with IMMEDIATE timestamp
        bundle = osc_bundle_builder.OscBundleBuilder(
            osc_bundle_builder.IMMEDIATELY)

        # Create and add message
        msg = osc_message_builder.OscMessageBuilder(address="/tick")
        
        msg.add_arg(f'Hello nr.{i} from Python client!')
        
        bundle.add_content(msg.build())

        # Send the bundle
        client.send(bundle.build())

        # Wait for the next beat
        time.sleep(0.5)
    
    print("done sending...")


if __name__ == "__main__":
    sendMsg(client1)
