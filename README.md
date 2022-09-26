# Ecommerce Client
Ecommerce desktop site

## Quick Start

To get this project up and running locally on your computer:


* Set up the Python development environment.
   > **Note:** I want to recommend using a Python virtual environment.
   
  
* Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):
   ```
   pip3 install -r requirements.txt
   ```

* Make Sure Backend Server(REST API project) is running.


* Run main.py
  ```
  python3 main.py
  ```

## Containerization(Docker)
```
sudo docker build --tag ecommerce-client .
sudo docker run ecommerce-client
```

