import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class ShowRollInfo extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String rollno = request.getParameter("rollno");

        out.println("<html><body>");
        out.println("<h2>Information for Roll Number: " + rollno + "</h2>");

        
        if(rollno.equals("101")) {
            out.println("<p>Name: Ali</p>");
            out.println("<p>Department: CS</p>");
            out.println("<p>Year: 2nd</p>");
        } else if(rollno.equals("102")) {
            out.println("<p>Name: Sara</p>");
            out.println("<p>Department: IT</p>");
            out.println("<p>Year: 1st</p>");
        } else {
            out.println("<p>No student found for this roll number.</p>");
        }

        out.println("</body></html>");
        out.close();
    }
}
