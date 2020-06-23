#!/usr/bin/env python3

import math
import sys

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    return solution

def opt2(solution,cities):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    solution_length=len(solution)
    solution.append(0)
    # length = sum(distance(cities[u], cities[v]) for u, v in zip(cities, cities[1:] + cities[0:1]))

    while 1:
        length = sum(dist[solution[i]][solution[i+1]] for i in range(solution_length))

        for i in range(solution_length):
            for j in range(i+2, solution_length):
                if dist[solution[i]][solution[i+1]] + dist[solution[j]][solution[j+1]] > dist[solution[i]][solution[j]] + dist[solution[i+1]][solution[j+1]]:
                    solution[i+1:j+1] = reversed(solution[i+1:j+1])
        after_length = sum(dist[solution[i]][solution[i+1]] for i in range(solution_length))
        if after_length>=length:
            break
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    cities=read_input(sys.argv[1])
    solution = solve(cities)
    solution = opt2(solution, cities)
    print_solution(solution)
