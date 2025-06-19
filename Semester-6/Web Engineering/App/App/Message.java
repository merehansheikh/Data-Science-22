import java.io.*;
import javax.servlet.http.*;
import javax.servlet.*;

public class Message extends HttpServlet {

   public void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
        PrintWriter out = res.getWriter();
        out.println("<html><body><h1>Welcome to the Student Directory Info Page</h1></body></html>");
        out.close();
    }


}