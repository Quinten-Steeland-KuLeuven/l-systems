import pytest

from ls_config import getConfig

# ====================================
# ==== test setup ====================
# ====================================

def config_test(configFilename):
    variables, constants, axiom, rules, translations = getConfig(configFilename)
    return [variables, set(constants), axiom, rules, translations]

# ==========================================
# ==== actual tests ========================
# ==========================================

# === test 1 ===
def test_1():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/empty_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 2 ===
def test_2():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_json_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 3 ===
def test_3():
    assert config_test("./Unit_tests/no_rules_config.json") == [[], {"F", "G", "+", "-"}, "F-G-G", {}, {"F": ["draw", 20], "G": ["draw", 20], "+": ["angle", -120], "-": ["angle", 120]}]

# === test 4 ===
def test_4():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/no_translations_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 5 ===
def test_5():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/no_axiom_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 6 ===
def test_6():
    assert config_test("./Unit_tests/empty_axiom_config.json") == [["F", "G"], {"+", "-"}, "", {'F': 'GFG', 'G': 'F'}, {"F": ["draw", 20], "G": ["draw", 20], "+": ["angle", -120], "-": ["angle", 120]}]

# === test 7 ===
def test_7():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/unknown_axiom_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 8 ===
def test_8():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/unknown_char_in_rule_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 9 ===
def test_9():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/unknown_char_in_rule_2_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
    
# === test 10 ===
def test_10():
    assert config_test("./Unit_tests/invalid_translation_config.json") == [['F', 'G'], {'-', '+'}, 'F', {'F': 'GFG', 'G': 'F'}, {'F': ['draw', 20], 'G': ['{', "'", 'p', 'o', 'p', "'", '}'], '+': ['angle', -120], '-': ['angle', 120]}]
    
# === test 11 ===
def test_11():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/invalid_rule_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 12 ===
def test_12():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/invalid_rule_2_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
   
# === test 13 ===
def test_13():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/invalid_translation_2_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
     
# === test 14 ===
def test_14():
    assert config_test("./Unit_tests/bad_translations_1_config.json") == [['F', 'G'], {'-', '+'}, 'F', {'F': 'GFG', 'G': 'F'}, {'F': [], 'G': ['draw', 20], '+': ['angle', -120], '-': ['angle', 120]}]

# === test 15 ===
def test_15():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_2_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
       
# === test 16 ===
def test_16():
    assert config_test("./Unit_tests/bad_translations_3_config.json") == [['F', 'G'], {'-', '+'}, 'F', {'F': 'GFG', 'G': 'F'}, {'F': ["draw", 3.0], 'G': ['draw', 20], '+': ['angle', -120], '-': ['angle', 120]}]
 
# === test 17 ===
def test_17():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_4_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
       
# === test 18 ===
def test_18():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_5_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 19 ===
def test_19():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_6_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 20 ===
def test_20():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_7_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 21 ===
def test_21():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_8_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 22 ===
def test_22():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_9_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 23 ===
def test_23():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_10_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0

# === test 24 ===
def test_24():
    assert config_test("./Unit_tests/bad_translations_11_config.json") == [['F', 'G'], {'-', '+'}, 'F', {'F': 'GFG', 'G': 'F'}, {'F': ['draw', 3, 'color', '#ffbb42'], 'G': ['draw', 20], '+': ['angle', -45.0], '-': ['angle', 120]}]
 
# === test 25 ===
def test_25():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/bad_translations_12_config.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
    
