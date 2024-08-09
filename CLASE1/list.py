class Nodo:
  def __init__(self, valor): # Captura entrada
      self.valor = valor
      self.siguiente = None

class LSL:
  def __init__(self):
    self.cabecera = None

  def insertar(self, valor):
    nuevo_nodo = Nodo(valor)
    if self.cabecera is None:
      self.cabecera = nuevo_nodo # Ingresar primer nodo
    else:
      nodo_actual = self.cabecera
      while nodo_actual.siguiente: # nodo.actual.siguiente != None
        nodo_actual = nodo_actual.siguiente # Asignar espacio de memoria
      nodo_actual.siguiente = nuevo_nodo # Reemplazar nuevo nodo en el espacio disponible de memoria
  
  def imprimir(self):
    if self.cabecera is None:
      print("La LSL está vacía")
    else:
      nodo_actual = self.cabecera
      while nodo_actual: # nodo.actual != None
        print(nodo_actual.valor, end = "->")
        nodo_Actual = nodo_actual.siguiente
      print("None")
  
  def buscar(self, x_obj):
    nodo_actual = self.cabecera
    pos = 0
    while nodo_actual: # nodo.actual != None
      if nodo_actual.valor == x_obj:
        print("El valor {:.0f} esta en la posición {:.0f}".format(nodo_actual.valor, pos)) #f => valor flotante  0 => entero
        return True
      nodo_actual = nodo_actual.siguiente
      pos += 1 # pos = pos + 1
    print("El valor no se encontró")
    return False