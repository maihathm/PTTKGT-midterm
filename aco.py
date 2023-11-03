"""
Choosing the next path based on  =>
    The probabilities of choosing edge (i,j) = t(i,j)^a * l(i,j)^b / total sum of t(i,j)^a * l(i,j)^b
        Where t => pheromone level on the edge (i, j)
              l => quality of the edge = 1/(length of the edge)
              a,b = increase or decrease the impact of t and l
    Then, use the probabilities to choose the next path (edge) with the ROULETTE WHEEL technique:
        Calculating the cumulative sum of the probabilities
        Generate a random number between 1 and 0
        The path (edge) to choose depends on the interveal where the random number generated belongs

"""

'''

Updating pheromones : 
    If kth ant travels on the edge (i, j) then 
                        pheromone that the kth ant deposits on this edge(i,j) = 1/Lk (Lk is the total length of the kth ant tour )
    Otherwise 0

    The Pheromone level on an edge  : 
        without vaporization => total of the pheromones deposited by each ant 
        with vaporization => total of the pheromones deposited by each ant plus 
                                [(1-p)*current pheromone level on the edge] (p is the evaporation rate)
        using the reforencement of the global best tour => when each tour is completed, we add a certein amount of pheromones to the best 
            tour we got till now => adding e.1/Lk pheromones to every edge that compose the best tour (where e is the reinforcement factor 
            a positive integer and Lk is the total length of the best tour) this process is one of the daemon actions
            that we can perform to an ACO to get better results  

    
'''

import data
import functions

# Graph (list of the cities, their neighbors, the distance and pheromone level between each neighbors)
graph = data.graphGR17
graphCopy = graph.copy()
# algorithm parameters
startCity, evaporationRate, antsNumber, a, b, bestTours = '633', 0.5, 50000, 1, 1, []
# parameter used to improve aco performances
asParameter, acsParameter = 4, .3
for i in range(0, antsNumber):
    currentCity = startCity
    visitedCities = [startCity]
    totalDistance = 0
    isHamiltonian = True
    while (len(visitedCities) < len(graph) and isHamiltonian):
        candidateCities = functions.getCandidateCities(graph.get(currentCity), visitedCities)
        if len(candidateCities) > 0:
            nextCity = functions.getNextCity(candidateCities, a, b, acsParameter)
            currentCity = nextCity.get('name')
            totalDistance += nextCity.get('distance')
            visitedCities.append(currentCity)
        else:
            isHamiltonian = False
    if isHamiltonian:
        isHamiltonian = False
        for city in graph.get(currentCity):
            if city.get('name') == startCity:
                totalDistance += city.get('distance')
                visitedCities.append(city.get('name'))
                isHamiltonian = True
                break
        if isHamiltonian:
            # print(f'Visited cities : {visitedCities}')
            found = False
            for tour in bestTours:
                if tour['name'] == visitedCities:
                    tour['count'] += 1
                    found = True
            if found == False:
                bestTours.append({'name': visitedCities, 'total distance': totalDistance, 'count': 1})
            functions.updatePheromones(graph, graphCopy, totalDistance, visitedCities, evaporationRate, bestTours,
                                       asParameter)

# print('----------------------')
bestTours.sort(key=lambda x: x['count'], reverse=False)
# for tour in bestTours:
#     print(f'{tour} \n')
bestTours.sort(key=lambda x: x['total distance'], reverse=False)
print(bestTours[0])
