The script is one possible solution of the following exercise: 

4. Town
Create a class Town. The __init__ method should receive the name of the town. It should also have 3 more
methods:
 set_latitude(latitude) - set an attribute called latitude to the given one
 set_longitude(longitude) - set an attribute called longitude to the given one
 __repr__ - return representation of the object in the following string format:
"Town: {name} | Latitude: {latitude} | Longitude: {longitude}"
Example

Test Code Output

town = Town(&quot;Sofia&quot;)
town.set_latitude("42° 41' 51.04" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)

Town: Sofia | Latitude: 42° 41'
51.04" N | Longitude: 23° 19'
26.94" E



