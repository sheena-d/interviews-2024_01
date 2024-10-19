from activity import Activity

class FileActivity(Activity):

    FILE_ACTIVITY_DESCRIPTOR = None

    def __init__(self, test_name, file_name, file_path=[]):
        super().__init__(test_name)
        self.file_name = file_name
        self.file_path = file_path

    def command(self) -> list[str]:
        return ['/bin/sh', '-c']

    def before_activity_hook(self) -> None:
        self.full_path = self.compose_file_path()

    def compose_file_path(self) -> str:
        match self.platform:
            case 'Darwin' | 'Linux':
                return '%s/%s' % ("/".join(self.file_path), self.file_name)
            case 'Windows':
                return '%s\\%s' % ("\\".join(self.file_path), self.file_name)

    def details(self) -> dict:
        details = super().details()
        details['full_path'] = self.full_path
        details['descriptor'] = self.FILE_ACTIVITY_DESCRIPTOR
        return details