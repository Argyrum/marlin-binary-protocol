import argparse
import os
import binproto2 as mbp

class ConsoleLogger(object):
    def debug(self, msg, *args, **kwargs):
        pass
    def info(self, msg, *args, **kwargs):
        print("INFO: {0}".format(msg))
    def warning(self, msg, *args, **kwargs):
        print("WARNING: {0}".format(msg))
    def error(self, msg, *args, **kwargs):
        print("ERROR: {0}".format(msg))
    def critical(self, msg, *args, **kwargs):
        print("CRITICAL: {0}".format(msg))
    def exception(self, msg, *args, **kwargs):
        print("EXCEPTION: {0}".format(msg))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send files over a serial port to Marlin')
    parser.add_argument('source',                                       help='Source path')
    parser.add_argument('destination',          nargs='?',              help='Destination path (default SD root folder)')
    parser.add_argument("-p", "--port",         default="COM3",         help="Serial port to use (default COM3)")
    parser.add_argument("-b", "--baud",         default="115200",       help="Baud rate of serial connection (default 115200)")
    parser.add_argument("-d", "--blocksize",    default="512",          help="Defaults to autodetect (Default 512)")
    parser.add_argument("-r", "--reset",        action='store_true',    help="Reset after transfer (For firmware flash, needed for E3V2s)")
    parser.add_argument("-t", "--test",         action='store_true',    help="Benchmark the serial link without storing the file")
    parser.add_argument("-c", "--compression",  action='store_true',    help="Enable compression (Recommended for files above 500kB)")
    parser.add_argument("-x", "--timeout",      default="1000",         help="Communication timout, lossy/slow connections need higher values")

    args = parser.parse_args()

    try:
        protocol = mbp.Protocol(args.port, args.baud, args.blocksize, int(args.timeout), ConsoleLogger())
        echologger = mbp.EchoProtocol(protocol, ConsoleLogger())

        protocol.connect()

        filetransfer = mbp.FileTransferProtocol(protocol, None, ConsoleLogger())
        filetransfer.copy(args.source, args.destination or os.path.basename(args.source), args.compression, args.test)

        protocol.disconnect()

        if args.reset:
            protocol.send_ascii("M997")
        else:
            protocol.send_ascii("M21")
            
    except KeyboardInterrupt:
        filetransfer.abort()

    except mbp.FatalError:
        print("Too Many Retries, Abort")

    except Exception as exc:
        print(exc)

    finally:
        protocol.shutdown()
