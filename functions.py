from random import random
from random import randrange


def removeCityIfExist(citiesList, city):
    for c in citiesList:
        if c.get('name') == city:
            citiesList.remove(c)
            break


def getCandidateCities(candidatesCities, alreadyVisitedCities):
    finalList = candidatesCities.copy()
    for city in alreadyVisitedCities:
        removeCityIfExist(finalList, city)
    return finalList


def getNextCity(candidatesCities, a, b, acsParameter):
    rand = random()
    if rand <= (1 - acsParameter):
        totalProbabilities = 0.0
        edegsProbabilities = []
        if len(candidatesCities) == 1:
            edegsProbabilities.append(1)
        else:
            for city in candidatesCities:
                totalProbabilities += (city.get('pheromones') ** a * (1 / city.get('distance')) ** b)
            if totalProbabilities == 0: return candidatesCities[randrange(len(candidatesCities))]
            for city in candidatesCities:
                edegsProbabilities.append(
                    (city.get('pheromones') ** a * (1 / city.get('distance')) ** b) / totalProbabilities)
        cummulativeSum(edegsProbabilities)
        edegsProbabilities.append(0)
        randomNum = random()
        x = binary_search_iterative(edegsProbabilities, randomNum)
        indexX = edegsProbabilities.index(x)
        if x < randomNum:
            indexX -= 1
        return candidatesCities[indexX]
    else:
        nextCity = candidatesCities[0]
        maxProd = (nextCity.get('pheromones') * (1 / nextCity.get('distance')) ** b)
        for i in range(1, len(candidatesCities)):
            prod = candidatesCities[i].get('pheromones') * (1 / candidatesCities[i].get('distance')) ** b
            if prod > maxProd:
                maxProd = prod
                nextCity = candidatesCities[i]
        return nextCity


def updateEdgePheromone(citiesList, city, pheromoneToAdd, fact=1):
    for c in citiesList:
        if c.get('name') == city:
            c['pheromones'] += pheromoneToAdd * fact


def pheromoneEvaporation(graph, evaporationRate):
    for c1 in graph:
        for c2 in graph[c1]:
            c2['pheromones'] = (1 - evaporationRate) * c2['pheromones']


def globalBestReinforcement(graph, tours, reinforcementFactor=1):
    bestTour = tours[0].get('name')
    totalDistance = tours[0].get('total distance')
    for i in range(0, len(bestTour) - 1):
        updateEdgePheromone(graph.get(bestTour[i]), bestTour[i + 1], reinforcementFactor * 1 / totalDistance)
        updateEdgePheromone(graph.get(bestTour[i + 1]), bestTour[i], reinforcementFactor * 1 / totalDistance)


def updatePheromones(graph, graphCopy, totalDistance, visitedCities, evaporationRate, tours, asParameter):
    tours.sort(key=lambda x: x['total distance'], reverse=False)
    graph = graphCopy.copy()

    w = asParameter if len(tours) > asParameter else len(tours)
    for j in range(0, w - 1):
        # evaporization
        pheromoneEvaporation(graph, evaporationRate)
        r = j + 1
        # deposit pheromones
        for i in range(0, len(tours[j]['name']) - 1):
            updateEdgePheromone(graph.get(tours[j]['name'][i]), tours[j]['name'][i + 1], 1 / tours[j]['total distance'],
                                w - r)
            updateEdgePheromone(graph.get(tours[j]['name'][i + 1]), tours[j]['name'][i], 1 / tours[j]['total distance'],
                                w - r)
    globalBestReinforcement(graph, tours, w)

    # for i in range(0, len(visitedCities)-1):
    #     updateEdgePheromone(graph.get(visitedCities[i]) , visitedCities[i+1], 1/totalDistance)
    #     updateEdgePheromone(graph.get(visitedCities[i+1]) , visitedCities[i], 1/totalDistance)
    # global best tour reinforcement
    # globalBestReinforcement(graph, tours, reinforcementFactor)


def cummulativeSum(probabilities):
    probabilities.reverse();
    cummulativeSum = 0
    for i in range(0, len(probabilities)):
        cummulativeSum += probabilities[i]
        probabilities[i] = cummulativeSum
    probabilities.reverse()
    probabilities[0] = round(probabilities[0])
    return probabilities


def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0
    arrayClone = array.copy()
    arrayClone.reverse()
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2

        if element == arrayClone[mid]:
            return arrayClone[mid]

        if element < arrayClone[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return arrayClone[mid]


test = 3
