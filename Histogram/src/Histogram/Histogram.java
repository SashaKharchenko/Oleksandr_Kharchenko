package Histogram;

import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


/**
Realization of Histogram class functions
Done by Kharchenko Oleksandr (group 2)
Date 06.12.2024
Implementation of Histogram
*/
public class Histogram {
	
	private double min_hist;
	private double max_hist;
	private int M;
	private int[] frequency;
	
	/**
	 *  Constructs an empty histogram with M bins
	 *  @param min_hist		minimum value in histogram
	 *  @param max_hist 	maximum value in histogram
	 *  @param M 	number of bins in histogram
	 */
	public Histogram(double min_hist, double max_hist, int M) {
		this.min_hist = min_hist;
		this.max_hist = max_hist;
		this.M = M;
		this.frequency =new int[M];
		Arrays.fill(frequency, 0);
	}
	
	/**
	 *  Constructs a histogram by frequency array
	 *  @param min_hist		minimum value in histogram
	 *  @param max_hist 	maximum value in histogram
	 *  @param frequency 	number of elements in each bin
	 */
	public Histogram(double min_hist, double max_hist, int[] frequency) {
		this.min_hist = min_hist;
		this.max_hist = max_hist;
		this.M = frequency.length;
		this.frequency = frequency.clone();
	}
	
	/**
	 * Getter for min_hist
	 * 
	 * @return 		min_hist - minimum value in histogram
	 */
	public double getMin_hist() {
		return min_hist;
	}
	
	/**
	 * Getter for max_hist
	 * 
	 * @return 		max_hist - maximum value in histogram
	 */
	public double getMax_hist() {
		return max_hist;
	}
	
	/**
	 * Getter for M
	 * 
	 * @return 		M - number of bins in histogram
	 */
	public int getM() {
		return M;
	}
	
	/**
	 * Getter for frequency
	 * 
	 * @return 		frequency - number of elements in each bin
	 */
	public int[] getFrequency() {
		return frequency;
	}
	
	/**
	 * Changes the max value of the histogram
	 * @param m 	new maximum
	 */
	public void setMax(double m) {
		if (max_hist < min_hist){
			return;
		}
		int[] new_frequency = new int[M];
		Arrays.fill(new_frequency, 0);
		double width = (max_hist - min_hist)/M;
		double new_width = (m - min_hist)/M;
		int cur = 0;
		int new_cur = 0;
		double prev_f = 0;
		while ((cur < M) && (new_cur < M)) {
				
			double l =Math.max(new_cur * new_width, cur * width);
			double r =Math.min((new_cur+1) * new_width, (cur+1) * width);
			double d = (r-l)/width;
			prev_f =d*frequency[cur]+prev_f;
				
			int prev = (int) Math.round(prev_f);
				
			prev_f -= prev;
			new_frequency[new_cur] += prev;
				
			if (((cur + 1) * width) <= ((new_cur+1) * new_width)) {
				cur += 1;
			}else {
				new_cur += 1;
			}
				
		}
		this.frequency = new_frequency;
		this.max_hist = m;
	}
	
	/**
	 * Changes the min value of the histogram
	 * @param m 	new minimum
	 */
	public void setMin(double m) {
		int[] new_frequency = new int[M];
		Arrays.fill(new_frequency, 0);
		double width = (max_hist - min_hist)/M;
		double new_width = (max_hist - m)/M;
		int cur = M-1;
		int new_cur = M-1;
		double prev_f = 0;
		while ((cur >= 0) && (new_cur >= 0)) {
			double r =Math.min((M-new_cur) * new_width, (M-cur) * width);
			double l =Math.max((M-new_cur-1) * new_width, (M-cur-1) * width);
			double d = (r-l)/width;
			
			prev_f =d*frequency[cur]+prev_f;
			int prev = (int) Math.round(prev_f);
				
			prev_f -= prev;
			new_frequency[new_cur] += prev;
				
			if (((M-cur) * width) <= ((M-new_cur) * new_width)) {
				cur -= 1;
			}else {
				new_cur -= 1;
			}
		}
		this.frequency = new_frequency;
		this.min_hist = m;
	}
	
