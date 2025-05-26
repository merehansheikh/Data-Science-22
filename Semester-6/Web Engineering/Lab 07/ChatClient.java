import java.io.*;
import java.net.*;

public class ChatClient {
    public static void main(String[] args) {
        final String SERVER_IP = "localhost";
        final int SERVER_PORT = 1234;

        try (Socket socket = new Socket(SERVER_IP, SERVER_PORT)) {
            System.out.println("Connected to server.");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader console = new BufferedReader(new InputStreamReader(System.in));

            String message;
            while (true) {
                System.out.print("You: ");
                message = console.readLine();
                out.println(message);
                if (message.equalsIgnoreCase("exit")) {
                    break;
                }
                message = in.readLine();
                if (message.equalsIgnoreCase("exit")) {
                    System.out.println("Server has exited the chat.");
                    break;
                }
                System.out.println("Server: " + message);
            }

            socket.close();
        } catch (IOException e) {
            System.out.println("Client error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
