from gestorAplicacion.servicios.Cita import Cita
from src.gestorAplicacion.servicios.CitaVacuna import CitaVacuna
from src.gestorAplicacion.servicios.Formula import Formula
from src.gestorAplicacion.servicios.Habitacion import Habitacion


#Elaborado por Jeronimo
class Pago:

    def calcular_precio(self, servicio):
        if isinstance(servicio, Formula):
            IVA = 1.19
            precio_total = 0
            for med in servicio.lista_meds:
                if self._tipo_eps == "Subsidiado":
                    precio_total += med.precio * 1.3
                if self._tipo_eps == "Contributivo":
                    precio_total += med.precio * 1.2
                if self._tipo_eps == "Particular":
                    precio_total += med.precio
            return precio_total * IVA

        elif isinstance(servicio, CitaVacuna):
            IVA = 0.19
            precio_total = servicio.vacuna.precio

            if servicio.vacuna.tipo == "Obligatoria":
                precio_total += 1000
            elif servicio.vacuna.tipo == "No obligatoria":
                precio_total += 3000

            tipo_eps = servicio.paciente.tipo_eps
            if tipo_eps == "Contributivo":
                precio_total += 2000
            elif tipo_eps == "Subsidiado":
                precio_total += 500
            elif tipo_eps == "Particular":
                precio_total += 10000

            precio_total *= (1 + IVA)
            return precio_total
        elif isinstance(servicio, Habitacion):
            IVA = 0.19
            precio_total = 0
            if self.tipo_eps == "Subsidiado":
                precio_total = self._habitacion_asignada.categoria.valor * 0
            elif self.tipo_eps == "Contributivo":
                precio_total = (self._habitacion_asignada.categoria.valor / 2) * self._habitacion_asignada.dias
            else:
                precio_total = self._habitacion_asignada.categoria.valor * self._habitacion_asignada.dias
            precio_total *= (1 + IVA)
            return precio_total

        elif isinstance(servicio, Cita):
            IVA = 0.19
            precio_total = 0
            tipo_eps = servicio.paciente.tipo_eps
            especialidad = servicio.doctor.especialidad

            if especialidad == "General":
                precio_total += 5000
            if especialidad == "Odontologia":
                precio_total += 10000
            if especialidad == "Oftalmologia":
                precio_total += 7000
            if tipo_eps == "Contributivo":
                precio_total += 2000
            if tipo_eps == "Subsidiado":
                precio_total += 500
            if tipo_eps == "Particular":
                precio_total += 10000

            precio_total *= (1 + IVA)
            return precio_total