#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:58:01 2020

@author: martins
"""
import Solitude_V3 as solitude


def is_draw_test():
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # draw with finished grid
    state2 = ['O','-','X','X','X','O','O','-','-', 'X'] # unfinished game
    state3 = ['O','X','O','O','X','O','X','X','X', 'O'] # win with finished grid
    state4 = ['O','-','X','O','X','-','X','O','X', 'O'] # win with empty grid
    state5 = ['X','O','X','X','O','X','O','O','O', 'X'] # loss with finished grid
    state6 = ['X','-','O','X','O','-','O','X','O', 'X'] # loss with empty grid
    

    
    case1 = solitude.is_draw(state1)
    case2 = solitude.is_draw(state2)
    case3 = solitude.is_draw(state3)
    case4 = solitude.is_draw(state4)
    case5 = solitude.is_draw(state5)
    case6 = solitude.is_draw(state6)
    
    
    score = 0
    failed = []
    if case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if not case3:
        score += 1
    else:
        failed.append('case3')
    if not case4:
        score += 1
    else:
        failed.append('case4')
    if not case5:
        score += 1
    else:
        failed.append('case5')
    if not case6:
        score += 1
    else:
        failed.append('case6')
    
    print("Test: is_draw(state)")
    print("      passed: " + str(score) + "/6 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()

def is_win_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # draw with finished grid
    state2 = ['O','-','X','X','X','O','O','-','-', 'X'] # unfinished game
    state3 = ['O','X','O','O','X','O','X','X','X', 'O'] # win with finished grid
    state4 = ['O','-','X','O','X','-','X','O','X', 'O'] # win with empty grid
    state5 = ['X','O','X','X','O','X','O','O','O', 'X'] # loss with finished grid
    state6 = ['X','-','O','X','O','-','O','X','O', 'X'] # loss with empty grid
    
    case1 = solitude.is_win(state1, player1)
    case2 = solitude.is_win(state1, player2)
    case3 = solitude.is_win(state2, player1)
    case4 = solitude.is_win(state2, player2)
    case5 = solitude.is_win(state3, player1)
    case6 = solitude.is_win(state3, player2)
    case7 = solitude.is_win(state4, player1)
    case8 = solitude.is_win(state4, player2)
    case9 = solitude.is_win(state5, player1)
    case10 = solitude.is_win(state5, player2)
    case11 = solitude.is_win(state6, player1)
    case12 = solitude.is_win(state6, player2)
    
    score = 0
    if case1:
        score += 1
    if case2:
        score += 1
    if not case3:
        score += 1
    if not case4:
        score += 1
    if case5:
        score += 1
    if not case6:
        score += 1
    if case7:
        score += 1
    if not case8:
        score += 1
    if not case9:
        score += 1
    if case10:
        score += 1
    if not case11:
        score += 1
    if case12:
        score += 1
    
    print("Test: is_win(state, player)")
    print("      passed: " + str(score) + "/10 test cases")
    print()
    
def is_a_way_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # draw with finished grid
    state2 = ['O','-','X','X','X','O','O','-','-', 'X'] # unfinished game, no way
    state3 = ['O','X','O','O','X','O','X','X','X', 'O'] # win with finished grid
    state4a = ['O','-','X','O','X','-','X','O','X', 'O'] # win with empty grid and a_way for winner
    state4b = ['X','X','X','O','O','-','-','-','-', 'O'] # win with empty grid and a_way for losser
    state5a = ['O','-','-','X','X','-','O','-','X', 'O'] # unfinished game, a_way X
    state5b = ['X','-','-','O','O','-','X','-','O', 'X'] # unfinished game, a_way O
    state6 = ['O','-','-','O','X','-','X','-','X', 'O'] # unfinished game, two_ways
    
    case1 = solitude.is_a_way(state1, player1) # return false
    case2 = solitude.is_a_way(state1, player2) # return false
    case3 = solitude.is_a_way(state2, player1) # return false
    case4 = solitude.is_a_way(state2, player2) # return false
    case5 = solitude.is_a_way(state3, player1) # return false
    case6 = solitude.is_a_way(state3, player2) # return false
    case7 = solitude.is_a_way(state4a, player1) # return false
    case8 = solitude.is_a_way(state4b, player2) # return false
    case9 = solitude.is_a_way(state5a, player1) # return true
    case10 = solitude.is_a_way(state5a, player2) # return false
    case11 = solitude.is_a_way(state5b, player1) # return false
    case12 = solitude.is_a_way(state5b, player2) # return true
    case13 = solitude.is_a_way(state6, player1) # return false
    case14 = solitude.is_a_way(state6, player2) # return false
    
    score = 0
    failed = []
    if not case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if not case3:
        score += 1
    else:
        failed.append('case3')
    if not case4:
        score += 1
    else:
        failed.append('case4')
    if not case5:
        score += 1
    else:
        failed.append('case5')
    if not case6:
        score += 1
    else:
        failed.append('case6')
    if not case7:
        score += 1
    else:
        failed.append('case7')
    if not case8:
        score += 1
    else:
        failed.append('case8')
    if case9:
        score += 1
    else:
        failed.append('case9')
    if not case10:
        score += 1
    else:
        failed.append('case10')
    if not case11:
        score += 1
    else:
        failed.append('case11')
    if case12:
        score += 1
    else:
        failed.append('case12')
    if not case13:
        score += 1
    else:
        failed.append('case13')
    if not case14:
        score += 1
    else:
        failed.append('case14')
    
    print("Test: is_a_way(state, player)")
    print("      passed: " + str(score) + "/14 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()

def is_two_ways_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # draw with finished grid
    state2 = ['O','-','X','X','X','O','O','-','-', 'X'] # unfinished game, no way
    state3 = ['O','X','O','O','X','O','X','X','X', 'O'] # win with finished grid
    state4 = ['O','-','-','X','X','-','O','-','X', 'O'] # unfinished game, a_way X
    state5 = ['O','-','O','-','X','-','X','X','-', 'O'] # two_ways, possible loss X
    state6 = ['X','O','O','-','X','-','X','-','-', 'O'] # two_ways, sure win X
    state7 = ['O','O','O','X','X','-','X','-','-', 'X'] # loss with empty grid and a_way X
    state8 = ['X','O','O','-','X','O','X','-','X', 'O'] # win with empty grid and two_ways X
    state9 = ['X','O','O','-','-','O','X','-','X', 'X'] # three_ways, sure win X
    
    case1 = solitude.is_two_ways(state1, player1) # return false
    case2 = solitude.is_two_ways(state2, player1) # return false
    case3 = solitude.is_two_ways(state2, player2) # return false
    case4 = solitude.is_two_ways(state3, player1) # return false
    case5 = solitude.is_two_ways(state4, player1) # return false
    case6 = solitude.is_two_ways(state5, player1) # return true
    case7 = solitude.is_two_ways(state6, player1) # return true
    case8 = solitude.is_two_ways(state7, player1) # return false
    case9 = solitude.is_two_ways(state8, player1) # return false
    case10 = solitude.is_two_ways(state9, player1) # return true
    
    score = 0
    failed = []
    if not case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if not case3:
        score += 1
    else:
        failed.append('case3')
    if not case4:
        score += 1
    else:
        failed.append('case4')
    if not case5:
        score += 1
    else:
        failed.append('case5')
    if case6:
        score += 1
    else:
        failed.append('case6')
    if case7:
        score += 1
    else:
        failed.append('case7')
    if not case8:
        score += 1
    else:
        failed.append('case8')
    if not case9:
        score += 1
    else:
        failed.append('case9')
    if case10:
        score += 1
    else:
        failed.append('case10')
    
    print("Test: is_two_ways(state, player)")
    print("      passed: " + str(score) + "/10 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def end_state_test():
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # draw with finished grid
    state2 = ['O','-','X','X','X','O','O','-','-', 'X'] # unfinished game
    state3 = ['O','X','O','O','X','O','X','X','X', 'O'] # win with finished grid
    state4 = ['O','-','X','O','X','-','X','O','X', 'O'] # win with empty grid
    state5 = ['X','O','X','X','O','X','O','O','O', 'X'] # loss with finished grid
    state6 = ['X','-','O','X','O','-','O','X','O', 'X'] # loss with empty grid
    state7 = ['','','','','','','','','', 'X'] # empty grid
    
    case1 = solitude.end_state(state1) # return true
    case2 = solitude.end_state(state2) # return false
    case3 = solitude.end_state(state3) # return true
    case4 = solitude.end_state(state4) # return true
    case5 = solitude.end_state(state5) # return true
    case6 = solitude.end_state(state6) # return true
    case7 = solitude.end_state(state7) # return false
    
    score = 0
    failed = []
    if case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if case3:
        score += 1
    else:
        failed.append('case3')
    if case4:
        score += 1
    else:
        failed.append('case4')
    if case5:
        score += 1
    else:
        failed.append('case5')
    if case6:
        score += 1
    else:
        failed.append('case6')
    if case7:
        score += 1
    else:
        failed.append('case7')
    
    print("Test: end_state(state)")
    print("      passed: " + str(score) + "/7 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def has_center_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # center X
    state2 = ['X','O','O','O','O','X','X','X','O', 'O'] # center O
    state3 = ['X','O','O','O','-','X','X','X','O', 'O'] # empty center
    
    case1 = solitude.has_center(state1, player1) # return true
    case2 = solitude.has_center(state1, player2) # return false
    case3 = solitude.has_center(state2, player1) # return false
    case4 = solitude.has_center(state2, player2) # return true
    case5 = solitude.has_center(state3, player1) # return false
    case6 = solitude.has_center(state3, player2) # return false
    
    score = 0
    failed = []
    if case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if not case3:
        score += 1
    else:
        failed.append('case3')
    if case4:
        score += 1
    else:
        failed.append('case4')
    if not case5:
        score += 1
    else:
        failed.append('case5')
    if not case6:
        score += 1
    else:
        failed.append('case6')
    
    print("Test: has_center(state, focus)")
    print("      passed: " + str(score) + "/6 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def has_corner_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # corner X
    state2 = ['X','O','O','O','X','X','O','X','O', 'O'] # corner O
    state3 = ['-','O','-','O','X','X','-','X','-', 'O'] # empty corner
    
    case1 = solitude.has_corner(state1, player1) # return true
    case2 = solitude.has_corner(state1, player2) # return true
    case3 = solitude.has_corner(state2, player1) # return true
    case4 = solitude.has_corner(state2, player2) # return true
    case5 = solitude.has_corner(state3, player1) # return false
    case6 = solitude.has_corner(state3, player2) # return false
    
    score = 0
    failed = []
    if case1:
        score += 1
    else:
        failed.append('case1')
    if case2:
        score += 1
    else:
        failed.append('case2')
    if case3:
        score += 1
    else:
        failed.append('case3')
    if case4:
        score += 1
    else:
        failed.append('case4')
    if not case5:
        score += 1
    else:
        failed.append('case5')
    if not case6:
        score += 1
    else:
        failed.append('case6')
    
    print("Test: has_corner(state, focus)")
    print("      passed: " + str(score) + "/6 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def has_edge_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # edge X
    state2 = ['X','O','O','O','X','X','O','X','O', 'O'] # edge O
    state3 = ['X','-','O','-','X','-','O','-','O', 'X'] # empty edge
    
    case1 = solitude.has_edge(state1, player1) # return true
    case2 = solitude.has_edge(state1, player2) # return true
    case3 = solitude.has_edge(state2, player1) # return true
    case4 = solitude.has_edge(state2, player2) # return true
    case5 = solitude.has_edge(state3, player1) # return false
    case6 = solitude.has_edge(state3, player2) # return false
    
    score = 0
    failed = []
    if case1:
        score += 1
    else:
        failed.append('case1')
    if case2:
        score += 1
    else:
        failed.append('case2')
    if case3:
        score += 1
    else:
        failed.append('case3')
    if case4:
        score += 1
    else:
        failed.append('case4')
    if not case5:
        score += 1
    else:
        failed.append('case5')
    if not case6:
        score += 1
    else:
        failed.append('case6')
    
    print("Test: has_edge(state, focus)")
    print("      passed: " + str(score) + "/6 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def corner_avail_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # corner X
    state2 = ['X','O','O','O','X','X','O','X','O', 'O'] # corner O
    state3 = ['-','O','-','O','X','X','-','X','-', 'O'] # empty corner
    state4 = ['X','O','O','O','X','X','-','X','O', 'O'] # one corner available
    
    case1 = solitude.corner_avail(state1) # return false
    case2 = solitude.corner_avail(state2) # return false
    case3 = solitude.corner_avail(state3) # return true
    case4 = solitude.corner_avail(state4) # return true
    
    score = 0
    failed = []
    if not case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if case3:
        score += 1
    else:
        failed.append('case3')
    if case4:
        score += 1
    else:
        failed.append('case4')
    
    print("Test: corner_avail(state)")
    print("      passed: " + str(score) + "/4 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def center_avail_test():
    player1 = 'X'
    player2 = 'O'
    state1 = ['X','O','O','O','X','X','X','X','O', 'O'] # corner X
    state2 = ['X','O','O','O','X','X','O','X','O', 'O'] # corner O
    state3 = ['X','O','O','O','-','X','X','X','O', 'O'] # empty corner
    
    case1 = solitude.center_avail(state1) # return false
    case2 = solitude.center_avail(state2) # return false
    case3 = solitude.center_avail(state3) # return true
    
    score = 0
    failed = []
    if not case1:
        score += 1
    else:
        failed.append('case1')
    if not case2:
        score += 1
    else:
        failed.append('case2')
    if case3:
        score += 1
    else:
        failed.append('case3')
    
    print("Test: center_avail(state)")
    print("      passed: " + str(score) + "/3 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
def static_value_test():
    maxi = 'X'
    mini = 'O'
    state1 = ['-','-','X','-','X','-','X','-','-', 'O'] # is_win maxi
    state2 = ['-','X','-','X','X','-','-','-','-', 'O'] # is_two_ways + has_center
    state3 = ['-','-','-','-','X','-','X','-','-', 'O'] # is_a_way + has_corner + has_center
    state4 = ['-','-','-','-','X','-','-','-','-', 'O'] # has_center maxi
    state5 = ['-','-','-','-','-','-','X','-','-', 'O'] # has_corner mini
    state6 = ['-','-','O','-','O','-','O','-','-', 'X'] # is_win mini
    state7 = ['O','-','X','-','O','-','O','-','-', 'X'] # is_two_ways + has_center + has_corner mini + has_corner maxi
    state8 = ['-','-','-','-','-','O','-','-','O', 'X'] # is_a_way + has_corner mini
    state9 = ['-','-','-','-','O','-','-','-','-', 'X'] # has_center mini
    state10 = ['-','-','-','-','-','-','O','-','-', 'X'] # has_corner mini
    state11 = ['X','O','-','X','O','-','X','-','-', 'O'] # is_win maxi + is_a_way mini
    state12 = ['X','O','-','X','O','-','X','O','-', 'O'] # is_win maxi + is_win mini
    state13 = ['X','-','O','-','X','-','X','-','-', 'O'] # is_two_ways has_center + has_corner mini + has_corner maxi
    state14 = ['O','-','O','O','X','-','X','X','X', 'O'] # is_win maxi + ...
    state15 = ['O','O','X','X','X','O','O','X','X', 'O'] # corner + center both draw game
    state16 = ['O','X','O','O','X','X','X','O','X', 'O'] # corner + center both draw game
    state17 = ['X','O','X','-','X','O','O','-','X', 'O'] # is_win maxi + ...
    state18 = ['O','X','X','O','O','-','O','-','X', 'X'] # is_win mini + ...
    state19 = ['X','-','O','X','O','-','X','O','X', 'O'] # is_win maxi + ...
    state20 = ['X','-','O','O','O','-','X','X','X', 'O'] # is_win maxi + ...
    
    case1 = solitude.static_value(state1, maxi, mini) # 100
    case2 = solitude.static_value(state2, maxi, mini) # 55
    case3 = solitude.static_value(state3, maxi, mini) # 16
    case4 = solitude.static_value(state4, maxi, mini) # 5
    case5 = solitude.static_value(state5, maxi, mini) # 1
    case6 = solitude.static_value(state6, maxi, mini) # -100
    case7 = solitude.static_value(state7, maxi, mini) # -55
    case8 = solitude.static_value(state8, maxi, mini) # -11
    case9 = solitude.static_value(state9, maxi, mini) # -5
    case10 = solitude.static_value(state10, maxi, mini) # -1
    case11 = solitude.static_value(state11, maxi, mini) # 100
    case12 = solitude.static_value(state12, maxi, mini) # 100
    case13 = solitude.static_value(state13, maxi, mini) # 55
    case14 = solitude.static_value(state14, maxi, mini) # 100
    case15 = solitude.static_value(state15, maxi, mini) # 0
    case16 = solitude.static_value(state16, maxi, mini) # 0
    case17 = solitude.static_value(state17, maxi, mini) # 100
    case18 = solitude.static_value(state18, maxi, mini) # -100
    case19 = solitude.static_value(state19, maxi, mini) # 100
    case20 = solitude.static_value(state20, maxi, mini) # 100
    
    score = 0
    failed = []
    if case1 == 100:
        score += 1
    else:
        failed.append('case1')
    if case2 == 55:
        score += 1
    else:
        failed.append('case2')
    if case3 == 16:
        score += 1
    else:
        failed.append('case3')
    if case4 == 5:
        score += 1
    else:
        failed.append('case4')
    if case5 == 1:
        score += 1
    else:
        failed.append('case5')
    if case6 == -100:
        score += 1
    else:
        failed.append('case6')
    if case7 == -55:
        score += 1
    else:
        failed.append('case7')
    if case8 == -11:
        score += 1
    else:
        failed.append('case8')
    if case9 == -5:
        score += 1
    else:
        failed.append('case9')
    if case10 == -1:
        score += 1
    else:
        failed.append('case10')
    if case11 == 100:
        score += 1
    else:
        failed.append('case11')
    if case12 == 100:
        score += 1
    else:
        failed.append('case12')
    if case13 == 55:
        score += 1
    else:
        failed.append('case13')
    if case14 == 100:
        score += 1
    else:
        failed.append('case14')
    if case15 == 0:
        score += 1
    else:
        failed.append('case15')
    if case16 == 0:
        score += 1
    else:
        failed.append('case16')
    if case17 == 100:
        score += 1
    else:
        failed.append('case17')
    if case18 == -100:
        score += 1
    else:
        failed.append('case18')
    if case19 == 100:
        score += 1
    else:
        failed.append('case19')
    if case20 == 100:
        score += 1
    else:
        failed.append('case20')
        
    print("Test: static_value(state)")
    print("      passed: " + str(score) + "/20 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()

def get_all_next_moves_test():
    maxi = 'X'
    mini = 'O'
    state1 = ['O','-','-','X','X','O','O','-','X', 'X'] # normal maxi
    state2 = ['O','X','O','-','X','-','X','O','-', 'X'] # normal maxi
    state3 = ['X','O','-','X','X','-','-','-','O', 'O'] # normal mini
    state4 = ['-','-','X','-','O','O','O','X','X', 'X'] # normal maxi
    state5 = ['O','X','X','-','O','-','O','-','-', 'X'] # normal maxi
    state6 = ['O','O','X','X','X','O','O','X','X', 'O'] # outlier mini
    state7 = ['X','X','O','O','O','X','X','O','O', 'X'] # outlier maxi
    state8 = ['-','-','-','-','-','-','-','-','-', 'X'] # normal maxi
    state9 = ['X','O','-','X','X','O','X','-','O', 'O'] # outlier mini
    state10 = ['O','X','-','O','O','X','O','-','X', 'X'] # outlier maxi
    
    case1 = solitude.get_all_next_moves(state1, maxi, mini) # 3
    case2 = solitude.get_all_next_moves(state2, maxi, mini) # 3
    case3 = solitude.get_all_next_moves(state3, maxi, mini) # 4
    case4 = solitude.get_all_next_moves(state4, maxi, mini) # 3
    case5 = solitude.get_all_next_moves(state5, maxi, mini) # 4
    case6 = solitude.get_all_next_moves(state6, maxi, mini) # *
    case7 = solitude.get_all_next_moves(state7, maxi, mini) # *
    case8 = solitude.get_all_next_moves(state8, maxi, mini) # 9
    case9 = solitude.get_all_next_moves(state9, maxi, mini) # *
    case10 = solitude.get_all_next_moves(state10, maxi, mini) # *
    
    score = 0
    failed = []
    if len(case1) == 3:
        score += 1
    else:
        failed.append('case1')
    if len(case2) == 3:
        score += 1
    else:
        failed.append('case2')
    if len(case3) == 4:
        score += 1
    else:
        failed.append('case3')
    if len(case4) == 3:
        score += 1
    else:
        failed.append('case4')
    if len(case5) == 4:
        score += 1
    else:
        failed.append('case5')
    if len(case6) == 0:
        score += 1
    else:
        failed.append('case6')
    if len(case7) == 0:
        score += 1
    else:
        failed.append('case7')
    if len(case8) == 9:
        score += 1
    else:
        failed.append('case8')
    if len(case9) == 0:
        score += 1
    else:
        failed.append('case9')
    if len(case10) == 0:
        score += 1
    else:
        failed.append('case10')
    
    print("Test: get_all_next_moves(state, maxi, mini)")
    print("      passed: " + str(score) + "/10 test cases")
    if failed:
        print("      failed cases:")
        for case in failed:
            print("                  ", case)
    print()
    
    cases = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10]
    for i in range(0,len(cases)):
        if len(cases[i]) != 0:
            print("Test case " + str(i+1) + ":")
            for s in cases[i]:
                print("    ", s)

def game_test():
    state1 = ['X','O','-','-','X','-','O','X','O', 'X']
    # max choices:
    state1a = ['X','O','X','-','X','-','O','X','O', 'O']
    state1b = ['X','O','-','X','X','-','O','X','O', 'O']
    state1c = ['X','O','-','-','X','X','O','X','O', 'O']
    # min choices:
    state1aA = ['X','O','X','-','X','O','O','X','O', 'X']
    state1aB = ['X','O','X','O','X','-','O','X','O', 'X']
    state1bA = ['X','O','O','X','X','-','O','X','O', 'X']
    state1bB = ['X','O','-','X','X','O','O','X','O', 'X']
    state1cA = ['X','O','O','-','X','X','O','X','O', 'X']
    state1cB = ['X','O','-','O','X','X','O','X','O', 'X']
    # max choices:
    state1aA1 = ['X','O','X','X','X','O','O','X','O', 'O']
    state1aB1 = ['X','O','X','O','X','X','O','X','O', 'O']
    state1bA1 = ['X','O','O','X','X','X','O','X','O', 'O']
    state1bB1 = ['X','O','X','X','X','O','O','X','O', 'O']
    state1cA1 = ['X','O','O','X','X','X','O','X','O', 'O']
    state1cB1 = ['X','O','X','O','X','X','O','X','O', 'O']
    
    statebug = ['X','-','O','-','X','-','-','O','-', 'X']


if __name__ == '__main__':
    is_draw_test()
    is_win_test()
    is_a_way_test()
    is_two_ways_test()
    end_state_test()
    has_center_test()
    has_corner_test()
    has_edge_test()
    corner_avail_test()
    center_avail_test()
    static_value_test()
    get_all_next_moves_test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    