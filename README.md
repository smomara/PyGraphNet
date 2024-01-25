# graphent: A Python Library for Graph Theory Experiments

graphent is an intuitive and straightforward Python library tailored for graph theory experimentation. This project originated from a personal need to explore and understand graph theory concepts during a graph theory course. It's perfect for anyone interested in delving into graph theory, whether for academic, professional, or personal learning purposes.

## Installation

### Install From Source
To install graphent from source, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/smomara/graphent.git
```
2. Navigate to the `graphent` directory:
```bash
cd graphent
```
3. Install the package using pip:
```bash
sudo python3 -m pip install -e .
```
### Direct Installation
For a quicker intsallation, use the following command:
```bash
python3 -m pip install git+https://github.com/smomara/graphent.git
```
## Examples
I have included a ![basic usage example](https://github.com/smomara/graphent/blob/main/examples/word_graph.ipynb) of a word graph is available in the `examples` folder of the repository. I am constantly updating this section with increasingly complex examples as development continues, so stay tuned!

## Contributing
graphent is an open-source project under rapid active development, and contributions are highly encouraged and appreciated. Whether it's adding new features, fixing bugs, or improving documentation, your input is valuable.

### Running Tests
Before submitting a pull request, please ensure all test pass. Here's how you can run the tests locally:

- For running a specific test suite, such as edge tests:
```bash
python3 test/test_edge.py
```
- For running the entire test suite:
```bash
pytest test/
```