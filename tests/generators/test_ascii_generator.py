import os
import sys
import pytest
from ascii_generator import ascii_generator
from PIL import Image

def test_pallette_display(capsys):
    ag = ascii_generator.AsciiGenerator(' !0')
    ag.pallette_display()
    captured = capsys.readouterr()

    results = captured.out
    results_array = results.split(os.linesep)
    assert len(results_array) == 257
    assert results_array[0] == '0 =>  '
    assert results_array[85] == '85 =>  '
    assert results_array[86] == '86 => !'
    assert results_array[170] == '170 => !'
    assert results_array[171] == '171 => 0'
    assert results_array[255] == '255 => 0'
    assert results_array[256] == ''


def test_generate_with_defaults():
    generator = ascii_generator.AsciiGenerator()
    results = generator.generate(Image.open('tests/fixtures/test.png'))
    assert len(results.as_text()) == 10000


def test_generate_with_parameters():
    pass
