import java.sql.*; 
public class PersonDAO { 
// method searchPerson 
  public PersonInfo searchPerson(String sName){ 
   PersonInfo person = null; 
   try { 

	System.out.println(sName);
	Class.forName("com.mysql.jdbc.Driver"); 
	String url = "jdbc:mysql://127.0.0.1/class_test"; 
	Connection con = DriverManager.getConnection(url, "root", "root"); 
	String sql = "SELECT * FROM info WHERE username = ?"; 
	PreparedStatement pStmt = con.prepareStatement(sql); 
	pStmt.setString(1, sName); 
	ResultSet rs = pStmt.executeQuery(); 
	if (rs.next( ) ) { 
		String name = rs.getString("username"); 
		String add = rs.getString("address"); 
		String pNum = rs.getString("phone"); 
		person = new PersonInfo(name, add, pNum); 
	} 
	con.close(); 
	}
    catch(Exception ex){ 
		System.out.println(ex); 
	} 

  return person; 
 }// end method 
}