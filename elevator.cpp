#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

class Elevator {
public:
    Elevator(int max_floor, int capacity) : max_floor(max_floor), capacity(capacity) {}

    void add_request(int from, int to) {
        requests.push_back({from, to});
    }

    void process_requests() {
        sort_requests();
        int current_floor = 1;
        for (const auto& request : requests) {
            int from = request.first;
            int to = request.second;
            travel_time += std::abs(current_floor - from) + std::abs(from - to);
            current_floor = to;

            std::cout << "From floor " << from << " to floor " << to << std::endl;
            std::cout << "Travel time: " << travel_time << std::endl;
        }
    }

private:
    void sort_requests() {
        std::sort(requests.begin(), requests.end());
    }

    int max_floor;
    int capacity;
    int travel_time = 0;
    std::vector<std::pair<int, int>> requests;
};

int main() {
    Elevator elevator(10, 5);

    elevator.add_request(1, 5);
    elevator.add_request(4, 9);
    elevator.add_request(3, 7);
    elevator.add_request(6, 2);
    elevator.add_request(8, 10);

    std::cout << "Processing elevator requests..." << std::endl;
    elevator.process_requests();

    return 0;
}

