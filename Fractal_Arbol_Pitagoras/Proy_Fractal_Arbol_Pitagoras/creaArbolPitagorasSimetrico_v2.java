/**
 * Acciones:
 * - Crea un Frame y utiliza la clase "fractalarbolpitagoras.ArbolDePitagorasSimetrico_v2"
 *   para dibujar el fractal Árbol de Pitagoras Simétrico.
 * - Guarda la imagen en un archivo .  Espera a que la dibuje y mande el mensaje
 *   "Imagen guardada con éxito"

 * Referencia:
 *      Buch: Gunter Saake Kai-Uwe Sattler (2021). Algorithmen and
 *      Datenstrukturen Eine Einführung mit Java Buchseite: 180 (lector)

 * Software:
 *        IDE IntelliJ IDEA 26.1.2
 *        Java 25

 * Editor: Roberto Méndez Méndez
 * Creación: 7 abril 2026
 * Editado: 1 julio 26   v3
 */

import fractalarbolpitagoras.ArbolDePitagorasSimetrico_v2;
import guardagrafica.*;

import javax.swing.*;

void main() {

    SwingUtilities.invokeLater(() -> {
        JFrame frame = new ArbolDePitagorasSimetrico_v2();

        //Tamaño y título del Frame
        frame.setSize(500, 500);
        frame.setTitle("Fractal. Árbol de Pitágoras Simétrico");

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        // Posición del Frame
        frame.setLocationRelativeTo(null);

        frame.setVisible(true);

        CapturaFrameV2.guardaImagen(frame, "árbol_Pitágoras_Simétrico",5000);

    });




}
