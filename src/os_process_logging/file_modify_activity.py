from file_activity import FileActivity

class FileModifyActivity(FileActivity):
    FILE_ACTIVITY_DESCRIPTOR = 'modify'
    SUPPORTED_PLATFORMS = ['Linux', 'Darwin']

    def command(self) -> list[str]:
        match self.platform:
            case 'Darwin' | 'Linux':
                return [*super().command(), 'echo "New Content" >> %s' % self.full_path]

