
Wed, Aug 26 at 11:40 AM
i m doing like this how do i seperate 

Today 10:31 PM
494100d9-643c-4fc1-9609-6f0e29779a47.png
43d85ff4-ebc8-4712-835f-af492cb4bc4a.png
5b46a1f5-3255-4f15-b98a-2ea72c06aa9e.png
152fe0a1-88f6-45d2-98bf-390772936d69.png
its for descriptive statistics There are three most common measures of central tendency: mean, median, and mode. In what follows, carefully note that there may be slight differences in terms of how these measures are computed for a population versus for a sample. The symbols used might also vary.

The Mean
The arithmetic mean, or simply the mean, is the sum of all values in a series divided by the total number of values in that series:

﻿top enclose X equals 1 over n stack sum with i equals 1 below and n on top x subscript i﻿

Explanations:

﻿top enclose X﻿ (read "x-bar") symbolises the mean of the sample

﻿n﻿ is the total number of values in the series

﻿x subscript i﻿ is each value in the series

The sigma symbol﻿sum from blank to blank of﻿ indicates the summation operation performed on ﻿x subscript i﻿

Example
The mean of a series of values 100, 115, 93, 102, and 297 is calculated as:

﻿top enclose X equals left parenthesis 100 plus 115 plus 93 plus 102 plus 297 right parenthesis divided by 5 equals 707 divided by 5 equals bold 141 bold. bold 4﻿

The mean of a population is calculated quite similarly, only with a slightly different symbol:

﻿mu equals 1 over N sum from i equals 1 to n of x subscript i﻿

Explanations:

﻿mu﻿ (read "mu") symbolises the mean of the population

The Median
The median is the middle value in a series of ranked values (in ascending or descending order).

If there are n values, the median is formally defined as the (n+1)/2-th value.

If n is an even number, the median is the average of the (n/2)-th and ((n/2)+1)-th values.

Examples
The median of values 1, 4, 6, 6, 10 (ranked in ascending order) is 6.
The median of values 15, 10, 6, 5, 3, 1 (ranked in an ascending order) is (6+5)/2 = 5.5
By virtue of its definition, half of the data in a series lie below the median and half above the median. This provides us with some sense of how the values are distributed. In addition, the median is a better measure of central tendency than the mean for data that is asymmetrical or that contains outliers.

The Mode
The mode refers to the most frequently occurring value. It is normally used for describing nominal or ordinal data.

Example
The mode of values 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3 is 3 (occuring 7 times in the series).

Measures of Dispersion
Dispersion tells us about how variable or spread out our data is. Knowing the dispersion is as useful as knowing the central tendency. Together, they form the foundations for descriptive statistics and other more advanced statistical analyses. There are different ways of measuring dispersion, explained below.

The Range
This range is the difference between the minimum (smallest) and the maximum (largest) values in a series. It is the simplest measure of dispersion.

Example
The range of values 100, 115, 93, 102, 297 = 297 - 93 = 204

The Interquartile Range (IQR)
The interquartile range (IQR) is a little more sophisticated than the range. It is the difference between the 25th and the 75th percentile values.

Assuming a sorted set of values, the percentile is the value below which a percentage of the values fall. A value representing the 25th percentile is the value below which 25% of all values in a series fall. By the same definition, 75% of all values in a series fall below the 75th percentile value, and the median is equivalent to the 50th percentile. The image below further illustrates the idea of percentile. Visit this webpage for the percentile formulas.

percentile.png

Source: mathisfun.com

Example
For values 1, 2, 3, 5, 7, 8, 11, 12, 15, 15, 18, 18, 20, its IQR is calculated as follows:

25th percentile = 5
75th percentile = 15
IQR = 15 - 5 = 10
A useful application of the IQR is to detect outliers in data. An outlier is usually a value that is rare or rather unexpected. It may point to an error in data collection, an unusual phenomenon, or other kinds of unexpected observation. Using IQR, we can determine that any value that is *lower *than 1.5 x IQR below the 25th percentile or *higher *than 1.5 x IQR above the 75th percentile is an outlier. Visit this webpage for an illustrated example.

