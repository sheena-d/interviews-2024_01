from file_activity import FileActivity

class FileDeleteActivity(FileActivity):
    FILE_ACTIVITY_DESCRIPTOR = 'delete'
    SUPPORTED_PLATFORMS = ['Linux', 'Darwin', 'Windows']

    def command(self) -> list[str]:
        match self.platform:
            case 'Darwin' | 'Linux':
                return [*super().command(), 'rm %s' % self.full_path]
            case 'Windows':
                return [*super().command(), 'Remove-Item %s' % self.full_path]
