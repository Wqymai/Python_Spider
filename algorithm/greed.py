# -*- coding:utf-8 -*-
# 贪婪算法(用于解决NP问题)

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        print 'station:',station,' states:',states
        covered = states_needed & states
        print 'covered:',covered
        print 'len(covered):',str(len(covered))," len(states_covered)",str(len(states_covered))
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
        print '>>>> best_station:',best_station
        print '>>>> states_covered:', states_covered
    print '='*50
    states_needed -= states_covered
    final_stations.add(best_station)
    print 'states_needed:',states_needed
    print 'final_stations:', final_stations
    print '='*50


# print final_stations

