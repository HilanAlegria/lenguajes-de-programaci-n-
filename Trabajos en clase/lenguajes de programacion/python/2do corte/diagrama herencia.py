from abc import ABC, abstractmethod

# -------------------------------
# Clase abstracta Empleado
# -------------------------------
class Empleado(ABC):
    def __init__(self, nombre: str, id_empleado: int):
        self.nombre = nombre
        self.id_empleado = id_empleado

    @abstractmethod
    def calcular_pago(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, id_empleado: int, salario_mensual: float):
        super().__init__(nombre, id_empleado)
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.salario_mensual


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre: str, id_empleado: int, horas: int, tarifa: float):
        super().__init__(nombre, id_empleado)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas * self.tarifa


# -------------------------------
# Clase abstracta Notificación
# -------------------------------
class Notificacion(ABC):
    def __init__(self, mensaje: str, destinatario: str):
        self.mensaje = mensaje
        self.destinatario = destinatario

    @abstractmethod
    def enviar(self):
        pass


class NotificacionEmail(Notificacion):
    def enviar(self):
        print("📧 EMAIL")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")
        print("------------------\n")


class NotificacionSMS(Notificacion):
    def enviar(self):
        print("📱 SMS")
        print(f"Para: {self.destinatario}")
        print(f"Mensaje: {self.mensaje}")
        print("------------------\n")


# -------------------------------
# Ejemplo de integración
# -------------------------------
if __name__ == "__main__":
    # Crear empleados
    emp1 = EmpleadoTiempoCompleto("Ana", 1, 3000)
    emp2 = EmpleadoPorHoras("Luis", 2, 120, 25)

    # Calcular sus pagos
    pago1 = emp1.calcular_pago()
    pago2 = emp2.calcular_pago()

    # Crear notificaciones (se heredan los métodos abstractos)
    noti1 = NotificacionEmail(f"Hola {emp1.nombre}, tu pago es ${pago1}.", "ana@email.com")
    noti2 = NotificacionSMS(f"Hola {emp2.nombre}, tu pago es ${pago2}.", "+123456789")

    # Enviar notificaciones
    noti1.enviar()
    noti2.enviar()
