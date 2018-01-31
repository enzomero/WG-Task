# -*- coding: utf-8 -*-
import datadiff

# main scenario
def ut_mainScenario():
    lv_data = {'a' : {'a1' : 1,'a2' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    lv_dataSec = {'a' : {'a1' : 0,'a2' : 2,}, 'b' : {'b1' : {'b11' : 0,'b12' : 2,},}}
    return verdict(lv_data, lv_dataSec, {'a': {'a1': 0}, 'b': {'b1': {'b11': 0}}})

# TC if we have not any difference
def ut_noDiffiriance():
    lv_data = {'a' : {'a1' : 1,'a2' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    lv_dataSec = {'a' : {'a1' : 1,'a2' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    return verdict(lv_data, lv_dataSec)

# TC change key with value
def ut_changeKey():
    lv_data = {'a' : {'a1' : 1,'a2' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    lv_dataSec = {'a' : {'a1' : 1,'a3' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    return verdict(lv_data, lv_dataSec, 'Can\'t find the key')

# TC remove key with value
def ut_changeStructRemove():
    lv_data = {'a' : {'a1' : 1,'a2' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    lv_dataSec = {'a' : {'a1' : 1,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    return verdict(lv_data, lv_dataSec, 'Can\'t find the key')

# TC add key with value
def ut_changeStructAdd():
    lv_data = {'a' : {'a1' : 1,'a2' : 2,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    lv_dataSec = {'a' : {'a1' : 1,'a2' : 2,'a3' : 1,}, 'b' : {'b1' : {'b11' : 1,'b12' : 2,},}}
    return verdict(lv_data, lv_dataSec, {'a': {'a3': 1}})

# p_data        - base value of data
# p_dataSec     - changed data
# p_expect      - expected difference
def verdict(p_data, p_dataSec, p_expect = {}):
    print p_data
    print p_dataSec
    print 'Expect:'
    print p_expect
    print 'Got:'
    vl_got = datadiff.getChanges(p_data, p_dataSec)
    print vl_got
    print 'Verdict:'
    if vl_got == p_expect :
        return 'pass\n'
    else :
        return 'fail\n'

def control():
    print ut_mainScenario()
    print ut_noDiffiriance()
    print ut_changeKey()
    print ut_changeStructRemove()
    print ut_changeStructAdd()

control()
input('')
