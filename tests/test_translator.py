from scripts.atomese2metta.translator import Expression, MList, MSet, Symbol, Translator

def test_given_a_Expression_instance_then_should_return_a_string_with_parentheses():
    assert str(Expression()) == '()'

def test_given_a_MList_instance_then_should_return_a_string_with_brackets():
    assert str(MList()) == '()'

def test_given_a_MSet_instance_then_should_return_a_string_with_curly_brackets():
    assert str(MSet()) == '{}'