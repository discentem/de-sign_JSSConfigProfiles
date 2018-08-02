import argparse
import subprocess
def run_live(command):
  """
  Run a subprocess with real-time output.
  Can optionally redirect stdout/stderr to a log file.
  Returns only the return-code.
  """
  # Validate that command is not a string
  if isinstance(command, basestring):
    # Not an array!
    raise TypeError('Command must be an array')
  # Run the command
  proc = subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
  while proc.poll() is None:
    l = proc.stdout.readline()
    print l,
  print proc.stdout.read()
  return proc.returncode

def createReadableProfileFrom(path="", name="de-signed.mobileconfig"):
    if path == "" or not(path):
        raise Error("Path is empty")

    if ".mobileconfig" not in name:
        name = name + ".mobileconfig"

    cmd = "openssl smime -inform DER -verify -in {0} -noverify -out {1}"
    cmd = cmd.format(path, name)
    cmd = cmd.split(" ")
    run_live(cmd)

    cmd2 = ["plutil", "-convert", "xml1", "./{0}".format(name)]
    run_live(cmd2)

def gather_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        default="",
                        dest='path')
    parser.add_argument('-n', '--name',
                        dest='name',
                        default="de-signed.mobileconfig")


    return parser.parse_args()

def main():
    args = gather_args()
    createReadableProfileFrom(path=args.path, name=args.name)

main()
