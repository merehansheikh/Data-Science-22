import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;

public class rmiServer extends UnicastRemoteObject implements RemoteInf{

	public rmiServer()throws RemoteException{}

	public String show()throws RemoteException{
 		return "i am from remote server program";
	}

public static void main(String p[])throws Exception{
		rmiServer obj=new rmiServer();
		Registry registry = LocateRegistry.getRegistry();
		registry.bind("ob",obj);
		System.out.println("server is running");
  }
}

