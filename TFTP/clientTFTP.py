import argparse
from pathlib import PurePosixPath, Path

import argparse_utils
from tftp import TFTPClient, BLOCK_SIZE

import tftpy
import sys, logging, os
from optparse import OptionParser

log = logging.getLogger('tftpy')
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
default_formatter = logging.Formatter('[%(asctime)s] %(message)s')
handler.setFormatter(default_formatter)
log.addHandler(handler)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Trivial File Transfer Protocol (TFTP) client.')
    parser.add_argument('-H', '--host', default='127.0.0.1',
                        help='host de escucha (default: 127.0.0.1)')
    parser.add_argument('port', type=int, default=8085, nargs='?',
                        help='puerto de escucha (default: 8085)')

    operation_group = parser.add_mutually_exclusive_group(required=False)
    operation_group.add_argument(
                '-g', '--get', metavar='FILE_NAME',
                help='Nombre del archivo a descargar')
    operation_group.add_argument(
                '-p', '--put', metavar='FILE_NAME',
                help='Nombre del archivo a subir')
    parser.add_argument(
                '-t', '--target', metavar='FILE_NAME',
                help='Nombre del archivo destino '
                     'Default: Mismo nombre del archivo descargado/subido')
    parser.add_argument(
                '-b', '--block-size', metavar='BLOCK_SIZE', type=int,
                default=BLOCK_SIZE,
                help='Tamaño del bloque definido en RFC 2348 (default: 512)')
    parser.add_argument(
                '-w', '--window-size', metavar='WINDOW_SIZE', type=int, default=1,
                help='Tamaño de banda definido en RFC 7440 (default: 1)')
    return parser


def main():
    args = create_parser().parse_args()
    class Progress(object):
        def __init__(self, out):
            self.progress = 0
            self.out = out

        def progresshook(self, pkt):
            if isinstance(pkt, tftpy.TftpPacketTypes.TftpPacketDAT):
                self.progress += len(pkt.data)
                self.out("Transferred %d bytes" % self.progress)
            elif isinstance(pkt, tftpy.TftpPacketTypes.TftpPacketOACK):
                self.out("Received OACK, options are: %s" % pkt.options)
    progresshook = Progress(log.info).progresshook
    archivo1 = ""
    archivo2 = ""
    peticion=""
    args = create_parser().parse_args()
    
    
    try:
        tclient = tftpy.TftpClient(args.host, int(args.port))
        while True:
            peticion=input("Ingresa la palabra de la accion que deseas\n-Lectura\n-Escritura\n-ctrl+c (salir)\n")
            if peticion=="lectura":
                archivo1=input("Archivo a leer: ")
                archivo2=input("Archivo destino:")
                tclient.download(archivo1, archivo2, progresshook)
            if peticion=="escritura":
                archivo1=input("Nombre del archivo externo:")
                archivo2=input("Nombre del archivo local:")
                tclient.upload(archivo1, archivo2, progresshook)
            if peticion=="salir":
                break
    except Exception as e:
        print(str(e))
    except KeiboardInterrupt:
        print("Saliendo")

if __name__ == '__main__':
    main()