# PyGraphNet: A Python Library for Network Analysis

PyGraphNet is an intuitive and straightforward Python library tailored for graph theory experimentation. This project originated from a personal need to explore and understand graph theory concepts during a graph theory course. It's perfect for anyone interested in delving into graph theory, whether for academic, professional, or personal learning purposes.

## Installations

### Install From Source
To install PyGraphNet from source, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/smomara/pygraphnet.git
```
2. Navigate to the `pygraphnet` directory:
```bash
cd pygraphnet
```
3. Install the package using pip:
```bash
sudo python3 -m pip install -e .
```
### Direct Installation
For a quicker intsallation, use the following command:
```bash
python3 -m pip install git+https://github.com/smomara/pygraphnet.git
```

## Contributing
PyGraphNet is an open-source project under rapid active development, and contributions are highly encouraged and appreciated. Whether it's adding new features, fixing bugs, or improving documentation, your input is valuable.

### Running Tests
Before submitting a pull request, please ensure all test pass. Here's how you can run the tests locally:

For running the entire test suite:
```bash
pytest
```

For running a specific module's test suite:
```bash
pytest operations/
```

For running a specific test suite:
```bash
pytest operations/test_complement.py
```