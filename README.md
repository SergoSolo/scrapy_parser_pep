# Project scrapy_parser_pep

With this parser you can get information from the pep site With this parser you can get information from the pep site about the title, number, status and save it to a file.


## How to start

First you need clone the repository:

```bash
git clone git@github.com:SergoSolo/scrapy_parser_pep.git
```

Create and activate virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate
```

install requirements: 

```bash
pip install -r requirements.txt
```

## Usage

For parse information enter the command:

```bash
scrapy crawl pep
```

After this command, 2 data files will be created in /scrapy_parser_pep/results


## Author:
> [Sergey](https://github.com/SergoSolo)