The Variance
The variance refers to how much, on average, all values in a series vary around the mean. It is calculated slightly differently, depending on whether the data represent a population or a sample.

Given n number of values in the data, if the data is a sample, then the variance is:

﻿s squared equals fraction numerator 1 over denominator n minus 1 end fraction sum from i equals 1 to n of left parenthesis x subscript i minus top enclose x right parenthesis squared﻿

If the data represents a population, then the variance:

﻿sigma squared equals 1 over n sum from i equals 1 to n of left parenthesis x subscript i minus mu right parenthesis squared﻿

The Standard Deviation
Deriving the standard deviation is easy if we know the variance. It is merely the square root of variance:

﻿s equals square root of s squared end root﻿ for the standard deviation of a sample, and ﻿sigma equals square root of sigma squared end root﻿ for a population's standard deviation.

Example
For a series of values 1, 2, 3, 4, and 5, find the sample variance and standard deviation. Likewise, if the series represents a population, calculate its variance and standard deviation. Solutions:

Sample variance:

var-sample.PNG

Sample standard deviation:

stdev-sample.PNG

Population variance:

var-pop.PNG

Population standard deviation:

stdev-pop.PNG

Source: Boslaugh (2012) Chapter 4 p. 94

To conclude this section, please watch this short but excellent video. It further illustrates variance and standard deviation using examples. It also introduces one additional measure of spread that is useful when dealing with data that employ different units of measurement: the Coefficient of Variation (CV).Distributions of Data

Essentially, the various measures of central tendency and dispersion help us better understand how values are distributed in a sample or population. Knowing these distributions, in turn, allows us to make informed guesses (inferences) about the properties and behaviours of a population being described by the sample data.

To start, let us learn about the histogram.

Histogram
The histogram is a popular data visualisation choice for displaying the distribution of continuous data. In a histogram, such as the one shown below, the x-axis (horizontal axis) represents a sorted scale of continuous values, whereas the y-axis (vertical axis) denotes the frequencies (count or number of occurrences) for each interval defined along the x-axis scale. The height of a bar or bin signifies the exact frequency of the corresponding interval scale.

Carefully examine the anatomy of the following example of the histogram (ignore the Cp, Cpk, CpU, ... scores on the right side of the histogram; they are not inherently part of a histogram).Normal distribution
Arguably, this is the most commonly used distribution in statistics and data science. One reason for this is that the normal distribution reasonably describes how continuous variables are distributed in reality (i.e. most real-world events can be described by normal distributions).

normal-dist-boslaugh.PNG

Source: Boslaugh (2012) Chapter 4 p. 89

All data that have normal distributions share certain characteristics:

Symmetry (not skewed)
Unimodality (there is only a single most common value)
A common value for the median, median, and mode
It is common to refer to normal distributions as the Gaussian distributions.

Skewed distributions
If values in data are neither distributed uniformly nor normally, then they may follow a skewed distribution. A skewed distribution follows a non-symmetrical shape, where the majority of different values are concentrated below or above the median. Consequently, the three measures of central tendency (mean, median, mode) for a skewed distribution are not identical.

There are two kinds of skewed distributions, as illustrated below. Observe the relative positions of the mean, median, and mode in each distribution.

mean median mode

Source: codeburst.io

Before moving on, watch this 5-minute video to check your understanding of continuous data distributions.

Binomial distribution
The previous distributions describe the distributions of continuous data. In contrast, for describing the distribution of nominal or categorical data where values can only assume a limited set of categories (e.g. the outcome of flipping a coin, rolling of a die, yes or no, male or female, colours, etc.), the binomial distribution is often used.

The binomial distribution is used when there are exactly two mutually exclusive outcomes of a trial. These outcomes are appropriately labelled "success" and "failure". For example, to obtain the binomial distribution of data obtained from flipping a coin 100 times, we could label "head" as "success" and "tail" as "failure", or vice versa. The binomial distribution then describes the distribution of the probability of obtaining the head outcome over 100 trials. It answers such questions as "what is the probability of obtaining 50 heads from flipping a coin 100 times?"

