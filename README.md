# transitflow

I wanted to teach myself:
- using an API
- making webpages: using HTML, Flask, etc

** Virtual Environment Testing (assuming Mac) **

- To create a virtual environment: python3 -m venv <name of venv: venv>
- To activate the environment: source <name of venv: venv>/bin/activate
- To activate: deactivate

The packages needed to run the app are in requirements.txt
- Personal note: to update what packages are needed: pip freeze > requirements.txt

*Using build_shapes.py*
- The user doesn't have to run anything extra, but just to make sense of the script and the data folder:
- Raw GTFS → (script) → cleaned JSON → (Flask) → frontend map