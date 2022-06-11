import os
import json
from process_data import ProcessBatch


def main():
    with open(os.getcwd() + os.path.sep + 'conf' + os.path.sep + 'config.json') as f:
        user_configs = json.load(f)

    input_files = os.listdir(os.getcwd() + os.path.sep + user_configs.get('data_dir'))
    thread_count = user_configs.get('thread_count', 1)

    batch_size = 0
    if thread_count:
        batch_size = len(input_files)/thread_count

    if batch_size:
        batches = [input_files[start: start+batch_size] for start in xrange(0, len(input_files), batch_size)]
        print batches
        ret = ProcessBatch(batches)
        print 'Returned: ', ret


if __name__ == "__main__":
    main()