Carefully observe four examples of the binomial distribution below. Let us assume that they describe the probability of obtaining the "success" outcome from tossing a coin 100 times (100 trials). Notice that the x-axis represents all possible numbers of times (frequencies) that the "success" outcome can be obtained (given a certain probability) and the y-axis represents their corresponding probabilities. In this way, the binomial distribution histogram differs slightly from other general histograms. Finally note that the shapes of the binomial distributions resemble normal distributions, especially when the data is considered 'large enough'.

binomial.PNG

Source: nist.gov

In a fair coin toss, if the probability of obtaining a head in a single toss is 0.5 (or 50%), then the probability of "success" is defined as 0.5 (P=0.50). The binomial distribution for such data, described by the lower left histogram in the above example, suggests that obtaining 50 heads in 100 trials has the highest probability (0.08).

On the contrary, if we believe that the coin is not a fair one and assume that the chance of obtaining a head is merely 0.1, then the upper left histogram is a more appropriate description of how the data is actually distributed. In this case, it is highly unlikely that we will obtain more than 20 heads out of 100 trials.

Further Readings

b0716060-0fe4-4c87-a307-670bd698b6c5.png
that's for analytical task mark other are for presentation and documentation 

95180427-74a8-4510-91fe-7ec3a76c7aa9.png
i think need to import yeah 

a81c6c10-8370-4ba8-a7dc-f29c12ebd396.png
81cba35e-7192-42b5-a628-87477c2526da.png
is it correct or not 


Pasted markdown(20260908-131858).md
File

6276e381-13f9-477e-93c3-fe4fb7c73f85.png
one thing i m confused here on y -axis why only till 17.5 sth 


Pasted markdown(20260908-132711).md
File
Inferential statistics (Confidence interval): Use the sample statistics to obtain the confidence interval estimation for the player population. now this one lecturrer gave 2 code CI mean is import scipy.stats as st
import math

Method 1: Step-by-step calculation
sample mean, standard deviation, and sample size
x_bar = 175
s = 20
n = 40
print("Mean: %.2f. Standard deviation: %.2f. Size: %d." % (x_bar, s, n))

z-score (assuming 95% Confidence Level)
z_score = st.norm.ppf(q = 0.975)
print("Z-statistic: %.2f" % z_score)

compute standard error
std_err = s / math.sqrt(n)
print("Standard error: %.2f" % std_err)

compute the margin of error
mrg_err = z_score * std_err
print("Margin of error: %.2f" % mrg_err)

get the lower and upper bound of confidence interval
ci_low = x_bar - mrg_err
ci_upp = x_bar + mrg_err

print("Confidence Interval of the mean: %.2f to %.2f" % (ci_low, ci_upp))

Method 2: Use the statsmodels package
import statsmodels.stats.weightstats as stm

ci_low_stm, ci_upp_stm = stm._zconfint_generic(x_bar,std_err,alpha=0.05, alternative="two-sided")
print("Confidence Interval of the mean: %.2f to %.2f" % (ci_low_stm, ci_upp_stm))
CI prop is import statsmodels.stats.proportion as stm

the number of objects of interest in a sample
prop = 52

sample size
total = 100

confidence level
conf_lvl = 0.95

significance level (alpha)
sig_lvl = 1 - conf_lvl

compute confidence interval for proportion (confidence level=95%)
ci_low, ci_upp = stm.proportion_confint(prop, total, alpha=sig_lvl, method="normal")
print("C.I. of proportion at %d%% confidence level is %.3f (%.1f%%) and %.3f (%.1f%%)." %
(conf_lvl100, ci_low, ci_low100, ci_upp, ci_upp*100))


5f546f9d-7186-496a-968e-5edaac5088a9.png
here lecturere got in positive u got negavtive is my correct PS C:\CDU S2 2026\Final FDS> & C:\Users\indra\AppData\Local\Programs\Python\Python313\python.exe "c:/CDU S2 2026/Final FDS/two-sample_t_test.py"

 Computing t* ...
         t-statistic (t*): -2.45

 Computing p-value ...
         p-value: 0.0151

 Conclusion:
         We reject the null hypothesis.
PS C:\CDU S2 2026\Final FDS> 

d5c8d2f9-7c8e-427e-988d-fb2225acc91e.png
here what is random state 42

5e544cf0-6e5b-4742-b741-65ed6e789c13.png
thats all yeah 

