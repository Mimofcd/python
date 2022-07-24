When Brunel worked on the design and construction of the SS Great Britain ship, most engine powered ships of the time used paddle wheels. His first design for this large iron hull ship was also based on using paddle wheels on both sides of the hull, however Brunel soon found out that using a propeller would be more effective and therefore he changed his design halfway through the construction stage! Once the decision was approved, one of Brunel’s next decisions was to choose how many blades to use for the propeller.

To assist him with the technical drawing of the propeller, Brunel used the following formula: angle=360/noofbladefa-spin
Your task is to write a function called calculateAngle() that takes one parameter, the number of blades of a propeller (as a positive integer value). Your function will calculate and return the inner angle between two adjacent blades (in degrees).

A viaduct is a specific type of bridge that consists of a series of arches, piers or columns supporting a long elevated railway or road. When working on the Great Western Railway (GWR) linking Bristol to London, Brunel designed several viaducts, each with a different length, height and number of arches. The Wharncliffe viaduct 📷 is a great example of his work. Built in 1837, it was the first railway viaduct to be built with hollow piers. It is 270 meters long and consists of eight arches.
Supposing that each arch has the same width, we can calculate the width of an arch as follows: width=length of viaduct/number of arches

Your task is to write a function called calculateArchWidth() that takes two parameters, the length of the viaduct in meters and the number of arches (both parameters being given as positive integers). Your function will calculate and return the width of an arch.

When designing the Great Western Railway (GWR), one of the main objectives of Brunel was to design a fairly straight route as level as possible in order to promote high speed travel on the line. To do so Brunel had to estimate the percent slope (gradient) of every section of the route to avoid steep slops.

Here is the formula that Brunel used to calculate the percent slope of every section of his planned route:
slope=delta h/delta x *100
Your task is to write a function called calculatePercentSlope() that takes two parameters: delta_x (Δx) and delta_h (Δh), the difference in coordinates and altitudes between the starting and ending position of a section. Your function will use these two parameters to calculate and return the percent slope of the section.

One of Brunel’s most famous project is the Clifton Suspension Bridge, Bristol’s most impressive structure. He started to design this project at the age of 24. The bridge took 33 years to complete!
One of the mathematical puzzle that Brunel had to solve, was to estimate the length of the main arc of the suspension bridge. This arc consists of wrought iron chains to support the load of the main deck as well as the extra load due to the traffic across the bridge. The arc joins the two towers on each side of the river Avon. The two towers are separated by 214 meters and are rising 26m above deck level. The deck itself is 75m above the high water mark!

The following mathematical formulas can be used to calculate the arc length based on the distance between the two towers (l) and the height of each tower (from the deck level) (h) radius=h/2*l^2/8h
                                                   theta=2*sin^-1(1/2radius)
                                                   arc length=2*pi*r*theta/360
Your task is to write a function called calculateArcLength() that takes two parameters: the length (l) and the height (from the deck level) (h) of the suspension bridge. Your function will use these two parameters to calculate and return the length or the arc of the bridge.