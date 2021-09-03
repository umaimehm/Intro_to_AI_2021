<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<h3 align="center">Dave3625 - Lab1</h3>
<p align="center">
  <a href="https://github.com/-/Dave3625-21-Lab/tree/main/Lab1">
    <img src="img/logo.png" alt="Data wrangling" width="791" height="442">
  </a>

  

  <p align="center">
    A exercise in pandas for cleaning and plotting a small dataset <br \>The set contains 50 rows of: StudentID, Age, email, hrsStudy, FinalGrade
    <br />
    ·
    <a href="https://github.com/-/Dave3625-21-Lab/issues">Report Bug</a>
    ·
    <a href="https://github.com/-/Dave3625-21-Lab/issues">Request Feature</a>
  </p>
</p>


<!-- ABOUT THE LAB -->
## About The Lab
Most of the time spent working on AI, is actually time spent preparing data. You need to figure out what datapoints to use, and if you can combine datapoints to get a better model. 
The first task when working with a new dataset is to clean the data and solve data errors. In the file stud.csv, we have 50 entries with:
StudentID, Age, email, hrsStudy, FinalGrade

We will be using [pandas][pandas-doc] and [numpy][numpy-doc].

## Tasks
**1. In this lab, you will import the csv file into pandas:**

Hint: 
```
#If you want to use the csv from this git set
# url = "https://raw.githubusercontent.com/-/Dave3625-21-Lab/main/Lab1/stud.csv"
# You can also download the csv and set
# url="{filepath]/ctud.csv"
df = pd.read_csv(url, sep=',')
df.head()

```


**2. You will then clean the data set so df.info() produce**

![dfinfo][dfinfo]

Hint: 
```
df.isna().sum() #show missing values
df=df.replace(r'^\s*$', np.nan, regex=True) #Replace blank values with np.nan values

df['Column'] = df['Column'].astype(str).astype(int) #Convert from obj to int
```
**3. Then idenify and remove the outliers in the «FinalGrade» column**

Hint : 
```
df["FinalGrade"].plot.box()
```

**4. Finally add a column “Grade” where you transform the grade from float to a char:**

[Hint][columns-condition]
```
91 - 100 = A
81 - 90  = B
71 - 80  = C
61 – 70  = D
51 – 60  = E
   > 50  = F
```
**5. Produce this plot:**

![barplot]

The dataset is generated with this script and errors added after it's creation:
```python
import random
print(StudentID,Age,email,hrsStudy,FinalGrade)
for i in range(50):
   studId ="s" + str(random.randrange(10000,99999,1)) 
   print(str(studId)+","+ str(random.randrange(19,35,1))+",
      "+str(studId+"@oslomet.no"+","+str(random.randint(0, 12)))+","+str(random.randint(20, 100)))
```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[issues-shield]: https://img.shields.io/github/issues/-/Dave3625-21-Lab.svg?style=for-the-badge
[issues-url]: https://github.com/-/Dave3625-21-Lab/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/-/Dave3625-21-Lab/blob/main/Lab1/LICENSE

[dfinfo]: img/dfinfo.png
[barplot]: img/barplot.png
[pandas-doc]: https://pandas.pydata.org/docs/reference/index.html#api
[numpy-doc]: https://numpy.org/doc/stable/
[columns-condition]: https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/