efa971f7-f05a-417f-bca5-07c9b577d862.png
now describe this one in short Distributions of Data

Essentially, the various measures of central tendency and dispersion help us better understand how values are distributed in a sample or population. Knowing these distributions, in turn, allows us to make informed guesses (inferences) about the properties and behaviours of a population being described by the sample data.

To start, let us learn about the histogram.

Histogram
The histogram is a popular data visualisation choice for displaying the distribution of continuous data. In a histogram, such as the one shown below, the x-axis (horizontal axis) represents a sorted scale of continuous values, whereas the y-axis (vertical axis) denotes the frequencies (count or number of occurrences) for each interval defined along the x-axis scale. The height of a bar or bin signifies the exact frequency of the corresponding interval scale.

Carefully examine the anatomy of the following example of the histogram (ignore the Cp, Cpk, CpU, ... scores on the right side of the histogram; they are not inherently part of a histogram).

anatomy-of-a-histogram.png

Source: qimacros.com

Common types of continuous data distributions
There are different ways by which continuous data can be distributed. The histograms below illustrate various shapes of distributions for continuous data.

histogram-example-2.png

Source: chartio.com

In what follows, we cover some of the most basic and common ones: uniform, normal, skewed, and binomial.

Uniform distribution
If all possible values in a given data have *approximately *the same frequencies or *approximately *the same probability of occurring, then the data has a uniform distribution. Below is a histogram that shows a uniform distribution of a set of continuous value ranges, spread between 0.00 and 100.00 along the x-axis. The y-axis represents the count or frequency of each value range.

uniform-dist-boslaugh.PNG

Source: Boslaugh (2012) Chapter 3 p. 60

The uniform distribution defines an equal probability over a given range for a continuous distribution. It is also often depicted using a standard straight line that signifies that all values along the x-axis have the same probability of occurring in the data:

uniform-dist.PNG

Source: nist.gov

One of the most important applications of uniform distribution is in the generation of random numbers, which is a common element in many data science methods and other statistical techniques. For this reason, it is serves as an important reference distribution.

Normal distribution
Arguably, this is the most commonly used distribution in statistics and data science. One reason for this is that the normal distribution reasonably describes how continuous variables are distributed in reality (i.e. most real-world events can be described by normal distributions).

normal-dist-boslaugh.PNG

Source: Boslaugh (2012) Chapter 4 p. 89

All data that have normal distributions share certain characteristics:

Symmetry (not skewed)
Unimodality (there is only a single most common value)
A common value for the median, median, and mode
It is common to refer to normal distributions as the Gaussian distributions.

Skewed distributions
If values in data are neither distributed uniformly nor normally, then they may follow a skewed distribution. A skewed distribution follows a non-symmetrical shape, where the majority of different values are concentrated below or above the median. Consequently, the three measures of central tendency (mean, median, mode) for a skewed distribution are not identical.

There are two kinds of skewed distributions, as illustrated below. Observe the relative positions of the mean, median, and mode in each distribution.

mean median mode

Source: codeburst.io

Before moving on, watch this 5-minute video to check your understanding of continuous data distributions.

Binomial distribution
The previous distributions describe the distributions of continuous data. In contrast, for describing the distribution of nominal or categorical data where values can only assume a limited set of categories (e.g. the outcome of flipping a coin, rolling of a die, yes or no, male or female, colours, etc.), the binomial distribution is often used.

The binomial distribution is used when there are exactly two mutually exclusive outcomes of a trial. These outcomes are appropriately labelled "success" and "failure". For example, to obtain the binomial distribution of data obtained from flipping a coin 100 times, we could label "head" as "success" and "tail" as "failure", or vice versa. The binomial distribution then describes the distribution of the probability of obtaining the head outcome over 100 trials. It answers such questions as "what is the probability of obtaining 50 heads from flipping a coin 100 times?"

Carefully observe four examples of the binomial distribution below. Let us assume that they describe the probability of obtaining the "success" outcome from tossing a coin 100 times (100 trials). Notice that the x-axis represents all possible numbers of times (frequencies) that the "success" outcome can be obtained (given a certain probability) and the y-axis represents their corresponding probabilities. In this way, the binomial distribution histogram differs slightly from other general histograms. Finally note that the shapes of the binomial distributions resemble normal distributions, especially when the data is considered 'large enough'.

