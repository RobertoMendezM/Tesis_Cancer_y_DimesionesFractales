/**
 * Dibuja el fractal "Árbol de Pitágoras" simétrico, es decir con
 *   triángulo rectángulo a 45 grados.

 * Referencia:
 *   - Gunter Saake Kai-Uwe Sattler (2021).
 *     Algorithmen and Datenstrukturen Eine Einführung mit Java
 *     Programm 3.3 Programm zum Darstellen des Pythagoras-Baumes
 *     Buchseite: 177 (lector)
 *   - NOTAS PROGRAMACIÓN: 20 y 23 de abril 2026

 * Software:
 *        IDE IntelliJ IDEA 26.1.2
 *        Java 25

 * Editor: Roberto Méndez Méndez
 * Creación: 24/ May / 22
 * Editado:  2 julio 2026
 */
package fractalarbolpitagoras;

import javax.swing.*;
import java.awt.*;
import java.util.concurrent.TimeUnit;

public class ArbolDePitagorasSimetrico_v2 extends JFrame {

    double dx, dy;
    double x3, y3;

    public void paint(Graphics g) {
        //super.paint(g);
        g.clearRect(10, 10, 490, 490);
        paintTree(g, 210, 400, 290, 400);
    }

    /**
        Método que grafica el Fractal
     */
    void paintTree(Graphics g, double x1, double y1,
                   double x2, double y2) {

        // Se calculan la "distancia" entre los puntos P1 y P2
        // del cuadrado
        dx = x1 - x2;
        dy = y1 - y2;

        /*
          Se establece una condición de paro, que geométricamente
          equivale a que el lado del cuadrado que se va a graficar
          sea mayor a raíz de 2 (si es menor termina el programa).
         */
        if (dx * dx + dy * dy > 10) {

            // Se calculan los puntos P3 y P4 del cuadrado
            x3 = x1 - dy;
            y3 = y1 + dx;
            double x4 = x2 - dy;
            double y4 = y2 + dx;

            /*
             * Se calcula el vertice del triángulo rectángulo
             * Nota: Primero encuentra las coordenadas del punto medio
             * y después los desplazamientos
             */
            double x5 = (x3 + x4) / 2 - dy / 2;
            double y5 = (y3 + y4) / 2 + dx / 2;

            // Se grafica el cuadrado
            g.drawLine((int) x1, (int) y1, (int) x2, (int) y2);
            g.drawLine((int) x2, (int) y2, (int) x4, (int) y4);
            g.drawLine((int) x4, (int) y4, (int) x3, (int) y3);
            g.drawLine((int) x3, (int) y3, (int) x1, (int) y1);

            // Solo para ralentizar y que se vea el proceso de
            // construcción del fractal
            try {
               TimeUnit.MICROSECONDS.sleep(1000);
            } catch (InterruptedException e) {
               throw new RuntimeException(e);
            }

            /*
             * Llamada recursiva a la función paintTree,
             * con la gráfica g y los nuevos puntos base de los cuadrados
             */
            paintTree(g, x3, y3, x5, y5);
            paintTree(g, x5, y5, x4, y4);
        }
    }
}

