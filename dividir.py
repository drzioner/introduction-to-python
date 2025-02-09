import pytest

def dividir(a, b):
  if b == 0:
    raise ValueError("No se puede dividir entre cero")
  return a / b

def test_dividir_entre_cero():
  with pytest.raises(ValueError) as excinfo:
    dividir(10, 0)
  assert str(excinfo.value) == "No se puede dividir entre cero"