	/**
	 * Changes M - the number of bins in histogram
	 * @param m 	new M
	 */
	public void setM(int m) {
		int[] new_frequency = new int[m];
		Arrays.fill(new_frequency, 0);
		double width = (max_hist - min_hist)/M;
		double new_width = (max_hist - min_hist)/m;
		int cur = 0;
		int new_cur = 0;
		double prev_f = 0;
		while ((cur < M) && (new_cur < m)) {
				
				double l =Math.max(new_cur * new_width, cur * width);
				double r =Math.min((new_cur+1) * new_width, (cur+1) * width);
				double d = (r-l)/width;
				prev_f =d*frequency[cur]+prev_f;
				
				int prev = (int) Math.round(prev_f);				
				prev_f -= prev;
				
				new_frequency[new_cur] += prev;
				if (((cur + 1) * width) <= ((new_cur+1) * new_width)) {
					cur += 1;
				}else {
					new_cur += 1;
				}
				
			}
		this.frequency = new_frequency;
		this.M = m;
	}
	
	/**
	 * Adds number to histogram
	 * 
	 * @param x 	the number that's added
	 * @param mode 	if mode == 1 numbers outside of [min_hist, max_hist] don't get added,
	 * 				if mode == 2 numbers outside of [min_hist, max_hist] get added to the ends of the histogram,
	 * 				if mode == 3 numbers outside of [min_hist, max_hist] change min_hist and max_hist
	 * @throws Exception mode == 1 and number is outside of [min_hist, max_hist]
	 */
	public void addNumber(double x, int mode)  throws Exception{
		if (mode == 1) {
			if ((x < min_hist) || (x > max_hist)) {
				
				String msg = "Number has to be between " + min_hist + " and " +
				max_hist + " to add to histogram\n";
				throw new Exception(msg);
			}else {
			double width = (max_hist - min_hist) / M;
			int bin = (int) ((x - min_hist)/width);
			if (bin == M) {
				bin = M-1;
			}
			frequency[bin] += 1;
			}
		}
		if (mode == 2) {
			double width = (max_hist - min_hist) / M;
			int bin = (int) ((x - min_hist)/width);
			if (bin < 0) {
				bin = 0;
			}
			if (bin >= M) {
				bin = M-1;
			}
			frequency[bin] += 1;
		}
		if (mode == 3) {
			if (x < min_hist) {
				this.setMin(x);
			}
			if(x > max_hist) {
				this.setMax(x);
			}
			double width = (max_hist - min_hist) / M;
			int bin = (int) ((x - min_hist)/width);
			if (bin == M) {
				bin = M-1;
			}
			frequency[bin] += 1;
		}
		
	}
	
	/**
	 * Adds number to histogram with mode = 1 by default
	 * 
	 * @param x 	the number that's added
	 * @throws Exception	 number is outside of [min_hist, max_hist]
	 */
	public void addNumber(double x) throws Exception{
		try {
			this.addNumber(x,1);
		} catch (Exception e) {
			throw e;
		}
	}
	
	/**
	 * Adds a batch of numbers to histogram
	 * 
	 * @param data	batch of numbers that's added
	 * @param dataSize 	length of data array
	 * @param mode 	if mode == 1 numbers outside of [min_hist, max_hist] don't get added,
	 * 				if mode == 2 numbers outside of [min_hist, max_hist] get added to the ends of the histogram,
	 * 				if mode == 3 numbers outside of [min_hist, max_hist] change min_hist and max_hist
	 * @throws Exception mode == 1 and number is outside of [min_hist, max_hist]
	 */
	public void addBatch(double[] data, int dataSize, int mode)  throws Exception {
		if (mode == 1) {
			for (int i = 0; i < dataSize; i++) {
				if ((data[i] < min_hist) || (data[i] > max_hist)) {
					String msg = "All numbers in batch have to be between " + min_hist + " and " +
							max_hist + " to add to histogram\n";
							throw new Exception(msg);
				}
					
			}
			double width = (max_hist - min_hist) / M;
			for (int i = 0; i < dataSize; i++) {
				int bin = (int) ((data[i] - min_hist)/width);
				if (bin == M)
					bin = M-1;
				frequency[bin] += 1;
				}
		}
		if (mode == 2) {
			for (int i = 0; i < dataSize; i++) {
				this.addNumber(data[i], 2);
			}
		}
		if (mode == 3) {
			double minNum = data[0];
			double maxNum = data[0];
			
			for (int i = 0; i < dataSize; i++) {
				if (data[i] < minNum)
					minNum = data[i];
				if (data[i] > maxNum)
					maxNum = data[i];					
			}
			
			if (minNum < min_hist) {
				this.setMin(minNum);
			}
			if (maxNum > max_hist) {
				this.setMax(maxNum);
			}
			
			double width = (max_hist - min_hist) / M;
			for (int i = 0; i < dataSize; i++) {
				int bin = (int) ((data[i] - min_hist)/width);
				if (bin == M)
					bin = M-1;
				frequency[bin] += 1;
			}
		}
	}
	
