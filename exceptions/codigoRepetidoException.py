
class CodigoRepetidoException(Exception):
    def __init__(self) -> None:
        super().__init__("Já existe um registro com este mesmo Código")
