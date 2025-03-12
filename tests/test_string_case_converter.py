import pytest
from src.string_case_converter import to_snake_case

def test_camel_case_conversion():
    assert to_snake_case("helloWorld") == "hello_world"
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("hello2World") == "hello2_world"

def test_pascal_case_conversion():
    assert to_snake_case("HelloWorld") == "hello_world"
    assert to_snake_case("TestCaseExample") == "test_case_example"

def test_kebab_case_conversion():
    assert to_snake_case("hello-world") == "hello_world"
    assert to_snake_case("test-case-example") == "test_case_example"

def test_space_separated_conversion():
    assert to_snake_case("hello world") == "hello_world"
    assert to_snake_case("Hello World") == "hello_world"

def test_mixed_punctuation_conversion():
    assert to_snake_case("hello-world!test") == "hello_world_test"
    assert to_snake_case("hello_world test") == "hello_world_test"
    assert to_snake_case("hello@world#test") == "hello_world_test"

def test_already_snake_case():
    assert to_snake_case("hello_world") == "hello_world"
    assert to_snake_case("snake_case_example") == "snake_case_example"

def test_empty_string():
    assert to_snake_case("") == ""

def test_single_word():
    assert to_snake_case("hello") == "hello"
    assert to_snake_case("World") == "world"

def test_error_handling():
    with pytest.raises(TypeError):
        to_snake_case(None)
    with pytest.raises(TypeError):
        to_snake_case(123)

def test_complex_cases():
    assert to_snake_case("HTTPResponse") == "http_response"
    assert to_snake_case("OpenAIModel") == "open_ai_model"
    assert to_snake_case("URL2API") == "url2_api"