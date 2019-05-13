# Traffic-directions-Gemeente-Duiven
Traffic directions website for Gemeente Duiven

### Prerequisites
* Python3 
* Pip3 
* Git 
* [Google Directions API Key](https://cloud.google.com/maps-platform/?apis=routes) 

### Installing
Clone this repository.
```
git clone https://github.com/japper83/Traffic-directions-Gemeente-Duiven
cd Traffic-directions-Gemeente-Duiven
```

Install the google maps and flask modules.
```
pip3 install googlemaps
pip3 install flask

```

Change the Google Maps API value in the main.py file.
```
token = 'EbYhtflimzMpWEiNNRcfKbJubwpyNQwOXgQGZBA'
```

### Running the script
```
FLASK_APP=main.py flask run --host 0.0.0.0
```
