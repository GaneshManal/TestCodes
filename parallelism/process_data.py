import threading
import os
import json
import logging


class ProcessBatch:

    def __init__(self, batches):
        self.batches = batches

        with open(os.getcwd() + os.path.sep + 'conf' + os.path.sep + 'config.json') as f:
            user_configs = json.load(f)
            self.data_dir = user_configs.get('data_dir')
            self.out_dir = user_configs.get('out_dir')

        threads = []
        for x_batch in batches:
            thread = threading.Thread(target=self.run, args=(x_batch,))
            threads.append(thread)
            thread.daemon = True
            thread.start()

        for thread in threads:
            thread.join()

    def run(self, batch):
        log = logging.getLogger()
        log.warning("Oh no, we're in a thread!")

        output_file = os.getcwd() + os.path.sep + 'result.txt'
        for item in batch:
            with open(self.data_dir + os.path.sep + item, 'r') as read_file, open(output_file, 'a') as write_file:
                lines = read_file.readlines()
                write_file.writelines(lines)