	/**
	 * Adds numbers from file to histogram
	 * 
	 * @param file	name of file 
	 * @param mode 	if mode == 1 numbers outside of [min_hist, max_hist] don't get added,
	 * 				if mode == 2 numbers outside of [min_hist, max_hist] get added to the ends of the histogram,
	 * 				if mode == 3 numbers outside of [min_hist, max_hist] change min_hist and max_hist
	 * @throws Exception mode == 1 and number is outside of [min_hist, max_hist]
	 */
	public void addFromFile(String file, int mode) throws Exception{
		Path inpPath = Path.of(file);
		try{
			List<String> list = Files.readAllLines(inpPath);
			ArrayList<Double> doubles = new ArrayList<>();
			for (int i = 0; i < list.size(); i++) {
				String[] line= list.get(i).trim().split("\\s+");
				for(int j = 0; j < line.length; j++) {
					doubles.add(Double.parseDouble(line[j]));
				}
			}
			
			double[] arr = new double[doubles.size()];
			for (int i = 0; i < arr.length; i++) {
				arr[i] = doubles.get(i);
			}
			try {
				this.addBatch(arr, arr.length, mode);
			} catch(Exception e) {
				throw e;
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
	/**
	 * Adds a batch of numbers to histogram with mode = 1 by default
	 * @param data	batch of numbers that's added
	 * @param dataSize 	length of data array
	 * @throws Exception mode == 1 and number is outside of [min_hist, max_hist]
	 */
	public void addBatch(double[] data, int dataSize) throws Exception{
		try {
			this.addBatch(data, dataSize, 1);
		} catch(Exception e) {
			throw e;
		}
	}
	
	/**
	 * Adds numbers from binary file to histogram
	 * 
	 * @param name	name of binary file 
	 * @param mode 	if mode == 1 numbers outside of [min_hist, max_hist] don't get added,
	 * 				if mode == 2 numbers outside of [min_hist, max_hist] get added to the ends of the histogram,
	 * 				if mode == 3 numbers outside of [min_hist, max_hist] change min_hist and max_hist
	 * @throws Exception mode == 1 and number is outside of [min_hist, max_hist]
	 */
	public void addFromBinaryFile(String name, int mode) throws Exception{
		double[] array = null;
		try {
			var f = new DataInputStream(
					new FileInputStream(name)
			);
			File file = new File(name);
			int size =  (int) (file.length() / Double.BYTES);
			array = new double[size];
			for (int i = 0; i < array.length; i++) {
				array[i] = f.readDouble(); 
			}
			f.close();
		}catch (IOException e) {
			e.printStackTrace();
		}
		try {
			this.addBatch(array, array.length, mode);
		} catch(Exception e) {
			throw e;
		}
	}
	
	/**
	 * Returns the number of elements in histogram
	 * 
	 * @return	 	number of elements in histogram
	 */
	public int num() {
		int s = 0;
		for (int i = 0; i < M; i++) {
			s += frequency[i];
		}
		return s;
	}
	
	/**
	 * Returns the amount of elements in i-th bin (starting from 0)
	 * @param i 	i-th  bin (starting from 0)
	 * @return		amount of elements in i-th bin
	 */
	public int numHist(int i) {
		return frequency[i];
	}
	
	/**
	 * Returns the mean of histogram
	 * 
	 * @return		mean
	 */
	public double mean() {
		double width = (max_hist - min_hist) / M;
		double m = 0;
		double cur_num = min_hist + width/2;
		for (int i = 0; i < M; i++) {
			m += cur_num * frequency[i];
			cur_num += width;
		}
		
		return m / this.num();
	}
	
	/**
	 * Returns the median of histogram
	 * 
	 * @return		median
	 */
	public double median() {
		double s = 0;
		double n = this.num();
		int i = 0;
		double width = (max_hist - min_hist) / M;
		
		for (i = 0; i < M; i++) {
			s += frequency[i];
			if (s * 2 >= n) {
				break;
			}
		}
		
		if (2 * s == n) {
			return min_hist + width *(i+ 1);
			
		}else {
			 return min_hist + width *(i+0.5 );
		}
	}
	
	/**
	 * Returns the variance of histogram
	 * 
	 * @return		variance
	 */
	public double variance() {
		double width = (max_hist - min_hist) / M;
		double cur_num = min_hist + width/2;
		double m2 = 0;
		for (int i = 0; i < M; i++) {
			m2 += cur_num * cur_num * frequency[i];
			cur_num += width;
		}
		m2 = m2 / this.num();
		double m = this.mean();
		return m2 - m * m;
	}
	
	/**
	 * Returns the standard deviation of histogram
	 * 
	 * @return		standard deviation
	 */
	public double dev() {
		return Math.sqrt(this.variance());
	}
	
	/**
	 * Returns the skewness of histogram
	 * 
	 * @return		skewness
	 */
	public double skewness() {
		double width = (max_hist - min_hist) / M;
		double cur_num = min_hist + width/2;
		double m = this.mean();
		double s = 0;
		for (int i = 0; i < M; i++) {
			s += Math.pow((cur_num - m), 3 )* frequency[i];
			cur_num += width;
		}

		return s/(this.num()*Math.pow(this.dev(), 3));
	}
	
	/**
	 * Returns the excess kurtosis of histogram
	 * 
	 * @return		excess kurtosis
	 */
	public double excess() {
		double width = (max_hist - min_hist) / M;
		double cur_num = min_hist + width/2;
		double m = this.mean();
		double s = 0;
		for (int i = 0; i < M; i++) {
			s += Math.pow((cur_num - m), 4 )* frequency[i];
			cur_num += width;
		}

		return s/(this.num()*Math.pow(this.variance(), 2)) - 3;
	}
	
	/**
	 * Returns the mode of histogram
	 * 
	 * @return		mode
	 */
	public double mode() {
		double width = (max_hist - min_hist) / M;
		int m = frequency[0];
		int index = 0;
		for (int i = 0; i < M; i++) {
			if (frequency[i] > m) {
				index = i;
				m = frequency[i];
			}
		}
		return min_hist + width * (index + 0.5);
	}
	
	/**
	 * Returns the lower quartile of histogram
	 * 
	 * @return		lower quartile
	 */
	public double lower_quartile() {
		double s = 0;
		int n = (int) (this.num()/4.0+0.5);
		int i = 0;
		double width = (max_hist - min_hist) / M;
		for (i = 0; i < M; i++) {
			s += frequency[i];
			if (s >= n) {
				break;
			}
		}
		
		return min_hist + width *(i+0.5 );
	}
	
	/**
	 * Returns the upper quartile of histogram
	 * 
	 * @return		upper quartile
	 */
	public double upper_quartile() {
		double s = 0;
		int n = (int) (3*this.num()/4.0+0.5);
		int i = 0;
		double width = (max_hist - min_hist) / M;
		for (i = 0; i < M; i++) {
			s += frequency[i];
			if (s >= n) {
				break;
			}
		}
		
		return min_hist + width *(i+0.5 );
	}
	
	/**
	 * Returns the interquartile range of histogram
	 * 
	 * @return		Interquartile range
	 */
	public double IQR() {
		return upper_quartile() - lower_quartile();
	}
	
	/**
	 * Returns the entropy of histogram
	 * 
	 * @return		Entropy
	 */
	public double entropy() {
		double e = 0;
		double n = this.num();
		for (int i = 0; i< M; i++) {
			double prob = frequency[i] / n;
			if (prob != 0)
				e -= prob * Math.log(prob) / Math.log(2);
		}
		return e;
	}
	
	/**
	 * Represents the histogram as a string
	 * 
	 * @return		String, containing all Histogram fields
	 */
	public String toString() {
		String str = "min = " + min_hist + " max = " + max_hist + " M = " +
	M + "\n" + "array = " + Arrays.toString(frequency);
		return str;
	}
}
