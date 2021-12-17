package uiMain;

import java.util.Hashtable;

public abstract class UI {
	public abstract Hashtable<Integer, String> getMenu();

	public abstract void ejecutarOpcion(int op);
}
