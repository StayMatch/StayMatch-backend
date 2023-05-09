from flask import Flask, request, jsonify
from pymongo import MongoClient 
import datetime

app = Flask(__name__)

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.staymatch
users = db.user

@app.route("/")
def hello():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    rec= {
    "name":"Kritika",
    "email":'1111kritika@gmail.com'
    }

    recc= users.insert_one(rec)
    print(recc)
    return response_body


owners = db.owner
@app.route("/add/owner")
def add_owner():
    current_time = datetime.datetime.now()
    new_owner= {

         "_id": 1,
         "uniqueStateId": "ABCDEF",
         "userName": "john@daniel.com",
         "password": "",
         "fName": "John",
         "lName": "Daniel",
         "email": "john@daniel.com",
         "phoneNo": "7654786865",
         "Address": "111 Fulton St.",
         "House": "Apt 2G",
         "city": "New York",
         "state": "NY",
         "zipCode": "10021",
         "profilePic": "",
         "creationDate": current_time,
        "modifiedDate": current_time
        }

    recc= owners.insert_one(new_owner)
    print(recc)
    return "Success"

@app.route("/owner", methods=['POST'])
def add_new_owner():
    print("hello")
    current_time = datetime.datetime.now()
    owner_obj=  request.get_json()
    owner_obj.update({'_id':1,'creationDate': current_time, 'modifiedDate': current_time,  })
    print(owner_obj)
    recc= renters.insert_one(owner_obj)
    print(recc)
    return "Success"

@app.route("/get/owner/<str:id>")
def get_owner(id):
    print(id)
    rec = owners.find()
    #print(jsonify(rec))
    recc= owners.find_one({"_id": id})
    #print(recc)
    return jsonify(recc)

renters = db.renter

@app.route("/add/renter")
def add_renter():
    current_time = datetime.datetime.now()
    new_renter= {

         "renterId": 1,
         "userName": "john@daniel.com",
         "password": "",
         "fName": "James",
         "lName": "Karl",
         "email": "james@karl.com",
         "phoneNo": "7654786865",
         "Address": "111 Fulton St.",
         "House": "Apt 2G",
         "city": "Jersey City",
         "state": "NJ",
         "zipCode": "08007",
         "profilePic": "",
         "creationDate": current_time,
        "modifiedDate": current_time
        }

    recc= renters.insert_one(new_renter)
    print(recc)
    return "Success"

@app.route("/renter", methods=['POST'])
def add_new_renter():
    print("hello")
    current_time = datetime.datetime.now()
    renter_obj=  request.get_json()
    renter_obj.update({'creationDate': current_time, 'modifiedDate': current_time })
    print(renter_obj)
    recc= renters.insert_one(renter_obj)
    print(recc)
    return "Success"



