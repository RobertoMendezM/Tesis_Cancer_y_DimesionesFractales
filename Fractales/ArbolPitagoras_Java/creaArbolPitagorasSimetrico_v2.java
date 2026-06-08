/**
 * Curso: Programación
 *
 * Crea un Frame y utiliza la clase "ArbolDePitagorasSimetrico_v2"
 * para dibujar el fractal Árbol de Pitagoras Simétrico
 *
 * Objetivos: Tema 5.Herencia y manejo de swing.JFrame elemental
 *
 * Referencia:
 *      Buch: Gunter Saake Kai-Uwe Sattler (2021). Algorithmen and
 *      Datenstrukturen Eine Einführung mit Java Buchseite: 180 (lector)
 *
 * Software:
 *        IDE IntelliJ IDEA 26.1.2
 *        Java 25
 *
 * Editor: Roberto Méndez Méndez
 * Creación: 7 Abril 2026
 * Editado: 8 Jun 26
 */

import javax.swing.*;

void main() {
    JFrame frame = new ArbolDePitagorasSimetrico_v2();

    //Tamaño y título del Frame
    frame.setSize(500, 500);
    frame.setTitle("Fractal. Árbol de Pitágoras");

    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

    // Posición del Frame
    frame.setLocationRelativeTo(null);

    frame.setVisible(true);
}