binomial.PNG

Source: nist.gov

In a fair coin toss, if the probability of obtaining a head in a single toss is 0.5 (or 50%), then the probability of "success" is defined as 0.5 (P=0.50). The binomial distribution for such data, described by the lower left histogram in the above example, suggests that obtaining 50 heads in 100 trials has the highest probability (0.08).

On the contrary, if we believe that the coin is not a fair one and assume that the chance of obtaining a head is merely 0.1, then the upper left histogram is a more appropriate description of how the data is actually distributed. In this case, it is highly unlikely that we will obtain more than 20 heads out of 100 trials.


42729616-1f92-499e-bd4e-e9f461b01f2e.png
7c924474-27bb-489f-bf02-cafc72545dd0.png
1edc3931-5b0e-4d4e-b7ff-e17f253dbdb7.png
54fd8f7e-0e7b-40d2-b1cc-c5d9a273aec9.png
7fb29134-7b4c-47f5-8cb4-220b678a6ac3.png
d39e1a52-e126-4181-87c9-d49c3d47af7f.png
27404fcd-5e80-45b6-afe5-fdbdaf0cafe0.png
7ca98dd2-0290-4d4d-a223-7511f69dd91b.png
take idea from it and say how my histogram is 

d5c20af3-d920-43e6-afa6-288a574574f9.png
this one 

0efb40d5-99fc-4a2e-a86f-3ed2ae613ff5.png
Midfielders (MF): here, the histogram shows a positively skewed (right-skewed) distribution. Most players are concentrated at lower to middle completed passes per 90 values, while a few high values extend the tail to the right. This is also supported by the mean (33.93) being greater than the median (31.48). u need to describe and mention like this i guess After histogram:

Shape/distribution: MF and DF appear positively
(right) skewed.

 
Where most values are concentrated: roughly the middle/lower
ranges.

 
Tail: fewer observations occur at very high
completed-passes-per-90 values.

 
Connection to statistics: mean > median for both groups,
supporting the right-skew interpretation.

 
Comparison: DF values appear somewhat shifted higher than MF
values.


344c88d8-f447-4478-9383-794124acc629.png
can u give me this in word teacher may think its AI generated 


Assignment 2 Objective 1.docx
Document
so all good yeah 

Yes mate — I checked the document. Your statistical analysis is good overall, and the final t-test section is correct. Your hypotheses, test statistic, p-value, and conclusion all line up correctly. 


There are just a few small things I'd fix before submitting:

On page 1, your example says 82.09 and then the calculation says 82.08. 747/819×90=82.09 when rounded to 2 decimals, so use 82.09 consistently. 


Change “Players who have the less 90 minutes” to “Players who played less than 90 minutes were filtered out.” 


Under descriptive statistics, “Before these descriptive statistics take random sample:” sounds unfinished. Replace it with “A simple random sample was selected before calculating the descriptive statistics.” 


In your hypothesis section, you currently have “Where and represent the population mean…” — the symbols disappeared. Change it to: “Where μMF and μDF represent the population mean completed passes per 90 for midfielders and defenders, respectively.” 


Your final sentence “Since the p-value ... is less than 0.05, and the null hypothesis is rejected” would read better as: “Since the p-value (0.0151) is less than 0.05, the null hypothesis is rejected.” 


Most importantly, nothing is fundamentally wrong with your analysis. Your final result is:

p = 0.0151 < 0.05 → Reject H₀ → There is a statistically significant difference in average completed passes per 90 between MF and DF, with defenders having the higher sample mean (38.96 vs 33.93).

So don't redo the analysis. Just clean up those few wording/formatting issues before submission.



Assignment 2 Objective 1(1).docx
Document
can u create a read me file from this 

Yep mate. I created a clean README.md based on your Objective 1 document, including the analytic question, sampling, descriptive statistics, histogram findings, confidence intervals, t-test, and final conclusion. 


Download README.md 


README.md
Document


9e308dd4-7a2c-4b7c-8096-0a51fb3bfc96.png
u idot u can't make table like this 