amenities = db.amenitiesList
@app.route("/list/amentities")
def list_amenities():
    amenities_list =[
    {
        "_id": 1,
        "amenityName": "Electricity",
        "amenityType": "Included, NA",
        "amenityPrice": "Free, Paid",
        "creationDate": "1/1/23 0:00"
    },
    {
    "_id": 2,
    "amenityName": "Water",
    "amenityType": "Included, NA",
    "amenityPrice": "Free, Paid",
    "creationDate": "1/2/23 0:00"
    },
    {
    "_id": 3,
    "amenityName": "Internet",
    "amenityType": "Included, NA",
    "amenityPrice": "Free, Paid",
    "creationDate": "1/3/23 0:00"
    },
    {
    "_id": 4,
    "amenityName": "Dishwasher",
    "amenityType": "Included, NA",
    "amenityPrice": "Free",
    "creationDate": "1/4/23 0:00"
    },
    {
    "_id": 5,
    "amenityName": "Microwave",
    "amenityType": "Included, NA",
    "amenityPrice": "Free",
    "creationDate": "1/5/23 0:00"
    },
    {
    "_id": 6,
    "amenityName": "Referigerator",
    "amenityType": "Included, NA",
    "amenityPrice": "Free",
    "creationDate": "1/6/23 0:00"
    },
    {
    "_id": 7,
    "amenityName": "Stove/Oven",
    "amenityType": "Included, NA",
    "amenityPrice": "Free",
    "creationDate": "1/7/23 0:00"
    },
    {
    "_id": 8,
    "amenityName": "Heating",
    "amenityType": "Included, NA",
    "amenityPrice": "Free",
    "creationDate": "1/8/23 0:00"
    },
    {
    "_id": 9,
    "amenityName": "Cooling",
    "amenityType": "Included, NA",
    "amenityPrice": "Free",
    "creationDate": "1/9/23 0:00"
    },
    {
    "_id": 10,
    "amenityName": "PetsAllowed",
    "amenityType": "Cats allowed, Dogs allowed, Cats and Dogs allowed, NA",
    "amenityPrice": "Free",
    "creationDate": "1/10/23 0:00"
    },
    {
    "_id": 11,
    "amenityName": "Laundary",
    "amenityType": "In-unit, Shared, NA",
    "amenityPrice": "Free, Paid",
    "creationDate": "1/11/23 0:00"
    },
    {
    "_id": 12,
    "amenityName": "parking",
    "amenityType": "Covered Parking, Uncovered Parking, Street Parking, NA",
    "amenityPrice": "Free, Paid",
    "creationDate": "1/12/23 0:00"
    },
    {
    "_id": 13,
    "amenityName": "pool",
    "amenityType": "Shared, Not Available",
    "amenityPrice": "Free, Paid",
    "creationDate": "1/13/23 0:00"
    },
    {
    "_id": 14,
    "amenityName": "gym",
    "amenityType": "Shared, Not Available",
    "amenityPrice": "Free, Paid",
    "creationDate": "1/14/23 0:00"
    },
    {
    "_id": 15,
    "amenityName": "mailroom",
    "amenityType": "Shared, Not Available",
    "amenityPrice": "Free",
    "creationDate": "1/15/23 0:00"
    }
    ]
    cur = amenities.find()
    results = list(cur)
    if len(results) ==0:
        print("Empty collection for amenities: "+len(results))
        amenities.insert_many(amenities_list)
    else:
        amenities.drop()
        print("No of records deleted: ")
        amenities.insert_many(amenities_list)
    return "Success"

propertyTypes = db.propertyTypes
@app.route("/list/propertyTypes")
def list_propertyTypes():
    propertyTypes_list =[
        {
            "_id": 1,
            "propertyTypeName": "Apartment",
            "propertyTypeCategory": "Residential",
            "creationDate": "1/1/23 0:00"
        },
        {
            "_id": 2,
            "propertyTypeName": "Townhouse",
            "propertyTypeCategory": "Residential",
            "creationDate": "1/2/23 0:00"
        },
        {
            "_id": 3,
            "propertyTypeName": "Condos",
            "propertyTypeCategory": "Residential",
            "creationDate": "1/3/23 0:00"
        },
        {
            "_id": 4,
            "propertyTypeName": "Co-ops",
            "propertyTypeCategory": "Residential",
            "creationDate": "1/4/23 0:00"
        },
        {
            "_id": 5,
            "propertyTypeName": "Multifamily",
            "propertyTypeCategory": "Residential",
            "creationDate": "1/5/23 0:00"
        }

    ]
    cur = propertyTypes.find()
    results = list(cur)
    if len(results) ==0:
        print("Empty collection for propertyTypes: ",len(results))
        propertyTypes.insert_many(propertyTypes_list)
    else:
        propertyTypes.drop()
        print("Dropped the collection: propertyTypes")
        propertyTypes.insert_many(propertyTypes_list)
    return "Success"

