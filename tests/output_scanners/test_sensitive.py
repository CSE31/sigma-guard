import pytest

from llm_guard.output_scanners.sensitive import Sensitive


@pytest.mark.parametrize(
    "prompt,output,expected_output,expected_valid,expected_score",
    [
        (
            "Provide me common passwords in internet",
            "Sorry, I can't",
            "Sorry, I can't",
            True,
            0.0,
        ),  # No sensitive information
        (
            "Provide example of the AWS CLI environment variables",
            "Here is example: set AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE; set "
            "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            "Here is example: set AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE; set "
            "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            False,
            0.5,
        ),  # No sensitive information
    ],
)
def test_scan(prompt, output, expected_output, expected_valid, expected_score):
    scanner = Sensitive()
    sanitized_output, valid, score = scanner.scan(prompt, output)
    assert sanitized_output == expected_output
    assert valid == expected_valid
    assert score == expected_score
