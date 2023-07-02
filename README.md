# Simulating elevator transportation for an intentional time interval + simple GUI
## About model
- This model uses classes for passengers and elevators to create instances of each that store related data for them like the arrival time of passenger and state of the elevator at any time.
- A simple GUI is created utilizing the Tkinter package that shows the state of elevators (based on their colors), the number of passengers they are carrying, moving direction, and the floor they are, at the moment.
- Passengers are created randomly based on a Poisson distribution that you could see on papers.
- Elevators use a function to wait for more passengers to pick up or start moving. By deploying a Genetic Algorithm model on this model, we determined the parameters of that function so that the waiting time for passengers at peak time was minimum.

## How to run
- Install the required packages
- Open up application.py
- Tweak the parameters if you want
- run it!

You can watch a video of running this application on youtube [here](https://www.youtube.com/watch?v=J0lqZi_s7V0)
