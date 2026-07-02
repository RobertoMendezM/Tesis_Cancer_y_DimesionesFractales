/**
  * Acciones:
 * - Crea un Frame y utiliza "ArbolDePitagorasNoSimetrico30y60"
 *   para que dibuje el Árbol de Pitágoras a 30 y 60 grados
 * - Guarda la imagen en un archivo.  Espera a que la dibuje y mande el mensaje
 *   "Imagen guardada con éxito"

 * Referencias:
 *   -Gunter Saake Kai-Uwe Sattler (2021).
 *    Algorithmen and Datenstrukturen Eine Einführung mit Java
 *    Buchseite: 180 (lector)

 * Software:
 *        IDE IntelliJ IDEA 26.1.2
 *        Java 25

 * Editor: Roberto Méndez Méndez
 *
 * @version 7 Abril 22
 * editado   24 May 22
 *           11 Nov 2025
 *           2 Julio 2026   Guarda Imagen
 */

import fractalarbolpitagoras.ArbolPitagorasNoSimetrico30y60;
import guardagrafica.*;
import javax.swing.*;

void main() {
    SwingUtilities.invokeLater(() -> {
        JFrame frame = new ArbolPitagorasNoSimetrico30y60();

        //Tamaño del Frame
        frame.setSize(640, 500);
        frame.setTitle("Fractal. Árbol de Pitágoras a 30 y 60 grados");
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        // Posición del Frame
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

        CapturaFrameV2.guardaImagen(frame, "árbol_Pitágoras_30_60",5000);
    });
}
