# graphent

A simple python graphing library. Created so I can experiment while taking a graph theory course.

## Installation

### From Source
```bash
git clone https://github.com/smomara/graphent.git
cd graphent
sudo python3 -m pip install -e .
```
### Direct
```bash
python3 -m pip install git+https://github.com/smomara/graphent.git
```
## Usage

### Examples
A basic usage ![example](https://github.com/smomara/graphent/blob/main/examples/word_graph.ipynb) is available in the `examples` folder of the repository. Increasingly complex examples will be added as development continues.

## Development
This library is under active development and any contributions are more than welcome.

### Running Tests
Please locally run tests before submitting a pull request. To locally run the tests:
```bash
python3 test/test_edge.py   # just the edge test suite
pytest test/                # whole test suite
```