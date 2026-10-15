// Archivo complementario en C++ para demostrar el cálculo de indicadores de la encuesta.
// La página web se construye con HTML, CSS, Bootstrap y Python/Flask.
// Este programa se ejecuta por separado y no es necesario para abrir el sitio.

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int respuestas = 100;
    const int interes_plataforma = 67;
    const int acepta_ia = 47;
    const int tal_vez_ia = 21;
    const int dificil_elegir = 24;
    const int muy_dificil_elegir = 21;

    double porcentaje_interes = (interes_plataforma * 100.0) / respuestas;
    double porcentaje_ia_potencial = ((acepta_ia + tal_vez_ia) * 100.0) / respuestas;
    double porcentaje_dificultad = ((dificil_elegir + muy_dificil_elegir) * 100.0) / respuestas;

    cout << fixed << setprecision(1);
    cout << "AURABEAUTY - Indicadores de encuesta" << endl;
    cout << "Respuestas analizadas: " << respuestas << endl;
    cout << "Interes en una sola plataforma: " << porcentaje_interes << "%" << endl;
    cout << "Aceptacion o interes potencial en IA: " << porcentaje_ia_potencial << "%" << endl;
    cout << "Personas que reportan dificultad alta: " << porcentaje_dificultad << "%" << endl;
    cout << "\nNota: indicadores calculados a partir de los porcentajes compartidos por el equipo." << endl;
    return 0;
}