ehere is histogram for defenders as well 

Yes bro — the README already includes the defenders histogram interpretation, but it does not include the actual histogram image.

For the Defenders (DF) section, it currently says:

Slightly positively (right) skewed — Most players are concentrated around the middle values, while a few higher values extend the tail to the right. Mean = 38.96 and median = 37.32.

Your actual defender histogram is the one shown on page 3 of your document. 


If you mean you want me to put BOTH actual histogram images (MF and DF) inside the README.md, yes — I can update the README with both images.


in read me file 

Yes bro — fixed. The README now includes both actual histogram images:

Midfielders histogram

Defenders histogram

Interpretation under each histogram

All your tables and statistical results

Download these 3 files and keep them together in the same GitHub folder:

Download README.md
Download Midfielders Histogram
Download Defenders Histogram

That way GitHub will display both histograms directly inside the README. 


README.md
Document


histogram_midfielders.png
Image


histogram_defenders.png
Image


manishkat/PRT581-GroupAssessment2: FIFA World Cup 2026 data analysis — PRT581 Assessment 2 (Group Project). Statistical comparison of passing, fouls, shots, and possession performance using Python (pandas, scipy). Includes data wrangling, sampling, descriptive & inferential statistics, and two-sample t-tests for each task. push it here in this repo


Yes bro — I can push the README and both histogram images to that GitHub repo, but you need to connect the GitHub plugin first using the prompt above.

Once it’s connected, I can publish these files into:

manishkat/PRT581-GroupAssessment2

Files ready to push:

README.md

histogram_midfielders.png

histogram_defenders.png

After you connect GitHub, just say “push it”.


i need code 

Yep bro — if you mean the Git commands to push the README and histogram images to that repo, use this.

First open PowerShell in the folder where your files are saved, then run:

git clone https://github.com/manishkat/PRT581-GroupAssessment2.git
cd PRT581-GroupAssessment2
Now copy these files into that folder:

README.md
histogram_midfielders.png
histogram_defenders.png
Then run:

git add README.md histogram_midfielders.png histogram_defenders.png
git commit -m "Add passing analysis README and histogram images"
git push origin main
If the repo is already cloned on your computer, you only need:

git pull origin main
git add README.md histogram_midfielders.png histogram_defenders.png
git commit -m "Add passing analysis README and histogram images"
git push origin main
And inside your README.md, keep these lines so the images appear on GitHub:

### Midfielders (MF)

![Histogram of Completed Passes per 90 - Midfielders](histogram_midfielders.png)

### Defenders (DF)

![Histogram of Completed Passes per 90 - Defenders](histogram_defenders.png)
If your branch is called master instead of main, replace main with master.


Then don’t merge it, mate. Since you already started a merge, first cancel that merge:

git merge --abort
After that, if you want to push only your own work without combining with the existing repo history, you have two options.

The cleanest is to push your work to a new branch:

git checkout -b indra-passing-analysis
git add .
git commit -m "Add completed passes analysis"
git push -u origin indra-passing-analysis
That keeps the existing main branch untouched.

If you want your files directly on main without merging the existing work, that would require overwriting/replacing history, which is risky in a group repo. I would not recommend that unless the group explicitly wants it.

So for your case, use a separate branch.


what is merging u mean what to merge 

By merge, I mean Git is trying to combine your local Final FDS files/history with the files/history that are already on the GitHub repository.

When you ran:

git pull origin main --allow-unrelated-histories
Git downloaded the existing group repo and tried to combine it with your local work.

The problem happened specifically with:

README.md
There is already a README.md on GitHub, and you also have a README.md locally. Git doesn't know which content you want, so it reported:

CONFLICT (add/add): Merge conflict in README.md
It doesn't mean your statistical data is being merged together. It's Git combining the two sets of repository files.

If your intention is simply:

“I want to add my files to the existing group repo without deleting the files already there.”

then yes, technically Git needs to integrate the existing repository with your local files. We can resolve the README conflict and then push both your work and their existing work safely.

Don't run anything else yet if that's what you want — I can give you the exact 3–4 commands from your current screen.


“I want to add my files to the existing group repo without deleting the files already there.”  

