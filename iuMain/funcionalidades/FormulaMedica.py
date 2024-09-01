#Importar lo necesario...

public class FormulaMedica {
    static Scanner sc = new Scanner(System.in);

    public static void formulaMedica(Hospital hospital) {
        Paciente paciente = selectPatient(hospital);
        if (paciente == null) return;

        Enfermedad enfermedadTratar = selectDisease(paciente);
        if (enfermedadTratar == null) return;

        Doctor doctorEscogido = selectDoctor(paciente, enfermedadTratar, hospital);
        if (doctorEscogido == null) return;

        Formula formulaPaciente = createFormula(paciente, doctorEscogido, enfermedadTratar, hospital);

        if (formulaPaciente != null) {
            paciente.getHistoriaClinica().agregarFormula(formulaPaciente);
            System.out.println(formulaPaciente);
        }
    }

    private static Paciente selectPatient(Hospital hospital) {
        System.out.println("Ingrese la cédula del paciente: ");
        int cedula = sc.nextInt();
        sc.nextLine();
        Paciente paciente = hospital.buscarPaciente(cedula);
        if (paciente == null) {
            while (true) {
                System.out.println("El paciente no esta registrado.\n¿Desea registrarlo?");
                System.out.println("1. Si\n2. No \nSeleccione una opción");
                byte opcion = sc.nextByte();
                sc.nextLine();
                if (opcion == 1) {
                    RegistrarPaciente.registrarPaciente(hospital);
                    return null;
                } else if (opcion == 2) {
                    System.out.println("Adios");
                    return null;
                } else {
                    System.out.println("Opción Inválida");
                }
            }
        }
        return paciente;
    }

    private static Enfermedad selectDisease(Paciente paciente) {
        if (paciente.getHistoriaClinica().getEnfermedades().isEmpty()) {
            System.out.println("No hay enfermedades registradas, por favor diríjase a la sección de registrar enfermedades.");
            return null;
        }
        while (true) {
            System.out.println("¿Que enfermedad deseas tratar?");
            for (int i = 0; i < paciente.getHistoriaClinica().getEnfermedades().size(); i++) {
                System.out.println(i + 1 + "." + paciente.getHistoriaClinica().getEnfermedades().get(i));
            }
            byte opcEnf = sc.nextByte();
            sc.nextLine();
            if (opcEnf > 0 && opcEnf <= paciente.getHistoriaClinica().getEnfermedades().size()) {
                return paciente.getHistoriaClinica().getEnfermedades().get(opcEnf - 1);
            } else {
                System.out.println("Opción Inválida");
            }
        }
    }

    private static Doctor selectDoctor(Paciente paciente, Enfermedad enfermedadTratar, Hospital hospital) {
        ArrayList<Doctor> doctoresCita = paciente.getHistoriaClinica().buscarCitaDoc(enfermedadTratar.getEspecialidad(), hospital);
        if (doctoresCita.isEmpty()) {
            System.out.println("Ahora no contamos con doctores para tratar esta enfermedad. Lo sentimos mucho");
            return null;
        }
        while (true) {
            System.out.println("Los doctores que lo han atendido y están disponibles para formular " + enfermedadTratar.getNombre() + " " + enfermedadTratar.getTipologia() + " son: ");
            for (int i = 0; i < doctoresCita.size(); i++) {
                System.out.println(i + 1 + "." + doctoresCita.get(i).getNombre());
            }
            byte opcDoc = sc.nextByte();
            sc.nextLine();
            if (opcDoc > 0 && opcDoc <= doctoresCita.size()) {
                return doctoresCita.get(opcDoc - 1);
            } else {
                System.out.println("Opción inválida");
            }
        }
    }
}