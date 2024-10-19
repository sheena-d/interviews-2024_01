import argparse
import json
import io
import platform
from file_create_activity import FileCreateActivity
from file_delete_activity import FileDeleteActivity
from file_modify_activity import FileModifyActivity
from network_activity import NetworkActivity
from network_to_network_activity import NetworkToNetworkActivity
from process_start_activity import ProcessStartActivity

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input') # input filename/path
parser.add_argument('-o', '--output')  # Optional output filename/path
parser.set_defaults(input="./test_suite.json", output="./test_logs.json")
args = parser.parse_args()

test_suite = json.load(io.open(args.input))
test_results = []
for t in test_suite['test_cases']:
    if 'platform' not in t or t['platform'].lower() == platform.system().lower():
        act_type = t['type']
        act = globals()[act_type](t['test_name'], *t['args'])
        success = act.perform_activity()
        if success is True:
            test_results.append(act.log_activity())
        else:
            test_results.append(act.log_failure())
    else:
        test_results.append({"test_name": t['test_name'], "skipped": True})

out_file = io.open(args.output, "w", encoding="utf-8")
out_file.write(json.dumps(test_results, indent=4))