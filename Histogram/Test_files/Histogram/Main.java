package Histogram;

import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;


/**File Main.java
Realization of Histogram class functions
Done by Kharchenko Oleksandr (group 2)
Date 06.12.2024
Implementation of Histogram
*/
public class Main {

	public static void main(String[] args) {
		Histogram hist = new Histogram(0, 3, 3);
		Histogram hist2 = new Histogram(-3, 3, 12);
		Histogram hist3 = new Histogram(-3, 3, 12);
	   
		if (test1(hist) == false)
			System.out.println("test 1 passed");
		if (test2(hist) == false)
			System.out.println("test 2 passed");
		if (test3(hist2) == false)
			System.out.println("test 3 passed");
		if (test4(hist) == false)
			System.out.println("test 4 passed");
		if (test5(hist) == false)
			System.out.println("test 5 passed");
		if (test6(hist) == false)
			System.out.println("test 6 passed");
		if (test7(hist2) == false)
			System.out.println("test 7 passed");
		if (test8(hist2) == false)
			System.out.println("test 8 passed");
		if (test9(hist) == false)
			System.out.println("test 9 passed");
		if (test10(hist, hist2) == false)
			System.out.println("test 10 passed");
		if (test11(hist, hist2) == false)
			System.out.println("test 11 passed");
		if (test12(hist, hist2) == false)
			System.out.println("test 12 passed");
		if (test13(hist, hist2) == false)
			System.out.println("test 13 passed");
		if (test14(hist3, hist2) == false)
			System.out.println("test 14 passed");
		if (test15(hist3, hist2) == false)
			System.out.println("test 15 passed");
		if (test16(hist2) == false)
			System.out.println("test 16 passed");
		if (test17(hist2) == false)
			System.out.println("test 17 passed");
		if (test18(hist2, hist3) == false)
			System.out.println("test 18 passed");
		if (test19(hist) == false)
			System.out.println("test 19 passed");
		if (test20(hist, hist2) == false)
			System.out.println("test 20 passed");
		if (test21(hist, hist2) == false)
			System.out.println("test 21 passed");
		if (test22(hist, hist2) == false)
			System.out.println("test 22 passed");
		if (test23(hist, hist2) == false)
			System.out.println("test 23 passed");
		
		
		
		//hist.addFromFile( "resources\\Histogram_test.txt", 1);
		//writeToBinaryFile("resources\\Histogram_test.dat", data);
		//hist.addFromBinaryFile("resources\\Histogram_test.dat", 1);
		
	}
	
