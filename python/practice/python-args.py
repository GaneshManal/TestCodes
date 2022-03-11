import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', help='Consul agent port')
    parser.add_argument('logdir', help='Tetration log directory')
    args = parser.parse_args()
    consul_agent_port = args.port
    tet_log_dir = args.logdir
    print(args, tet_log_dir, consul_agent_port)