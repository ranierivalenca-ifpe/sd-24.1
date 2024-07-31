// a simple echo TCP server

import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(8080);
            System.out.println("Server started at port 8080");
            Socket client = server.accept();
            System.out.println("Client connected");
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            PrintWriter out = new PrintWriter(client.getOutputStream(), true);
            String line;
            while ((line = in.readLine()) != null) {
                if (line.isEmpty()) {
                    break;
                }
                System.out.println("Received: " + line);
                out.println(line);
            }
            in.close();
            out.close();
            client.close();
            server.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}


// // create a simple http server using socket interface

// import java.io.*;
// import java.net.*;

// public class server {
//     public static void main(String[] args) {
//         try {
//             ServerSocket server = new ServerSocket(8080);
//             System.out.println("Server started at port 8080");
//             Socket client = server.accept();
//             System.out.println("Client connected");
//             BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
//             PrintWriter out = new PrintWriter(client.getOutputStream(), true);
//             String line;
//             while ((line = in.readLine()) != null) {
//                 if (line.isEmpty()) {
//                     break;
//                 }
//                 System.out.println(line);
//                 out.println(line);
//             }
//             in.close();
//             out.close();
//             // out.println("HTTP/1.1 200 OK");
//             // out.println("Content-Type: text/html");
//             // out.println();
//             // out.println("<h1>Hello World</h1>");
//             // out.close();
//             // in.close();
//             client.close();
//             server.close();
//         } catch (IOException e) {
//             e.printStackTrace();
//         }
//     }
// }