	public static void writeToBinaryFile(String name, double[] array) {
		try {
			var f = new DataOutputStream(
					new FileOutputStream(name)
			);
			for (int i = 0; i < array.length; i++) {
				f.writeDouble(array[i]);
			}
			f.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static boolean test1(Histogram hist) {
		try {
			hist.addFromFile("resources\\Histogram_test.txt", 3);
		} catch (Exception e) {
			e.printStackTrace();
		}
		int[] res = {2, 2, 2};
		if (Arrays.equals(hist.getFrequency(), res) && hist.getMax_hist() == 6)
			return false;
		return true;
	}
	
	public static boolean test2(Histogram hist) {
		int[] res = {2, 2, 2};
		try {
			hist.addNumber(70, 1);
		} catch (Exception e) {
			if (Arrays.equals(hist.getFrequency(), res))
				return false;
			return true;
		}

		return true;
	}
	
	public static boolean test3(Histogram hist2) {
		double [] data = {-30000, -2, -1, 0, 1, 20000};
		writeToBinaryFile("resources\\Histogram_test.dat", data);
		try {
			hist2.addFromBinaryFile("resources\\Histogram_test.dat", 2);
		} catch (Exception e) {
			e.printStackTrace();
		}
		int[] res = {1,0,1,0,1,0,1,0,1,0,0,1};
		if (Arrays.equals(hist2.getFrequency(), res))
			return false;
		return true;
	}
	
	public static boolean test4(Histogram hist) {
		double [] data = {0, 2.5, 3, 3.5};
		try {
			hist.addBatch(data, 4, 1);
		}catch(Exception e) {
			e.printStackTrace();
		}
		int[] res = {3, 5, 2};
		if (Arrays.equals(hist.getFrequency(), res))
			return false;
		return true;
	}
	public static boolean test5(Histogram hist) {
		hist.setMax(12);
		int[] res = {8, 2, 0};
		if (Arrays.equals(hist.getFrequency(), res) && hist.getMax_hist()  == 12)
			return false;
		return true;
	}
	public static boolean test6(Histogram hist) {
		hist.setMin(3);
		int[] res = {3, 1, 0};
		if (Arrays.equals(hist.getFrequency(), res) && hist.getMin_hist() == 3)
			return false;
		return true;
	}
	public static boolean test7(Histogram hist2) {
		hist2.setM(6);
		int[] res = {1,1,1,1,1,1};
		if (Arrays.equals(hist2.getFrequency(), res) && hist2.getM() == 6)
			return false;
		return true;
	}
	public static boolean test8(Histogram hist2) {
		hist2.setM(3);
		int[] res = {2,2,2};
		if (Arrays.equals(hist2.getFrequency(), res) && hist2.getM() == 3)
			return false;
		return true;
	}
	public static boolean test9(Histogram hist) {
		hist.setM(12);
		int[] res = {1,1,0,1,0,1,0,0,0,0,0,0};
		if (Arrays.equals(hist.getFrequency(), res) && hist.getM() == 12)
			return false;
		return true;
	}
	public static boolean test10(Histogram hist, Histogram hist2) {
		if (hist.num() == 4 && hist2.num() == 6)
			return false;
		return true;
	}
	
	public static boolean test11(Histogram hist, Histogram hist2) {
		if ((hist.numHist(10) == 0) && (hist2.numHist(1) == 2))
			return false;
		return true;
	}
	public static boolean test12(Histogram hist, Histogram hist2) {
		if ((hist.mean() == 5.0625) && (hist2.mean() == 0.0))
			return false;
		return true;
	}
	
	public static boolean test13(Histogram hist, Histogram hist2) {
		if ((hist.median() == 4.5) && (hist2.median() == 0.0))
			return false;
		return true;
	}
	public static boolean test14(Histogram hist3, Histogram hist2) {
		try {
			hist3.addFromFile( "resources\\Histogram_test2.txt", 2);
		} catch (Exception e) {
			e.printStackTrace();
		}
		if (Math.abs(hist3.variance() - 0.8)<0.01 && Math.abs(hist2.variance() - 16.0/6)<0.01)
			return false;
		return true;
	}
	public static boolean test15(Histogram hist3, Histogram hist2) {
		if (Math.abs(hist3.dev() - Math.sqrt(0.8))<0.01 && Math.abs(hist2.dev() - Math.sqrt(16.0/6))<0.01)
			return false;
		return true;
	}
	public static boolean test16(Histogram hist2) {
		if (hist2.skewness() == 0.0)
			return false;
		return true;
	}
	public static boolean test17(Histogram hist2) {
		if (hist2.excess() == -6.0*10/(5 * 8))
			return false;
		return true;
	}
	public static boolean test18(Histogram hist2, Histogram hist3) {
		if ((hist2.mode() == -2 ) && (Math.abs(hist3.mode() - 0) <= 
				(hist3.getMax_hist() - hist3.getMin_hist())/hist3.getM()))
			return false;
		return true;
	}
	public static boolean test19(Histogram hist) {
		hist.setM(3);
		int[] res = {3, 1, 0};
		if ((hist.mode() == 4.5) &&Arrays.equals(hist.getFrequency(), res))
			return false;
		return true;
	}
	public static boolean test20(Histogram hist, Histogram hist2) {
		if ((hist.lower_quartile() == 4.5) && (hist2.lower_quartile() == -2))
			return false;
		return true;
	}
	public static boolean test21(Histogram hist, Histogram hist2) {
		if ((hist.upper_quartile() == 4.5) && (hist2.upper_quartile() == 2))
			return false;
		return true;
	}
	public static boolean test22(Histogram hist, Histogram hist2) {
		if ((hist.IQR() == 0) && (hist2.IQR() == 4))
			return false;
		return true;
	}
	public static boolean test23(Histogram hist, Histogram hist2) {
		if (((hist.entropy() + 0.75*Math.log(0.75)/ Math.log(2) + 0.25*Math.log(0.25)/ Math.log(2))<0.001) &&
				(hist2.entropy() - Math.log(3)/Math.log(2) < 0.001))
			return false;
		return true;
	}
}



