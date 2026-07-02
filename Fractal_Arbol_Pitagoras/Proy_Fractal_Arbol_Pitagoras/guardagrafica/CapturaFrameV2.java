/**
 * Toma captura de pantalla de un frame

 * Software:
 *        IDE IntelliJ IDEA 26.1.2
 *        Java 25

 * autor: Gemini
 * Editor: Roberto Méndez Méndez
 * Creación: 7 Abril 2026
 */

package guardagrafica;

import java.awt.AWTException;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.Timer;

public class CapturaFrameV2 extends JFrame {

    public static void guardaImagen(JFrame frame,  String titulo,
                                    int milisegundos) {

        Timer timer = new Timer(milisegundos, e -> {
        // Asegura que el frame sea visible y esté al frente para evitar capturar otra ventana
        if (!frame.isShowing()) {
            System.out.println("El frame debe estar visible en pantalla.");
            return;
        }

        try {
            // Coordenadas en pantalla (incluye los bordes de la ventana)
            Rectangle areaCaptura = frame.getBounds();

            // Toma una foto real de esa zona de la pantalla
            Robot robot = new Robot();
            BufferedImage imagen = robot.createScreenCapture(areaCaptura);

            // Guardar el archivo
            File archivo = new File(titulo+".jpg");
            ImageIO.write(imagen, "jpg", archivo);

            System.out.println("Imagen guardada con éxito en: " +
                                            archivo.getAbsolutePath());

        } catch (AWTException | IOException ex) {
            System.err.println("Error al capturar la ventana: " +
                                                        ex.getMessage());
        }
        });

        // Para que el timer se ejecute solo una vez
        timer.setRepeats(false);
        timer.start();
    }
}
