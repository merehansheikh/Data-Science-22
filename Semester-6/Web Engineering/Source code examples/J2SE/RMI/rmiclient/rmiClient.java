import java.rmi.*;
import java.rmi.registry.*;

public class rmiClient{
  public static void main(String arg[])throws Exception
  {
     Registry registry = LocateRegistry.getRegistry("localhost");
     RemoteInf o=(RemoteInf) registry.lookup("ob");

     System.out.println(o.show());
  }
}