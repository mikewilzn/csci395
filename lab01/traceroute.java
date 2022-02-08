import java.io.*;
import java.lang.Integer;

public class Traceroute {
	public static void main(String[] args) {

		/* IP address must be listed before ping count */
		String address = args[0];

		runPingCommand(address);
		java.util.Date date = new java.util.Date();
		System.out.println(date);
	}

	public static void runPingCommand(String address) {
		try {
			Process p = Runtime.getRuntime().exec("traceroute " + address + " -I");
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
