import json
import sys

VERSION = "versión 1.2"


class JSONReaderSingleton:
    """
    Clase que implementa un patrón Singleton para leer un archivo JSON.
    """
    def __new__(cls, file_path):
        """
        Método para crear una única instancia de la clase.
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
            cls._instance.file_path = file_path
            cls._instance.banks_info = cls._instance._load_banks_info()
        return cls._instance

    def _load_banks_info(self):
        """
        Método para cargar la información de los bancos desde el archivo JSON.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as myfile:
                data = myfile.read()
            json_obj = json.loads(data)
            return json_obj.get("bancos", {})
        except FileNotFoundError:
            print(f"Error del programa: El archivo {self.file_path} no se encontró.")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Error del programa: El archivo no es un JSON válido.")
            sys.exit(1)

    def get_banks_info(self):
        """
        Método para obtener la información de los bancos.
        """
        return self.banks_info


class Bank:
    """
    Clase que representa un banco.
    """
    def __init__(self, name, initial_balance, token):
        self.name = name
        self.balance = initial_balance
        self.token = token

    def can_process(self, amount):
        """
        Verifica si el banco puede procesar el pago.
        """
        return self.balance >= amount

    def process_payment(self, amount):
        """
        Procesa el pago restando el monto del saldo del banco.
        """
        if self.can_process(amount):
            self.balance -= amount
            return True
        return False

    def get_payment_info(self, amount):
        """
        Retorna la información del pago.
        """
        return {
            'bank_name': self.name,
            'amount': amount,
            'token': self.token
        }

    def __str__(self):
        return f"Banco {self.name} - Saldo: {self.balance} - Token: {self.token}"


class Payment:
    """
    Clase que representa un pago realizado.
    """
    def __init__(self, order_number, bank_name, amount, token):
        self.order_number = order_number
        self.bank_name = bank_name
        self.amount = amount
        self.token = token

    def __str__(self):
        return (f"Pedido {self.order_number}: Banco {self.bank_name}, "
                f"Monto {self.amount}, Token {self.token}")


class PaymentHistory:
    """
    Clase que mantiene el historial de pagos.
    """
    def __init__(self):
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)

    def __iter__(self):
        """
        Método para iterar sobre los pagos en el historial.
        """
        return iter(self.payments)


class PaymentHandler:
    """
    Clase que maneja la cadena de responsabilidad para el procesamiento de pagos.
    """
    def __init__(self, bank, successor=None):
        self.bank = bank
        self.successor = successor

    def handle(self, amount, order_number, payment_history):
        """
        Maneja el pago tratando de procesarlo con el banco actual.
        Si no puede, pasa la solicitud al sucesor.
        """
        if self.bank.process_payment(amount):
            payment_info = self.bank.get_payment_info(amount)
            payment = Payment(order_number, payment_info['bank_name'], amount, payment_info['token'])
            payment_history.add_payment(payment)
            print(f"Pago de {amount} procesado por {self.bank.name}. Nuevo saldo: {self.bank.balance}")
            return True
        if self.successor is not None:
            return self.successor.handle(amount, order_number, payment_history)
        print(f"Error: No se pudo procesar el pago de {amount}. Saldo insuficiente.")
        return False


class BankChain:
    """
    Clase que construye y maneja la cadena de responsabilidad de bancos.
    """
    def __init__(self, banks):
        self.chain = None
        for bank in banks:
            self.chain = PaymentHandler(bank, self.chain)

    def process_payment(self, amount, order_number, payment_history):
        """
        Procesa el pago a través de la cadena de responsabilidad.
        """
        if self.chain is not None:
            return self.chain.handle(amount, order_number, payment_history)
        print("Error: No hay bancos disponibles para procesar el pago.")
        return False


class Program:
    """
    Clase que representa el programa principal.
    """
    def __init__(self, bank_chain, payment_history):
        """
        Constructor de la clase Program.
        """
        self.bank_chain = bank_chain
        self.payment_history = payment_history
        self.order_number = 0

    def run(self, option, amount=None):
        """
        Método principal que ejecuta el programa.
        """
        try:
            if option == "auto":
                if amount is None:
                    print("Error: Se requiere un monto para la opción 'auto'.")
                    sys.exit(1)
                self.order_number += 1
                self.bank_chain.process_payment(float(amount), self.order_number, self.payment_history)
            elif option == "list":
                make_multiple_payments(self)
            else:
                print("Error: Opción no válida.")
                print_usage()
                sys.exit(1)
        except Exception as err:
            print(f"Error del programa: {err}")
            sys.exit(1)


def make_multiple_payments(program):
    """
    Función para realizar múltiples pagos y almacenarlos en el historial de pagos.
    """
    try:
        for _ in range(5):
            program.order_number += 1
            amount = 500.0  # Monto predeterminado
            program.bank_chain.process_payment(amount, program.order_number, program.payment_history)
    except ValueError:
        print("Error: El monto ingresado no es válido.")


def print_usage():
    """
    Función para imprimir el mensaje de uso del programa.
    """
    print("Uso: python programa.py <archivo_json> <opcion> [<monto>]")
    print("Opciones:")
    print("  auto           - Seleccionar automáticamente un banco para procesar el pago proporcionando el monto del pago.")
    print("  list           - Realizar múltiples pagos y almacenarlos en el historial de pagos.")
    print("Ejemplo: python programa.py archivo.json auto 100.0")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == '-v':
        print(f"Versión del programa: {VERSION}")
        sys.exit(0)

    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print_usage()
        sys.exit(0)

    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Error del programa: Número de argumentos inválido.")
        print_usage()
        sys.exit(1)

    json_file_path = sys.argv[1]
    option = sys.argv[2]
    payment_amount = sys.argv[3] if len(sys.argv) == 4 else None

    try:
        # Inicializa los bancos con sus respectivos saldos y tokens
        bank1 = Bank("Galicia", 1000.0, "token1")
        bank2 = Bank("Entre Rios", 2000.0, "token2")

        # Construye la cadena de responsabilidad
        bank_chain = BankChain([bank1, bank2])

        # Inicializa el historial de pagos
        payment_history = PaymentHistory()

        # Ejecuta el programa
        program = Program(bank_chain, payment_history)
        program.run(option, payment_amount)
    except Exception as err:
        print(f"Error del programa: {err}")
        sys.exit(1)
