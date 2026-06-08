/**
 * Curso: Programación
 * <p>
 * Crea un Frame y utiliza "ArbolDePitagorasNoSimetrico30y60"
 * para que dibuje el Árbol de Pitágoras a 30 y 60 grados
 * <p>
 * Tema: JFrame Básico
 * <p>
 * Editado de:
 * Buch: Gunter Saake Kai-Uwe Sattler (2021).
 * Algorithmen and Datenstrukturen Eine Einführung mit Java
 * Buchseite: 180 (lector)
 * <p>
 * Software: Java 25
 * <p>
 * Editor: Roberto Méndez Méndez
 *
 * @version 7 Abril 22
 * editado   24 May 22
 * 11 Nov 2025
 */

import javax.swing.*;

void main() {
    JFrame frame = new ArbolPitagorasNoSimetrico30y60();
    // Posición inicial del Frame
    frame.setLocation(50, 10);
    //Tamaño del Frame
    frame.setSize(640, 500);
    frame.setTitle("Fractal. Árbol de Pitágoras a 30 y 60 grados");
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    frame.setVisible(true);
}
