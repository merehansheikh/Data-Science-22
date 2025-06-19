import java.io.*;
import java.util.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class StudentInfo extends HttpServlet {
    ArrayList<Student> studentList;

    public void init(ServletConfig scfg) {
        studentList = new ArrayList<Student>();
        studentList.add(new Student("Ali", "Khan", "502"));
        studentList.add(new Student("Sara", "Ahmed", "503"));
        studentList.add(new Student("Zain", "Qureshi", "504"));
    }

    public void doGet(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();

        out.println("<html><body><table border='1'>");
        out.println("<tr><th>First Name</th><th>Last Name</th><th>Roll No</th></tr>");
        for (Student s : studentList) {
            out.println("<tr><td>" + s.firstName + "</td><td>" + s.lastName + "</td><td>" + s.rollNo + "</td></tr>");
        }
        out.println("</table></body></html>");
        out.close();
    }

    public void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
        res.setContentType("text/html");
        PrintWriter out = res.getWriter();

        String inputName = req.getParameter("firstName");

        out.println("<html><body><table border='1'>");
        out.println("<tr><th>First Name</th><th>Last Name</th><th>Roll No</th></tr>");
        for (Student s : studentList) {
            if (s.firstName.equalsIgnoreCase(inputName)) {
                out.println("<tr><td>" + s.firstName + "</td><td>" + s.lastName + "</td><td>" + s.rollNo + "</td></tr>");
            }
        }
        out.println("</table></body></html>");
        out.close();
    }
}