Exactly — then you do want to integrate your files into the existing repo, but you do not want to delete or overwrite the files already there.

Right now Git stopped because both sides have a README.md. The safest move is: keep the existing group README.md, then add your own README under a different filename.

From your current state, run:

git checkout --theirs README.md
git add README.md
Then rename your own local README file to something unique, for example:

README_Indra_Passing_Analysis.md
Put that renamed file back into:

C:\CDU S2 2026\Final FDS
Then run:

git add .
git commit -m "Add completed passes analysis"
git push origin main
That way:

existing group files stay there ✅

existing group README.md stays there ✅

your Python files/data get added ✅

your own README can still be included under a different name ✅

Do not use --force.


Library
/
README.md


FIFA World Cup 2026 - Completed Passes Analysis
Analytic Question
On average, is there a statistically significant difference in
completed passes per 90 minutes between midfielders and defenders at the
FIFA World Cup 2026?

Analysis Overview
Completed passes per 90 minutes was used to make the comparison fair
because players had different amounts of playing time. Comparing total
completed passes could favour players who played more minutes.

Formula:

Completed Passes per 90 = (Completed Passes / Minutes Played) × 90

Players who played less than 90 minutes were filtered out. Completed
passes per 90 was calculated to standardise passing performance across
different playing times.

Data Preparation and Sampling
Group Eligible Population Random Sample

Midfielders (MF) 248 115
Defenders (DF) 275 115
Total 523 230

Simple random sampling was used to select 115 players from each group.
random_state=42 was used to make the random selection reproducible.

Python Files
File Purpose

descriptive_stats.py Calculates descriptive statistics
for midfielders and defenders

histogram.py Creates histograms of completed
passes per 90

confidence_interval.py Calculates the 95% confidence
intervals

Descriptive Statistics
Statistic Midfielders (MF) Defenders (DF)

Sample Size (n) 115 115
Mean 33.93 38.96
Median 31.48 37.32
Mode 24.17 30.00
Sample Variance 243.77 241.45
Standard Deviation 15.61 15.54
Minimum 3.85 5.82
Maximum 85.96 80.95
Q1 22.04 27.98
Q3 44.28 48.51
IQR 22.24 20.53

In the sample, defenders completed about 5.03 more passes per 90
minutes on average than midfielders.

Histograms
Midfielders (MF)


The midfielder histogram shows a positively (right) skewed
distribution. Most players are concentrated at lower-to-middle
completed passes per 90 values, while a few high values extend the tail
to the right. This is supported by the mean (33.93) being greater
than the median (31.48).

Defenders (DF)


The defender histogram shows a slightly positively (right) skewed
distribution. Most players are concentrated around the middle
completed passes per 90 values, while a few higher values extend the
tail to the right. This is supported by the mean (38.96) being
slightly greater than the median (37.32).

95% Confidence Interval
Group Mean Lower Limit Upper Limit Interval Size

Midfielders (MF) 33.93 31.04 36.81 5.77
Defenders (DF) 38.96 36.09 41.83 5.74

At the 95% confidence level, the estimated population mean ranges from
31.04 to 36.81 completed passes per 90 for midfielders and 36.09
to 41.83 for defenders.

Two-Sample t-Test (Independent t-Test)
Step 1: State
The analytic question investigates whether midfielders and defenders
differ in their average completed passes per 90 minutes.

Step 2: Plan
A two-sided independent two-sample t-test was used because the question
investigates whether there is a difference without specifying which
group should have a higher mean.

Hypothesis Statement

H₀: μMF = μDF There is no difference in the
population mean completed passes
per 90 between midfielders and
defenders.

Step 3: Solve
Statistic MF DF

Sample Size 115 115
Mean 33.93 38.96
Standard Deviation 15.61 15.54

Test Result Value

t-statistic (t*) -2.45
p-value 0.0151
Significance level (α) 0.05
Decision Reject H₀

Since 0.0151 < 0.05, the null hypothesis is rejected.

Step 4: Conclude
There is statistically significant evidence that midfielders and
defenders differ in their average completed passes per 90 minutes.
Defenders recorded a higher sample mean (38.96) than midfielders
(33.93).

