"""
Builds the version of moment.js that's in vendor/moment and
packages it as a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "2.0.0"


def cp(src):
    cmd = [
        "cp -R vendor/moment/%s moment/static/moment/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./moment/static/moment"], shell=True)
    subprocess.call(
            ["cd vendor/moment && git checkout %(version)s" % args],
            shell=True)
    cp("min/*")
    cp("moment.js")
    cp("LICENSE")

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
