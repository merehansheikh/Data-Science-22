import java.io.*;
import java.util.*;
import javax.servlet.http.*;
import javax.servlet.*;

public class Greeting extends HttpServlet {

ArrayList<Book> AL;

public void init(ServletConfig scfg)
{
 AL = new ArrayList<Book>();
 AL.add(new Book("a","a","a"));
 AL.add(new Book("b","b","b"));
 AL.add(new Book("c","c","c"));
}

public void doGet(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
	{        
	
	
	response.setContentType("text/html");
    	PrintWriter out = response.getWriter();

    out.println("<html>");
    out.println("<head>");
    out.println("<title>Servlet GreetingServlet</title>");
    out.println("</head>");
    out.println("<body><table>");
	for(int i=0; i<AL.size(); i++)
	{
	out.println("<tr> <td>" + AL.get(i).author + AL.get(i).title + AL.get(i).ISBN +"<\td><\tr>");
	}
    out.println("</table></body>");
    out.println("</html>");
    out.close(); 

	
	}

public void doPost(HttpServletRequest request, HttpServletResponse response)throws ServletException, IOException 
	{        
	
	
	response.setContentType("text/html");
    	PrintWriter out = response.getWriter();

    String firstName = request.getParameter("firstName");
    String surname = request.getParameter("surname");

    out.println("<html>");
    out.println("<head>");
    out.println("<title>Servlet GreetingServlet</title>");
    out.println("</head>");
    out.println("<body><table>");
	for(int i=0; i<AL.size(); i++)
	{
		if(AL.get(i).author.equals(firstName ))
			out.println("<tr> <td>" + AL.get(i).author + AL.get(i).title + AL.get(i).ISBN +"<\td><\tr>");
	}
    out.println("</table></body>");
    out.println("</html>");
    out.close(); 

	
	}





}