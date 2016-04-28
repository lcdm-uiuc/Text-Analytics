###Metadata List from each json file from the NYT Search API

- Web URL
- Snippets
- lead_paragraph  (pretty much same as snippets, but slightly longer) 
- source 
- headline
- pub_date (and time)
- document_type
- word_count
- type_of_material 

____________

Python3+ is required for the best result and to avoid unnecessary errors. 

JSON_Scraper.py lets you download multiple JSON files at once, and it automatically rename each file so that we can easily process the file automatically. 

parser.py lets you parse multiple JSON files at once, and will only extract subsection (necessary information) of each JSON file (snippets, abstract, lead_paragragh, web_url, etc.)

Parsing 100 JSON files from Politics section has output-ed 30,789 words, which can be viewed in Raw Text Data folder. 
