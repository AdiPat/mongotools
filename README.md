# Mongo Tools

Mongotools is a command line utility written in Python for database migration across teams. I wrote these scripts for personal use. However, I plan to extend it in future if I get the time.

## Getting Started

Update server details, database name and data path in `config.py`. The default path for data is the `/data` folder. Exported data from database is stored in `/data/export` and data that you want to import to the database must be stored in `/data/import`.

## Prerequisites

It is reccomended that you install a virtual environment along with Python 3. Install dependencies with the command given below.

```
pip install -r requirements.txt
```

## Usage

- Import data to database from JSON files. Your data files must be in `/data/import`.

```
python mongotools.py import
```

- Export data from database to `/data/export`.

```
python mongotools.py export
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
