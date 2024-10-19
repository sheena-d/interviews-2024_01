import subprocess
from activity import Activity

class ProcessStartActivity(Activity):

    SUPPORTED_PLATFORMS = ['Linux', 'Darwin', 'Windows']

    def __init__(self, test_name, command_args):
        super().__init__(test_name)
        self.command_args = command_args

    def command(self) -> list[str]:
        match self.platform:
            case 'Darwin' | 'Linux':
                return self.command_args
            case 'Windows':
                return self.command_args
            case _:
                raise Exception("Platform not supported")
