#include <iostream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <numeric>

using namespace std;

// Function to find the next floor with a request
int FindNextRequestFloor(vector<int> requests, int currentPosition)
{
    int nextFloor = -1;
    for (int i = currentPosition + 1; i < requests.size(); i++) {
        if (requests[i] > 0) {
            nextFloor = i;
            break;
        }
    }
    return nextFloor;
}

// Function to print the lift movements and stops
void PrintResults(vector<int> passengerCount, int currentPosition)
{
    cout << "Lift movements and stops:" << endl;
    for (int i = 0; i < passengerCount.size(); i++) {
        if (passengerCount[i] > 0) {
            cout << "Stopped at floor " << i << " with " << passengerCount[i] << " passengers" << endl;
        }
    }
    cout << "Reached ground floor" << endl;
}

int main()
{
    int N, C, P;
    vector<int> requests;

    // Read inputs
    cout << "Enter the number of floors: ";
    cin >> N;
    cout << "Enter the lift capacity: ";
    cin >> C;
    cout << "Enter the number of passengers: ";
    cin >> P;

    // Read passenger requests
    cout << "Enter the passenger requests for each floor: " << endl;
    for (int i = 0; i < N; i++) {
        int request;
        cin >> request;
        requests.push_back(request);
    }

    // Initialize variables
    int currentPosition = 0;
    int currentPassengers = 0;
    vector<int> passengerCount(N, 0);
    string liftStatus = "idle";

    // Loop until all passenger requests are served
    while (accumulate(passengerCount.begin(), passengerCount.end(), 0) < P) {
        // Check liftStatus and move accordingly
        if (liftStatus == "idle") {
            // Find the next floor with a request
            int nextFloor = FindNextRequestFloor(requests, currentPosition);
            // If nextFloor found, move to the floor
            if (nextFloor != -1) {
                currentPosition = nextFloor;
                liftStatus = "serving";
            } else {
                // No more requests
                break;
            }
        } else if (liftStatus == "serving") {
            // Update passengers and requests
            requests[currentPosition]--;
            currentPassengers++;
            passengerCount[currentPosition]++;

            // Check lift capacity
            if (currentPassengers == C) {
                liftStatus = "dropping";
            }
        }
        if (liftStatus == "dropping") {
            // Move to the ground floor
            currentPosition = 0;
            liftStatus = "idle";
            currentPassengers = 0;
        }
    }

    // Print lift movements and stops
    PrintResults(passengerCount, currentPosition);

    return 0;
}
