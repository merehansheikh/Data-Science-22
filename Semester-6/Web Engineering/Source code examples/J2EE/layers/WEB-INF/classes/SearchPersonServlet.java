import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class SearchPersonServlet extends HttpServlet { 

public void processRequest(HttpServletRequest request,HttpServletResponse response) throws ServletException, IOException { 
	response.setContentType("text/html"); 
	PrintWriter out = response.getWriter(); 
	out.println("<html>" + "<body>" +"<h1> Address Book </h1>" +"<form action=ShowPersonServlet>" + "<br/>" 	+"<input type=text name=pName /> <br/>" +"<input type=submit value=Search Person />" +"</form>" +"</body>" +"</html>" 
	); 

	out.close(); 
	} 

// Handles the HTTP GET method.
	public void doGet(HttpServletRequest request,HttpServletResponse response)throws ServletException, IOException { 
		processRequest(request, response);} 

// Handles the HTTP POST method 
	public void doPost(HttpServletRequest request,HttpServletResponse response) throws ServletException, IOException { 
		processRequest(request, response); 
 } 

}
