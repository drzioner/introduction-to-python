import pytest

from mi_modulo import sumar

@pytest.mark.parametrize("a, b, resultado_esperado", [
  (2, 3, 5),
  (0, 5, 5),
  (-2, 3, 1),
])
def test_sumar(a, b, resultado_esperado):
  assert sumar(a, b) == resultado_esperado