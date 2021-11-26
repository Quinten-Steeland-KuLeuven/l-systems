import pytest

from ls_lSystem import generateLSystem

# ====================================
# ==== test setup ====================
# ====================================

def lSystem_test_one(iterations):
    axiom = "A" 
    rules = {
        "A": "B",
        "B": "AB"
    }
    translations = {
         "A": ["nop"],
         "B": ["nop"]
    }

    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

def lSystem_test_two(iterations):
    axiom = "F+F+F+F" 
    rules = {
        "F": "F+F-F-FF+F+F-F"
    }
    translations = {
         "F": ["nop"],
         "+": ["nop"],
         "-": ["nop"]
    }
    
    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

def lSystem_test_three(iterations):
    axiom = "A" 
    rules = {
        "A": "AB",
        "B": "A"
    }
    translations = {
         "A": ["nop"],
         "B": ["nop"]
    }

    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

def lSystem_test_four(iterations):
    axiom = "C" 
    rules = {
        "A": "AB",
        "B": "A",
        "C": ""
    }
    translations = {
         "A": ["nop"],
         "B": ["nop"],
         "C": ["nop"]
    }
    
    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

def lSystem_test_five(iterations):
    axiom = "A" 
    rules = {
        "A": "B+",
        "B": "C-",
        "C": "D",
        "D": "AEBECED",
        "E": "[D]"
    }
    translations = {
         "A": ["nop"],
         "B": ["nop"],
         "C": ["nop"],
         "D": ["nop"],
         "E": ["nop"],
         "[": ["nop"],
         "]": ["nop"],
         "+": ["nop"],
         "-": ["nop"]
    }
    
    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

def lSystem_test_six(iterations):
    axiom = "AC+" 
    rules = {
        "A": "B",
        "B": "AB",
        "C": ""
    }
    translations = {
         "A": ["nop"],
         "B": ["nop"],
         "C": ["nop"]
    }

    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

def lSystem_test_seven(iterations):
    axiom = "FAF" 
    rules = {
        "A": "B+",
        "B": "C-",
        "C": "D",
        "D": "AEBECEDF",
        "E": "[D]",
        "F": ""
    }
    translations = {
         "A": ["nop"],
         "B": ["nop"],
         "C": ["nop"],
         "D": ["nop"],
         "E": ["nop"],
         "F": ["nop"],
         "[": ["nop"],
         "]": ["nop"],
         "+": ["nop"],
         "-": ["nop"]
    }
    
    lSystem = generateLSystem(axiom, rules, translations, iterations)
    return lSystem

# ==========================================
# ==== actual tests ========================
# ==========================================

# === test 1 ===
def test_one_1():
    with open("./Unit_tests/test_1_answer.txt", "r") as readFile:
        anwser = readFile.readline()
    
    assert lSystem_test_one(30) == anwser.strip()

# === test 2 ===
def test_two_1():
    assert lSystem_test_two(1) == "F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F"
    
def test_two_2():
    assert lSystem_test_two(2) == "F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F-F+F-F-FF+F+F-FF+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F-F+F-F-FF+F+F-F"

# === test 3 ===
def test_three_1():
    assert lSystem_test_three(0) == "A"
    
def test_three_2():
    assert lSystem_test_three(1) == "AB"
        
def test_three_3():
    assert lSystem_test_three(2) == "ABA"
        
def test_three_4():
    assert lSystem_test_three(3) == "ABAAB"
        
def test_three_5():
    assert lSystem_test_three(4) == "ABAABABA"
        
def test_three_6():
    assert lSystem_test_three(5) == "ABAABABAABAAB"
        
def test_three_7():
    assert lSystem_test_three(6) == "ABAABABAABAABABAABABA"
        
def test_three_8():
    assert lSystem_test_three(7) == "ABAABABAABAABABAABABAABAABABAABAAB"

# === test 4 ===
def test_four_1():
    assert lSystem_test_four(0) == "C"
     
def test_four_2():
    assert lSystem_test_four(1) == ""
     
def test_four_3():
    assert lSystem_test_four(2) == ""

# === test 5 ===
def test_five_1():
    assert lSystem_test_five(0) == "A"
    
def test_five_2():
    assert lSystem_test_five(1) == "B+"
    
def test_five_3():
    assert lSystem_test_five(2) == "C-+"
    
def test_five_4():
    assert lSystem_test_five(3) == "D-+"
    
def test_five_5():
    assert lSystem_test_five(4) == "AEBECED-+"
    
def test_five_6():
    assert lSystem_test_five(5) == "B+[D]C-[D]D[D]AEBECED-+"
    
def test_five_7():
    assert lSystem_test_five(6) == "C-+[AEBECED]D-[AEBECED]AEBECED[AEBECED]B+[D]C-[D]D[D]AEBECED-+"
    
def test_five_8():
    assert lSystem_test_five(7) == "D-+[B+[D]C-[D]D[D]AEBECED]AEBECED-[B+[D]C-[D]D[D]AEBECED]B+[D]C-[D]D[D]AEBECED[B+[D]C-[D]D[D]AEBECED]C-+[AEBECED]D-[AEBECED]AEBECED[AEBECED]B+[D]C-[D]D[D]AEBECED-+"
    
# === test 6 ===
def test_six_1():
    assert lSystem_test_six(0) == "AC+"
    
def test_six_2():
    assert lSystem_test_six(1) == "B+"
    
def test_six_3():
    assert lSystem_test_six(2) == "AB+"
    
def test_six_4():
    assert lSystem_test_six(3) == "BAB+"
    
def test_six_5():
    assert lSystem_test_six(4) == "ABBAB+"
   
def test_six_6():
    assert lSystem_test_six(5) == "BABABBAB+"
    
def test_six_7():
    assert lSystem_test_six(6) == "ABBABBABABBAB+"
     
# === test 7 ===
def test_seven_1():
    assert lSystem_test_seven(0) == "FAF"
    
def test_seven_2():
    assert lSystem_test_seven(1) == "B+"
    
def test_seven_3():
    assert lSystem_test_seven(2) == "C-+"
    
def test_seven_4():
    assert lSystem_test_seven(3) == "D-+"
    
def test_seven_5():
    assert lSystem_test_seven(4) == "AEBECEDF-+"
    
def test_seven_6():
    assert lSystem_test_seven(5) == "B+[D]C-[D]D[D]AEBECEDF-+"
    
def test_seven_7():
    assert lSystem_test_seven(6) == "C-+[AEBECEDF]D-[AEBECEDF]AEBECEDF[AEBECEDF]B+[D]C-[D]D[D]AEBECEDF-+"
    
def test_seven_8():
    assert lSystem_test_seven(7) == "D-+[B+[D]C-[D]D[D]AEBECEDF]AEBECEDF-[B+[D]C-[D]D[D]AEBECEDF]B+[D]C-[D]D[D]AEBECEDF[B+[D]C-[D]D[D]AEBECEDF]C-+[AEBECEDF]D-[AEBECEDF]AEBECEDF[AEBECEDF]B+[D]C-[D]D[D]AEBECEDF-+"
    
    