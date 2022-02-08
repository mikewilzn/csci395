import java.io.*;
import java.lang.Integer;

public class Pingip {
	public static void main(String[] args) {

		/* IP address must be listed before ping count */
		String address = args[0];
		String pingCount = args[1];

		runPingCommand(address, pingCount);
		java.util.Date date = new java.util.Date();
		System.out.println(date);
	}

	public static void runPingCommand(String address, String pingCount) {
		try {
			Process p = Runtime.getRuntime().exec("ping " + address + " -c " + pingCount);
			BufferedReader InputStream = new BufferedReader(new InputStreamReader(p.getInputStream()));

			String s = "";

			while ((s = InputStream.readLine()) != null) {
				System.out.println(s);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