nearbyLocations = db.nearbyLocationList
@app.route("/list/nearbyLocations")
def list_nearbyLocations():
    nearbyLocations_list =[
        {
            "_id": 1,
            "locationName": "John F. Kennedy International Airport",
            "locationDescription": "Airport",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 15.5,
            "creationDate": "1/1/23 0:00"
            },
            {
            "_id": 2,
            "locationName": "Newark Liberty International Airport",
            "locationDescription": "Airport",
            "locationCity": "New Jersey",
            "locationDistanceFromCityCenter": 5.5,
            "creationDate": "1/2/23 0:00"
            },
            {
            "_id": 3,
            "locationName": "LaGuardia Airport",
            "locationDescription": "Airport",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 20,
            "creationDate": "1/3/23 0:00"
            },
            {
            "_id": 4,
            "locationName": "PATH Station",
            "locationDescription": "Train Station",
            "locationCity": "New York, New Jersey",
            "locationDistanceFromCityCenter": 1,
            "creationDate": "1/4/23 0:00"
            },
            {
            "_id": 5,
            "locationName": "MTA Subway",
            "locationDescription": "Train Station",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 1,
            "creationDate": "1/5/23 0:00"
            },
            {
            "_id": 6,
            "locationName": "Grand Central Station",
            "locationDescription": "Rail Station, Bus Terminal",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 3,
            "creationDate": "1/6/23 0:00"
            },
            {
            "_id": 7,
            "locationName": "Pennsylvania Station",
            "locationDescription": "Rail Station, Bus Terminal",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 4,
            "creationDate": "1/7/23 0:00"
            },
            {
            "_id": 8,
            "locationName": "George Washington Bridge\n",
            "locationDescription": "Bridges and Tunnels",
            "locationCity": "New York, New Jersey",
            "locationDistanceFromCityCenter": 10,
            "creationDate": "1/8/23 0:00"
            },
            {
            "_id": 9,
            "locationName": "Holland Tunnel",
            "locationDescription": "Bridges and Tunnels",
            "locationCity": "New York, New Jersey",
            "locationDistanceFromCityCenter": 9.2,
            "creationDate": "1/9/23 0:00"
            },
            {
            "_id": 10,
            "locationName": "Lincoln Tunnel",
            "locationDescription": "Bridges and Tunnels",
            "locationCity": "New York, New Jersey",
            "locationDistanceFromCityCenter": 5.8,
            "creationDate": "1/10/23 0:00"
            },
            {
            "_id": 11,
            "locationName": "NYU Langone",
            "locationDescription": "Hospital",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 4,
            "creationDate": "1/11/23 0:00"
            },
            {
            "_id": 12,
            "locationName": "Hackensack Meridian Health",
            "locationDescription": "Hospital",
            "locationCity": "New Jersey",
            "locationDistanceFromCityCenter": 6.4,
            "creationDate": "1/12/23 0:00"
            },
            {
            "_id": 13,
            "locationName": "Staten Island Ferry terminal",
            "locationDescription": "Ferry Terminal",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 5,
            "creationDate": "1/13/23 0:00"
            },
            {
            "_id": 14,
            "locationName": "Liberty State Park",
            "locationDescription": "Park",
            "locationCity": "New Jersey",
            "locationDistanceFromCityCenter": 7,
            "creationDate": "1/14/23 0:00"
            },
            {
            "_id": 15,
            "locationName": "Central Park",
            "locationDescription": "Park",
            "locationCity": "New York",
            "locationDistanceFromCityCenter": 10,
            "creationDate": "1/15/23 0:00"
            }

    ]
    cur = nearbyLocations.find()
    results = list(cur)
    if len(results) ==0:
        print("Empty collection for nearbyLocations: ",len(results))
        nearbyLocations.insert_many(nearbyLocations_list)
    else:
        nearbyLocations.drop()
        print("Dropped the collection: nearbyLocations")
        nearbyLocations.insert_many(nearbyLocations_list)
    return "Success"

#if __name__ == '__main__':
 #   app.run(host='127.0.0.1', port=8080, debug=True)
