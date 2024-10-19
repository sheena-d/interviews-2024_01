import io
import subprocess
from activity import Activity

class NetworkActivity(Activity):

    SUPPORTED_PLATFORMS = ['Linux', 'Darwin']

    def __init__(self, test_name, destination_protocol, destination_address, destination_port, data=None):
        super().__init__(test_name)
        self.destination_protocol = destination_protocol
        self.destination_address = destination_address
        self.destination_port = destination_port
        self.data = data

    def before_activity_hook(self) -> None:
        self.destination_path = self.compose_destination_path()
        self.network_data, self.amount_of_data = self.compose_network_data()

    def after_activity_hook(self, proc) -> None:
        return None

    def command(self) -> list[str]:
        match self.platform:
            case 'Darwin' | 'Linux':
                return ['echo', '"%s" > %s' % (self.network_data, self.destination_path)]
            case _:
                raise Exception("Platform not supported")

    def details(self) -> dict:
        details = super().details()
        details['amount_of_data'] = self.amount_of_data
        details['protocol'] = self.destination_protocol
        details['destination_address'] = self.destination_path
        details['destination_port'] = self.destination_port
        return details

    def compose_destination_path(self) -> str:
        match self.platform:
            case 'Darwin' | 'Linux':
                return '/dev/%s/%s/%s' % (self.destination_protocol, self.destination_address, self.destination_port)
            case _:
                raise Exception("Platform not supported")

    def compose_network_data(self) -> [str,int]:
        if self.data is not None:
            data = self.data
            return data, len(data)
        else:
            return '', 0
