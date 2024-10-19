from network_activity import NetworkActivity
import subprocess

class NetworkToNetworkActivity(NetworkActivity):

    SUPPORTED_PLATFORMS = ['Linux', 'Darwin']

    def __init__(self, test_name, destination_protocol, destination_address, destination_port, source_protocol, source_address, source_port):
        super().__init__(test_name, destination_protocol, destination_address, destination_port)
        self.source_protocol = source_protocol
        self.source_address = source_address
        self.source_port = source_port

    def details(self) -> dict:
        details = super().details()
        details['source_address'] = self.source_address
        details['source_port'] = self.source_port
        return details


    def compose_network_data(self) -> [str,int]:
        if self.source_address is not None and self.source_port is not None:
            sp = subprocess.run(['/bin/sh', 'cat /dev/%s/%s/%s' % (self.source_protocol, self.source_address, self.source_port)], capture_output=True)
            data = sp.stdout
            return data, len(data)
        else:
            return '', 0