# === test 26 ===
def test_26():
    assert config_test("./Unit_tests/test_1_config.json") == [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'], {'+', '-'}, 'ABCDEFGHIJKLMNOP', {'A': 'B', 'B': 'CB', 'C': 'BD', 'D': 'EB', 'E': 'BF', 'F': 'GB', 'G': 'BH', 'H': 'IB', 'I': 'BJ', 'J': 'KB', 'K': 'BL', 'L': 'MB', 'M': 'BN', 'N': 'OB', 'O': 'BP', 'P': 'A+'}, {'A': ['draw', 2.0, 'angle', 9.0], 'B': ['draw', 2.0, 'angle', 9.0], 'C': ['draw', 2.0, 'angle', 9.0], 'D': ['draw', 2.0, 'angle', 9.0], 'E': ['draw', 2.0, 'angle', 9.0], 'F': ['draw', 3, 'color', '#ffbb42'], 'G': ['draw', 20, 'color', 'navy'], 'H': ['draw', 2.0, 'angle', 9.0], 'I': ['draw', 2.0, 'angle', 9.0], 'J': ['draw', 2.0, 'angle', 9.0], 'K': ['draw', 2.0, 'angle', 9.0], 'L': ['draw', 2.0, 'angle', 9.0], 'M': ['draw', 2.0, 'angle', 9.0], 'N': ['draw', 2.0, 'angle', 9.0], 'O': ['draw', 2.0, 'angle', 9.0], 'P': ['draw', 2.0, 'angle', 9.0], '+': ['angle', -45.0], '-': ['angle', 120, 'lol']}]

# === test 27 ===
def test_27():
    assert config_test("./Unit_tests/test_2_config.json") == [['Q', 'C'], {'+', ']', '-', '/', '\\', '['}, '+Q-Q+Q-C+Q-Q+Q-C', {'Q': '+Q-Q+Q-C+Q-Q+Q-C', 'C': '/Q\\'}, {'Q': ['draw', 30], 'C': ['draw', 15], '+': ['color', 'darkgreen', 'angle', 45], '-': ['color', 'blue', 'angle', -60], '/': ['color', 'purple', 'angle', 5, 'draw', 60, 'angle', 5, 'draw', 60, 'angle', 5, 'draw', 60, 'angle', 5, 'draw', 60, 'angle', 5, 'draw', 60, 'angle', 5, 'draw', 60], '\\': ['color', 'violet', 'angle', -5, 'draw', 60, 'angle', -5, 'draw', 60, 'angle', -5, 'draw', 60, 'angle', -5, 'draw', 60, 'angle', -5, 'draw', 60, 'angle', -5, 'draw', 60], '[': ['push'], ']': ['pop']}]
    
# === test 28 ===
def test_28():
    assert config_test("./Unit_tests/test_3_config.json") == [['A'], {'[', '+', '-', ']'}, 'A', {'A': 'AA+[+A-A-A]-[-A+A+A]'}, {'A': ['draw', 10], '+': ['angle', 22.5], '-': ['angle', -22.5], '[': ['push'], ']': ['pop']}]
    
# === test 29 ===
def test_29():
    assert config_test("./Unit_tests/test_4_config.json") == [['F', 'G'], {'-', '+'}, 'F-G-G', {'F': 'F-G+F+G-F', 'G': 'GG'}, {'F': ['draw', 20], 'G': ['draw', 20], '+': ['angle', -120], '-': ['angle', 120]}]
   
# === test 30 ===
def test_30():
    assert config_test("./Unit_tests/test_5_config.json") == [['F', 'G'], {'-', '+'}, 'F', {'F': 'F+G', 'G': 'F-G'}, {'F': ['draw', 10], 'G': ['draw', 10], '+': ['angle', 90], '-': ['angle', -90]}]
    
# === test 31 ===
def test_31():
    assert config_test("./Unit_tests/test_6_config.json") == [['A'], {'+', '-'}, 'A', {'A': 'A+A-A-A+A'}, {'A': ['draw', 10], '+': ['angle', 90], '-': ['angle', -90]}]
    
# === test 32 ===
def test_32():
    assert config_test("./Unit_tests/test_7_config.json") == [['F', 'X'], {'+', '[', ']', '-'}, 'X', {'F': 'FF', 'X': 'F+[[X]-X]-F[-FX]+X'}, {'F': ['draw', 10], 'X': ['nop'], '+': ['angle', 25], '-': ['angle', -25], '[': ['push'], ']': ['pop']}]
    
# === test 33 ===
def test_33():
    with pytest.raises(SystemExit) as ex:
        config_test("./Unit_tests/thisfiledoesnotexist.pathdoesnotexis.txt.json")
    assert ex.type == SystemExit
    assert ex.value.code == 0
    
# === test 34 ===
def test_34():
    assert config_test("./Unit_tests/test_8_config.json") == [['0', '1'], {'+', '-'}, '0', {'0': '01', '1': '10'}, {'0': ['draw', 10], '1': ['nop'], '+': ['angle', 25], '-': ['angle', -25]}]
    
# === test 35 ===
def test_35():
    assert config_test("./Unit_tests/test_9_config.json") == [['0', '1'], {'-', '+'}, '0', {'0': '1', '1': '1+0'}, {'0': ['draw', 10.0], '1': ['draw', 15.5], '+': ['angle', 25.5], '-': ['angle', -25]}]
     
# === test 36 ===
def test_36():
    assert config_test("./Unit_tests/test_10_config.json") == [['0', '1', "A"], {'-', '+'}, 'A', {'0': '1', '1': '1+0', "A": "-0"}, {'0': ['draw', 10.0], '1': ['draw', 15.5], '+': ['angle', 25.5], '-': ['angle', -25], "A": ["angle", 0.5, "draw", 25.75]}]
    