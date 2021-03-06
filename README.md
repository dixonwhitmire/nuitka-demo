# nuitka-demo
Demonstration of Nuitka, "the Python Compiler"

This project provides references for multiple use-cases on separate feature branches. Current use-cases include:

- Hello World Standalone App: [main branch](https://github.com/dixonwhitmire/nuitka-demo)

Each feature branch contains the generated C assets, for reference. To view a use-case simply switch to the appropriate branch

## Setup

This project requires the following:

- [Python 3.9](https://www.python.org/downloads/) or higher for runtime/coding support
- [Ccache](https://ccache.dev/documentation.html) to support Nuitka compilation caching
- A C Compiler which supports C11 or greater

### Setup Validation
Confirm that Python, ccache, and the C compiler are available on your system. The commands used below are for OS X and may
differ from other platforms.

```shell
(venv) mbp nuitka-demo % python3 --version
Python 3.9.7

(venv) tdw@dixons-mbp nuitka-demo % ccache --version
ccache version master.971f1183

(venv) tdw@dixons-mbp nuitka-demo % clang --version
Apple clang version 12.0.5 (clang-1205.0.22.9)
Target: x86_64-apple-darwin20.6.0
Thread model: posix
InstalledDir: /Library/Developer/CommandLineTools/usr/bin
```

### Project Setup
```shell
pip install --upgrade pip setuptools

git clone https://github.com/dixonwhitmire/nuitka-demo
cd nuitka-demo

python3 -m venv venv && source venv/bin/activate && pip install --upgrade pip setuptools
pip install -e .[dev]
pytest
```

## Generate Native Executable
```shell
python3 -m nuitka --python-flag=no_site \
                   --onefile \
                   --clang \
                   --show-scons \
                   --show-progress \
                   --warn-implicit-exceptions \
                   --warn-unusual-code \
                   --prefer-source-code \
                   -o hello-world-nuitka src/tdw/nuitka_demo/main.py               

./hello-world-nuitka
```
An additional parameter, `--generate-c-only`, is helpful for debugging. 
