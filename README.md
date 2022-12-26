# Expense Tracker

Small program that downloads all the Emirates NBD, CBD and FAB-RAK banks statements from an email box
then parses the PDF files to a clean dataset and save it to a SQL DB.

## Getting Sarted

Setup your virtualenv (python 3.10 is recommended)

```bash
python3 -m venv venv
./venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Set-up your env vars (see the `env.example` file)

```bash
cp env.example .env
```

## ROADMAP

- MORE CONFIGURABLE EMAIL PARSER / FILTER - DONE
- OPEN PDF WITH PASSWORD (scenario with same password every file) with pdfminer.six
- PDF PARSER (make it work with the PDF first)
- ETL PIPELINE
- SQL CONFIG
- VISUALISATION TOOLS
- MAKE COOLS CHARTS
- MANUAL CATEGORY INTERFACE 
- USE NLP TO AUTO-TAG THE CATEGORIES.
- MAKE IT WORK FOR MANY BANKS


