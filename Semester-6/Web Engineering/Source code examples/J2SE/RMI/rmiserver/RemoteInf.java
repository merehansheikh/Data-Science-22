import java.rmi.*;

public interface RemoteInf extends Remote{
	String show()throws RemoteException;
}
