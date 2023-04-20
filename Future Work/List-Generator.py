# install the required packages (flask and geopy) using pip, and run the file using Python.
#You can then access the API by sending a GET request to http://localhost:5000/locations?start_location=<start_location>&end_location=<end_location>,
#where <start_location> and <end_location> are the latitude and longitude of the start and end locations, respectively, separated by a comma.

from flask import Flask, request, jsonify, render_template
import pandas as pd
import geopy.distance

app = Flask(__name__)

def find_attractions(start, end):
    # Load location database from CSV file
    df = pd.read_csv('Location_Database.csv')
    
    # Convert start and end locations to coordinates
    start_coord = (df.loc[df['Location'] == start, ['Latitude', 'Longitude']].values[0][0],
                   df.loc[df['Location'] == start, ['Latitude', 'Longitude']].values[0][1])
    end_coord = (df.loc[df['Location'] == end, ['Latitude', 'Longitude']].values[0][0],
                 df.loc[df['Location'] == end, ['Latitude', 'Longitude']].values[0][1])
    
    # Calculate distance between start and end locations
    distance = geopy.distance.distance(start_coord, end_coord).miles
    
    # Filter locations within 5 miles radius of start and end locations
    df_filtered = df[(df['Location'] != start) & (df['Location'] != end)]
    df_filtered = df_filtered[df_filtered.apply(lambda row: geopy.distance.distance(start_coord, (row['Latitude'], row['Longitude'])).miles <= 5, axis=1)]
    df_filtered = df_filtered[df_filtered.apply(lambda row: geopy.distance.distance(end_coord, (row['Latitude'], row['Longitude'])).miles <= 5, axis=1)]
    
    # Sort locations by distance to start location
    df_filtered['Distance to start'] = df_filtered.apply(lambda row: geopy.distance.distance(start_coord, (row['Latitude'], row['Longitude'])).miles, axis=1)
    df_filtered.sort_values(by='Distance to start', inplace=True)
    
    # Return list of locations as JSON
    return df_filtered['Location'].tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locations', methods=['GET'])
def locations():
    start = request.args.get('start')
    end = request.args.get('end')
    
    locations = find_attractions(start, end)
    
    return jsonify(locations=locations)

if __name__ == '__main__':
    app.run(debug=True)

