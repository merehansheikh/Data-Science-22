import java.io.*;
import java.net.*;

public class ChatServer {
    public static void main(String[] args) {
        final int PORT = 1234;

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server started. Waiting for client to connect...");
            
            Socket socket = serverSocket.accept();
            System.out.println("Client connected.");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader console = new BufferedReader(new InputStreamReader(System.in));

            String message;
            while (true) {
                message = in.readLine();
                if (message.equalsIgnoreCase("exit")) {
                    System.out.println("Client has exited the chat.");
                    break;
                }
                System.out.println("Client: " + message);
                System.out.print("You: ");
                message = console.readLine();
                out.println(message);
                if (message.equalsIgnoreCase("exit")) {
                    break;
                }
            }

            socket.close();
        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
