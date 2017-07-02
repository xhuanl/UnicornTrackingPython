This application prints the result of the closest points to the designated point.

It contains the following files:

main.py:

    The entry point of the application. It reads, parses and validates the input, calls the 
search.py to search the points and print out the results.

point.py:

    This class represents the points with co-ordinates. It also has a distance member to record 
the distance of to the designated point. The member is not actually the distance but the square 
of the distance because it saves the time to run sqrt() and also it keeps the member as an integer. 

searchResult.py:

    This class represents the actual result to be printed after the search. It uses a list to 
store the results and the list is sorted as we are using the method similar to the Insertation sort 
to add a new point. The new point can only be inserted to the list if the distance from that point
is among the closest ones to the designated point.

search.py:

    This class parses the input file, creates points and calculate the distances. The distance
of a new point is compared with the distances of the existing points in the list. If the distance
of the new point is less thn a point, the new point will be added and the existing point with the 
longest distance will be removed.

input.txt:

    The sample input file for the points.

output.txt:

    The result of running the application using the sample input.

To run the program, use the following command:

On Widows:

    python.exe "C:\Code\Python\Unicorn\UnicornTrackingPython\src\main.py"
     -i "C:\Code\Python\Unicorn\UnicornTrackingPython\input.txt"
     -p "(1, 0, 0)" -c 5 -o "C:\Code\Python\Unicorn\UnicornTrackingPython\output.txt"

On CentOS:

    python /root/Unicorn/UnicornTrackingPython/src/main.py -i /root/Unicorn/UnicornTrackingPython/input.txt 
    -p "(1, 0, 0)" -c 5 -o /root/Unicorn/UnicornTrackingPython/output.txt

Where

/root/Unicorn/UnicornTrackingPython/src/main.py is the entry point of the program


/root/Unicorn/UnicornTrackingPython/input.txt is the input file which contains all the points.

"(1, 0, 0)" is the designated point from which the rest points to be calculated. Need to be quoted.

5 is the expected amount of points to be found. Do not need to be quoted.

/root/Unicorn/UnicornTrackingPython/output.txt is the output file of the search result. 


Discussion:

The program loops through all the points in the input file, calculates the distance of each point 
immediately so that those points with longer distances will be dropped. The information for those dropped 
points will not use the memory. The big O for this operation is O(n) where n is the number of 
the points listed in the input file. The invalid input will be dropped.

After creating a point object for each point, the distance of the new point will be compared with the
distances of the existing points in the list. If the distance is less than a point, the new point
will be inserted to the list. As the maximum size of the list is the size of the expected points to be printed,
the big O of this operation will be O(m) where m is the expected number of the closest points.

The total big O would be O(mn).

