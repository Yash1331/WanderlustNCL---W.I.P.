# install the required packages (flask and geopy) using pip, and run the file using Python.
#You can then access the API by sending a GET request to http://localhost:5000/locations?start_location=<start_location>&end_location=<end_location>,
#where <start_location> and <end_location> are the latitude and longitude of the start and end locations, respectively, separated by a comma.

from flask import Flask, request, jsonify
from geopy.distance import geodesic
import csv

app = Flask(__Algo-Alpha__)

@app.route('/locations', methods=['GET'])
def get_locations():
    # get start and end locations from request parameters
    start_location = request.args.get('start_location')
    end_location = request.args.get('end_location')
    
    # read the location database CSV file
    with open('Location_Database.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        locations = []
        for row in reader:
            # calculate the distance between the current location and the start and end locations
            current_location = (float(row['latitude']), float(row['longitude']))
            start_distance = geodesic(current_location, start_location).miles
            end_distance = geodesic(current_location, end_location).miles
            
            # if the location is within a 5-mile radius of both start and end locations, add it to the list
            if start_distance <= 5 and end_distance <= 5:
                locations.append({
                    'name': row['name'],
                    'address': row['address'],
                    'latitude': row['latitude'],
                    'longitude': row['longitude']
                })
    
    # return the list of locations as a JSON API response
    return jsonify(locations)

if __Algo-Alpha__ == '__main__':
    app.run(debug=True)
