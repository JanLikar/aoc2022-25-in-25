#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits.h>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>

typedef std::vector<std::string> Grid;
typedef std::pair<uint, uint> Coordinates;
typedef std::vector<Coordinates> CoordinatesVector;
typedef std::map<Coordinates, uint> Distances;
typedef std::pair<uint, Coordinates> MinQueueItem;
typedef std::priority_queue<MinQueueItem, std::vector<MinQueueItem>, std::greater<MinQueueItem>> MinQueue;

CoordinatesVector findChar(Grid &g, char c) {
    CoordinatesVector vec;

    for (uint i = 0; i < g.size(); i++)
        for (uint j = 0; j < g[i].length(); j++)
            if (g[i][j] == c)
                vec.push_back(std::make_pair(i, j));

    return vec;
}

int getHeight(Grid &grid, Coordinates coords) {
    auto y = coords.first;
    auto x = coords.second;

    switch (grid[y][x]) {
        case 'S':
            return (int) 'a';
            break;
        case 'E':
            return (int) 'z';
            break;    
    }

    return (int) grid[y][x];
}

CoordinatesVector getReachableCoordinates(Grid &grid, Coordinates current_position, bool in_reverse) {
    CoordinatesVector candidates;
    auto y = current_position.first;
    auto x = current_position.second;
    auto max_y = grid.size() - 1;
    auto max_x = grid[0].length() - 1;

    if (y > 0)
        candidates.push_back(std::make_pair(y - 1, x));
    
    if (y < max_y)
        candidates.push_back(std::make_pair(y + 1, x));

    if (x > 0)
        candidates.push_back(std::make_pair(y, x - 1));

    if (x < max_x)
        candidates.push_back(std::make_pair(y, x + 1));

    CoordinatesVector filtered;

    if (in_reverse) {
        std::copy_if(
            candidates.begin(),
            candidates.end(),
            std::back_inserter(filtered),
            [&grid, current_position](Coordinates other) -> bool {
                return getHeight(grid, other) + 1 >= getHeight(grid, current_position);
            }
        );
    }
    else {
        std::copy_if(
            candidates.begin(),
            candidates.end(),
            std::back_inserter(filtered),
            [&grid, current_position](Coordinates other) -> bool {
                return 1 >= getHeight(grid, other) - getHeight(grid, current_position);
            }
        );
    };

    return filtered;
}

Distances getDistances(Grid &grid, Coordinates start, bool in_reverse = false) {
    std::set<Coordinates> visited;
    MinQueue pqueue;
    Distances distances;

    distances[start] = 0;
    pqueue.push(std::make_pair(0, start));

    while (pqueue.size() > 0) {
        auto item = pqueue.top();
        pqueue.pop();
        auto coordinates = item.second;

        visited.insert(coordinates);

        auto neighbours = getReachableCoordinates(grid, coordinates, in_reverse);

        for (Coordinates neighbour : neighbours) {
            const bool already_visited = visited.find(neighbour) != visited.end();
            if (already_visited) {
                continue;
            }

            auto pos = distances.find(neighbour);
            if (pos == distances.end()) {
                distances.emplace(neighbour, UINT_MAX);
            }

            auto old_dist = distances[neighbour];
            auto new_dist = distances[coordinates] + 1;

            if (new_dist < old_dist) {
                distances[neighbour] = new_dist;
                pqueue.push(std::make_pair(new_dist, neighbour));
            }
        }
    }

    return distances;
}

int main() {
    std::ifstream inFile("input.txt");
    std::string line;
    Grid grid;

    while (std::getline(inFile, line))
        grid.push_back(line);

    auto dists = getDistances(grid, findChar(grid, 'S')[0]);

    auto shortest_distance = dists[findChar(grid, 'E')[0]];
    

    std::cout << shortest_distance << "\n";

    auto reverse_distances = getDistances(grid, findChar(grid, 'E')[0], true);

    auto min = UINT_MAX;
    for (auto a_coordinate: findChar(grid, 'a')) {
        auto pos = reverse_distances.find(a_coordinate);
        if (pos == reverse_distances.end())
            continue;

        if (pos->second < min) {
            min = pos->second;
        }
    }

    std::cout << min << "\n";

    return 0;
}
