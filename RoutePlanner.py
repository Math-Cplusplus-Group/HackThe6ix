#
#  RoutePlanner.py
#  HackThe6ix
#
#  Created by Jeffrey, Maliha, Justin  and Lennart on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import Map

class RoutePlanner:
    """ Class that find the route that each car should take """
    m = Map.Map()
    path = []
    def setMap(self, m):
        self.m = m
        
    # This function returns the list of intersections
    # that leads from start to finish on the map m
<<<<<<< HEAD
    def calcCoarseRoute(self, start, finish):
        result = []
        return result

    # This function calculates the fine route dependent
    # on the previously computed coarse route
    def calcFineRoute(self, coarse):
        result = []
=======
    def find_shortest_Route(self, start, finish, m, path):
        path = path + [start]
        if start == finish:
            return path
        result = None
        for street in self.m.streets:
            if street[0] == start:
                if street[1] not in path:
                    newpath = RoutePlanner.find_shortest_Route(street[1], end, m, path)
                    if newpath:
                        if not result or len(newpath) < len(result):
                            result = newpath
>>>>>>> bdc6f3ae84a7f5682efba8fb904feaefba1bc9f0
        return result
