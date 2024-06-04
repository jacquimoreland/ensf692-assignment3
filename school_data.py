# school_data.py
# Jacqui Moreland

# A terminal-based application for computing and printing statistics based on given input.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022
import math

# Enrollment data contains the number of students enrolled in Grades 10-12 across 20 schools for the years 2013-2022
# Enrollment data: 1st index = year, 2nd index = school, 3rd index = grade
enrollment_data = np.array([year_2013.reshape(20,3), year_2014.reshape(20,3), year_2015.reshape(20,3), 
                                   year_2016.reshape(20,3), year_2017.reshape(20,3), year_2018.reshape(20,3), 
                                   year_2019.reshape(20,3), year_2020.reshape(20,3), year_2021.reshape(20,3), 
                                   year_2022.reshape(20,3)])

# School dictionary contains array index as the key, and the school code and name as the value list
schools = {0: ['1224', 'Centennial High School'],
           1: ['1679', 'Robert Thirsk School'],
           2: ['9626', 'Louise Dean School'],
           3: ['9806', 'Queen Elizabeth High School'],
           4: ['9813', 'Forest Lawn High School'],
           5: ['9815', 'Crescent Heights High School'],
           6: ['9816', 'Western Canada High School'],
           7: ['9823', 'Central Memorial High School'],
           8: ['9825', 'James Fowler High School'],
           9: ['9826', 'Ernest Manning High School'],
           10: ['9829', 'William Aberhart High School'],
           11: ['9830', 'National Sport School'],
           12: ['9836', 'Henry Wise Wood High School'],
           13: ['9847', 'Bowness High School'],
           14: ['9850', 'Lord Beaverbrook High School'],
           15: ['9856', 'Jack James High School'],
           16: ['9857', 'Sir Winston Churchill High School'],
           17: ['9858', 'Dr. E. P. Scarlett High School'],
           18: ['9860', 'John G Diefenbaker High School'],
           19: ['9865', 'Lester B. Pearson High School']}


def mean_enrollment(school_index, grade_index, grade):
    """
    Calculates the mean enrollment for a single grade and a given school across
    all years.

    Args:
        school_index: (int) the index of the enrollment_data array that 
        corresponds to the school in question

        grade_index: (int) the index of the enrollment_data array that 
        corresponds to the grade in question

        grade: (int) the grade in question

    """
    data = enrollment_data[:, school_index, grade_index]  
    mean = np.nanmean(data, axis=0)
    print(f"Mean enrollment for Grade {grade}: {math.trunc(mean)}")


def total_enrollment(school_index, year_index, year):
    """
    Calculates the total enrollment across all grades for a given school and
    a given year. 
    Returns a subarray of enrollment_data which was used to get to the total. 

    Args:
        school_index: (int) the index of the enrollment_data array that 
        corresponds to the school in question

        year_index: (int) the index of the enrollment_data array that 
        corresponds to the year in question

        year: (int) the year in question
    
    Return:
        (numpy array) Subarray of enrollment_data

    """
    data = enrollment_data[year_index, school_index, :]
    total = np.nansum(data)
    print(f"Total enrollment for {year}: {math.trunc(total)}")
    return total


