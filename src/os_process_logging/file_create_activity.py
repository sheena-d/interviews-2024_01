from file_activity import FileActivity

class FileCreateActivity(FileActivity):
    FILE_ACTIVITY_DESCRIPTOR = 'create'
    SUPPORTED_PLATFORMS = ['Linux', 'Darwin', 'Windows']

    def command(self) -> list[str]:
        match self.platform:
            case 'Darwin' | 'Linux':
                return [*super().command(), 'touch %s' % self.full_path]
            case 'Windows':
                return [*super().command(), 'New-Item %s' % self.full_path]
