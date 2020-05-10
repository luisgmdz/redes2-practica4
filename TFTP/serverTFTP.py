
import argparse
import logging

import argparse_utils
from tftp import TFTPServer, BLOCK_SIZE
import tftpy

log = logging.getLogger('tftpy')
log.setLevel(logging.INFO)

# console handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
default_formatter = logging.Formatter('[%(asctime)s] %(message)s')
handler.setFormatter(default_formatter)
log.addHandler(handler)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Trivial File Transfer Protocol (TFTP) server.')
    parser.add_argument('-H', '--host', default='127.0.0.1',
                        help='host de escucha (default: 127.0.0.1')
    parser.add_argument('-p', '--port', type=int, default=8085,
                        help='puerto de escucha (default: 8085)')
    parser.add_argument('-r', '--root',
                        default='/home/luis/Escritorio/redes2/practica4/TFTP',
                        help='Raiz donde se encuentran los documentos')
    parser.add_argument(
        '-b', '--block-size', metavar='BLOCK_SIZE', type=int,
        default=BLOCK_SIZE,
        help='block size as defined in RFC 2348 (default: 512)')
    parser.add_argument(
        '-w', '--window-size', metavar='WINDOW_SIZE', type=int, default=1,
        help='window size as defined in RFC 7440 (default: 1)')
    
    return parser


def main():
    args = create_parser().parse_args()
    #logging_level = logging.INFO
    #logging.basicConfig(level=logging_level)
    server = tftpy.TftpServer(args.root)
    server.listen(args.host, args.port)
    

if __name__ == '__main__':
    main()