def main():
    print("\n***ENSF 692 School Enrollment Statistics***\n")
    print("Shape of full data array: ", enrollment_data.shape)
    print("Dimensions of full data array: ", enrollment_data.ndim)

    # Index for the enrollment_data array corresponding to the input school
    school_index = 0

    # Prompt for user input until they enter a valid input.
    while True:
        try: 
            user_input = input("Please enter the highschool name or school code: ")
            # Check that the provided school name or code is valid
            isSchool = False
            for row, school_id in schools.items():
                if user_input in school_id:
                    isSchool = True
                    # Set the school index based on the row of the dictionary
                    school_index = row
                    break 
                else:
                    isSchool = False
            # Raise ValueError exception if not valid
            if isSchool == False:
                raise ValueError("You must enter a valid school name or code.")
            else:
                break
        except ValueError as err:
            print(err)
    
    # The following section calculates statistics for the school indicated by the user. 
    print("\n***Requested School Statistics***\n")
    print("School Name: ", schools[school_index][1], ", School Code: ", schools[school_index][0])

    # Calculate and print out the mean enrollment for Grades 10, 11, and 12 across all years.
    mean_enrollment(school_index=school_index, grade_index=0, grade=10) 
    mean_enrollment(school_index=school_index, grade_index=1, grade=11)
    mean_enrollment(school_index=school_index, grade_index=2, grade=12)

    # Calculate and print out the highest enrollment for any grade across all years. 
    all_grades_all_years = enrollment_data[:, school_index, :]
    all_grades_all_years.reshape(1, 30)
    max_all_grades_all_years = np.nanmax(all_grades_all_years)
    print(f"Highest enrollment for a single grade: {math.trunc(max_all_grades_all_years)}")

    # Calculate and print out the lowest enrollment for any grade across all years. 
    min_all_grades_all_years = np.nanmin(all_grades_all_years)
    print(f"Lowest enrollment for a single grade: {math.trunc(min_all_grades_all_years)}")

    # Calculate and print out the total enrollment for a specific school for years 2013-2022. 
    total_2013 = total_enrollment(school_index=school_index, year_index=0, year=2013)
    total_2014 = total_enrollment(school_index=school_index, year_index=1, year=2014)
    total_2015 = total_enrollment(school_index=school_index, year_index=2, year=2015)
    total_2016 = total_enrollment(school_index=school_index, year_index=3, year=2016)
    total_2017 = total_enrollment(school_index=school_index, year_index=4, year=2017)
    total_2018 = total_enrollment(school_index=school_index, year_index=5, year=2018)
    total_2019 = total_enrollment(school_index=school_index, year_index=6, year=2019)
    total_2020 = total_enrollment(school_index=school_index, year_index=7, year=2020)
    total_2021 = total_enrollment(school_index=school_index, year_index=8, year=2021)
    total_2022 = total_enrollment(school_index=school_index, year_index=9, year=2022)

    # Calculate and print out the total enrollment for a specific school across all 10 years.
    total_all_years = np.nansum(all_grades_all_years)
    print(f"Total ten year enrollment: {math.trunc(total_all_years)}")

    # Calculate and print out the mean total enrollment for a specific school across all 10 years. 
    totals = np.array([total_2013, total_2014, total_2015, total_2016, total_2017, 
                       total_2018, total_2019, total_2020, total_2021, total_2022])
    mean_totals = np.nanmean(totals)
    print(f"Mean total enrollment over 10 years: {math.trunc(mean_totals)}")

    # Print out the median value of enrollments over 500 across all 10 years for a specific school. 
    # If there were no enrollments above 500, print out that out. 
    over_500 = all_grades_all_years > 500
    if np.any(over_500) == True:
        median_over_500 = np.nanmedian(all_grades_all_years[over_500])
        print(f"For all enrollments over 500, the median value was: {math.trunc(median_over_500)}")
    else:
        print("No enrollments over 500.")
    

    # The following section calculates non-school speficic statistics.
    print("\n***General Statistics for All Schools***\n")

    # Calulate and print out the mean enrollment in 2013. 
    all_schools_all_grades_2013 = enrollment_data[0, :, :]
    mean_2013 = np.nanmean(all_schools_all_grades_2013)
    print(f"Mean enrollment in 2013: {math.trunc(mean_2013)}")

    # Calulate and print out the mean enrollment in 2022.
    all_schools_all_grades_2022 = enrollment_data[9, :, :]
    mean_2022 = np.nanmean(all_schools_all_grades_2022)
    print(f"Mean enrollment in 2022: {math.trunc(mean_2022)}")

    # Calulate and print out the total number of students in Grade 12 in 2022.
    all_schools_grade12_2022 = enrollment_data[9, :, 2]
    total_grad_2022 = np.nansum(all_schools_grade12_2022)
    print(f"Total graduating class of 2022: {math.trunc(total_grad_2022)}")

    # Calulate and print out the highest enrollment across all years, all schools and all grades.
    max_enrollment = np.nanmax(enrollment_data)
    print(f"Highest enrollment for a single grade: {math.trunc(max_enrollment)}")

    # Calulate and print out the lowest enrollment across all years, all schools and all grades.
    min_enrollment = np.nanmin(enrollment_data)
    print(f"Lowest enrollment for a single grade: {math.trunc(min_enrollment)}\n")


if __name__ == '__main__':
    main()

