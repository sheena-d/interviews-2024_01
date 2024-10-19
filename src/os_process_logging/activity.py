import json
import platform
import subprocess
import pwd

class Activity:

    def __init__(self, test_name):
        self.test_name = test_name
        self.platform = platform.system()
        if not self.platform in self.SUPPORTED_PLATFORMS:
            raise Exception("Platform not supported")

    def perform_activity(self) -> bool:
        self.before_activity_hook()
        try:
            proc = subprocess.Popen(self.command(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except Exception as e:
            print("Test case failed: %s" % e)
            return False
        self.process_id = proc.pid
        self.username = self.proc_username()
        self.process_name = self.proc_name()
        self.timestamp = self.proc_timestart()
        self.process_command_line = self.command_line()

        self.after_activity_hook(proc)
        proc.terminate()
        return True

    def command(self) -> list[str]:
        return []

    def details(self) -> dict:
        return {
            "test_name": self.test_name,
            "timestamp": self.timestamp,
            "username": self.username,
            "platform": self.platform,
            "process_name": self.process_name,
            "process_id": self.process_id,
            "process_command_line": self.command_line()
        }

    def log_activity(self) -> dict:
        details = self.details()
        print("test case succeeded: %s" % self.process_name)
        return details

    def log_failure(self) -> dict:
        print("test case failed: %s" % self.command_line())
        details = {"test_name": self.test_name, "failure":  True}
        return details

    def command_line(self) -> str:
        command = self.command()
        match self.platform:
            case 'Linux':
                return " ".join(command)
            case 'Windows':
                return ""
            case 'Darwin':
                return ""
            case _:
                raise Exception("Platform not supported")

    def proc_timestart(self) -> int:
        match self.platform:
            case 'Linux' | 'Darwin':
                sp = subprocess.run(['ps', '-p', '%d' % self.process_id, '-D', '%s', '-o', 'lstart='], capture_output=True)
                return int(sp.stdout)
            case 'Windows':
                return ""
            case 'Darwin':
                return ""
            case _:
                raise Exception("Platform not supported")

    def proc_name(self) -> str:
        match self.platform:
            case 'Linux':
                sp = subprocess.run(['ps', '-p', '%d' % self.process_id, '-o', 'comm='], capture_output=True)
                return sp.stdout.decode("utf-8").strip()
            case 'Windows':
                return ""
            case 'Darwin':
                return ""
            case _:
                raise Exception("Platform not supported")

    def proc_username(self) -> str:
        match self.platform:
            case 'Linux':
                sp = subprocess.run(['ps', '-p', '%d' % self.process_id, '-o', 'euid='], capture_output=True)
                return pwd.getpwuid(int(sp.stdout)).pw_name
            case 'Windows':
                return ""
            case 'Darwin':
                return ""
            case _:
                raise Exception("Platform not supported")

    def after_activity_hook(self, process) -> None:
        return None

    def before_activity_hook(self) -> None:
        return None