# STREAMLIT-SAMPLE
This is an example for streamlit connection with API and postgresql DB
This project is based on python and streamlit library for UI.

## Configuration
Before using this application make sure to:
- Install python with minimum requirements python 3.10.
[Link for python installation](https://www.python.org)
- install requirements from txt file with terminal.
```
  pip install -r requirements.txt
```
- After install requirements, configure file `secrets.toml` at `.streamlit` folder. `[If Needed]`
- If you don't have `.streamlit` folder. Create new folder first at root folder.
- Setting new configuration at `secrets.toml` file like :

## Running
To run this project with cmd just type
```
streamlit run streamlit_main.py
```
or you can use docker to build 
```
docker build -t streamlit-sample .
```
and run with
```
docker run -p 8501:8501 streamlit-sample
```

## Documentation
If you have any question related to this project, feel free to contact me at my github <br/>
[My Github Profile](https://github.com/ryanisml)