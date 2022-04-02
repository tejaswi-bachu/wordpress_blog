import sys

from gevent.server import StreamServer


def write_logs_to_file(socket, address):
    rfileobj = socket.makefile(mode='rb')
    unique_file_name = 'log_file_unique'
    log_file = open("{}/{}.log".format(logging_server_dir, unique_file_name), 'ab')
    while True:
        line = rfileobj.readline()
        if not line:
            msg = b"client disconnected"
            log_file.write(msg)
            break
        if line.strip().lower() == b'quit':
            msg = b"client quit"
            log_file.write(msg)
            break
        log_file.write(line)
    rfileobj.close()
    log_file.close()


if __name__ == '__main__':
    logging_server_ip = sys.argv[1]
    logging_server_port = int(sys.argv[2])
    logging_server_dir = sys.argv[3]
    server = StreamServer((logging_server_ip, logging_server_port), write_logs_to_file)
    server.serve_forever()


# Run the logging server as below. Replace the IP, Port and directory for logs
# python logging_server.py 192.168.10.20 5000 /home/logging_server/logs
