import numpy as np
from sklearn.datasets import load_diabetes

#Computes covariance matrix of non-target attributes
def q1a(d):
	return np.cov(d.data, rowvar=False)

#Uses matrix to extract correlation between bmi (col 2) and hdl (col 6) attributes
def q1b(d):
	cov_matrix = q1a(d)
	bmi_hdl_corr = cov_matrix[2, 6]
	return bmi_hdl_corr

#Verifying correlation from part b
def q1c(d):
	bmi_above_mean = d.data[d.data[:,2] > np.mean(d.data[:,2])] #All rows with bmi above mean
	bmi_below_mean = d.data[d.data[:,2] < np.mean(d.data[:,2])] #All rows with bmi below mean
	
	med_hdl_above = np.median(bmi_above_mean[:,6])
	med_hdl_below = np.median(bmi_below_mean[:,6])

	return [med_hdl_above, med_hdl_below]

#Compute effect size, as measured by Cohen's d
def q1d(d):
	a = d.data[d.data[:,2] > np.mean(d.data[:,2])] #All rows with bmi above mean
	b = d.data[d.data[:,2] < np.mean(d.data[:,2])] #All rows with bmi below mean
	a_size = a[:,6].size
	b_size = b[:,6].size
	a_var = np.var(a[:,6], ddof=1)
	b_var = np.var(b[:,6], ddof=1)

	#Uses above values to calculate pooled standard deviation
	pooled_sd = ((a_var * (a_size - 1) + b_var * (b_size - 1)) / (a_size + b_size - 2)) ** (1/2)
	#Final value for Cohen's d (magnitude)
	return abs(((np.mean(a[:,6]) - np.mean(b[:,6])) / pooled_sd))

def main(): 
		d = load_diabetes() #Store diabetes dataset (contains target and non-target matrices)
		print("Shape of covariance matrix (for non-target attributes): " + str(q1a(d).shape))
		print("Correlation between bmi and hdl attributes: " + str(q1b(d)))
		test_medians = q1c(d)
		print("Median hdl among patients with bmi greater than the mean: " + str(test_medians[0]))
		print("Median hdl among patients with bmi less than the mean: " + str(test_medians[1]))
		print("Cohen's d (Effect size): " + str(round(q1d(d), 4)))

if __name__ == "__main__":
	main()