import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class secondInclude extends HttpServlet{
 public void doGet(HttpServletRequest req,HttpServletResponse res)
            throws ServletException,IOException
 {

	    PrintWriter out = res.getWriter();
	   
	   String source = (String)req.getAttribute("source");
	   
	   out.println("<h1>Source from where request came <u>"+source+"</u> </h1>");
	   out.println("<h1>This line is generated by Second Include page.</h1>");


 }
}
