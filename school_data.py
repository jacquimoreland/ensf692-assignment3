# school_data.py
# Jacqui Moreland
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022
import math

# Declare any global variables needed to store the data here
enrollement_data = np.array([year_2013.reshape(20,3), year_2014.reshape(20,3), year_2015.reshape(20,3), 
                                   year_2016.reshape(20,3), year_2017.reshape(20,3), year_2018.reshape(20,3), 
                                   year_2019.reshape(20,3), year_2020.reshape(20,3), year_2021.reshape(20,3), 
                                   year_2022.reshape(20,3)])

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


# You may add your own additional classes, functions, variables, etc.


def main():
    print("\n***ENSF 692 School Enrollment Statistics***\n")
    
    # Print Stage 1 requirements here
    print("Shape of full data array: ", enrollement_data.shape)
    print("Dimensions of full data array: ", enrollement_data.ndim)

    # Prompt for user input
    global school_index
    try: 
        user_input = input("Please enter the highschool name or school code: ")
        # check that the provided school name or code is valid
        isSchool = False
        for row, school_id in schools.items():
            if user_input in school_id:
                isSchool = True
                school_index = row
                break 
            else:
                isSchool = False
        # Raise exception if not valid
        if isSchool == False:
            raise ValueError("You must enter a valid school name or code.")
    
    except ValueError as err:
        print(err)
        return
    
    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")

    print("School Name: ", schools[school_index][1], ", School Code: ", schools[school_index][0])

    # Enrollment data: 1st index = years, 2nd index = school, 3rd index = grade
    grade10_all_years = enrollement_data[:, school_index, 0]  
    mean_grade10_all_years = np.nanmean(grade10_all_years, axis=0)
    print(f"Mean enrollment for Grade 10: {math.trunc(mean_grade10_all_years)}")
    

    grade11_all_years = enrollement_data[:, school_index, 1]
    mean_grade11_all_years = np.nanmean(grade11_all_years, axis=0)
    print(f"Mean enrollment for Grade 11: {math.trunc(mean_grade11_all_years)}")

    grade12_all_years = enrollement_data[:, school_index, 2]
    mean_grade12_all_years = np.nanmean(grade12_all_years, axis=0) 
    print(f"Mean enrollment for Grade 11: {math.trunc(mean_grade12_all_years)}")

    all_grades_all_years = enrollement_data[:, school_index, :]
    all_grades_all_years.reshape(1, 30)
    max_all_grades_all_years = np.nanmax(all_grades_all_years)
    print(f"Highest enrollment for a single grade: {math.trunc(max_all_grades_all_years)}")

    min_all_grades_all_years = np.nanmin(all_grades_all_years)
    print(f"Lowest enrollment for a single grade: {math.trunc(min_all_grades_all_years)}")

    all_grade_2013 = enrollement_data[0, school_index, :]
    total_2013 = np.nansum(all_grade_2013)
    print(f"Total enrollment for 2013: {math.trunc(total_2013)}")

    all_grade_2014 = enrollement_data[1, school_index, :]
    total_2014 = np.nansum(all_grade_2014)
    print(f"Total enrollment for 2014: {math.trunc(total_2014)}")

    all_grade_2015 = enrollement_data[2, school_index, :]
    total_2015 = np.nansum(all_grade_2015)
    print(f"Total enrollment for 2015: {math.trunc(total_2015)}")

    all_grade_2016 = enrollement_data[3, school_index, :]
    total_2016 = np.nansum(all_grade_2016)
    print(f"Total enrollment for 2016: {math.trunc(total_2016)}")

    all_grade_2017 = enrollement_data[4, school_index, :]
    total_2017 = np.nansum(all_grade_2017)
    print(f"Total enrollment for 2017: {math.trunc(total_2017)}")

    all_grade_2018 = enrollement_data[5, school_index, :]
    total_2018 = np.nansum(all_grade_2018)
    print(f"Total enrollment for 2018: {math.trunc(total_2018)}")

    all_grade_2019 = enrollement_data[6, school_index, :]
    total_2019 = np.nansum(all_grade_2019)
    print(f"Total enrollment for 2019: {math.trunc(total_2019)}")

    all_grade_2020 = enrollement_data[7, school_index, :]
    total_2020 = np.nansum(all_grade_2020)
    print(f"Total enrollment for 2020: {math.trunc(total_2020)}")

    all_grade_2021 = enrollement_data[8, school_index, :]
    total_2021 = np.nansum(all_grade_2021)
    print(f"Total enrollment for 2021: {math.trunc(total_2021)}")

    all_grade_2022 = enrollement_data[9, school_index, :]
    total_2022 = np.nansum(all_grade_2022)
    print(f"Total enrollment for 2022: {math.trunc(total_2022)}")

    total_all_years = np.nansum(all_grades_all_years)
    print(f"Total ten year enrollment: {math.trunc(total_all_years)}")

    
    totals = np.array([total_2013, total_2014, total_2015, total_2016, total_2017, 
                       total_2018, total_2019, total_2020, total_2021, total_2022])
    mean_totals = np.nanmean(totals)
    print(f"Mean total enrollment over 10 years: {math.trunc(mean_totals)}")

    over_500 = all_grades_all_years > 500
    median_over_500 = np.nanmedian(all_grades_all_years[over_500])
    print(f"For all enrollments over 500, the median value was: {math.trunc(median_over_500)}")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")

    all_schools_all_grades_2013 = enrollement_data[0, :, :]
    mean_2013 = np.nanmean(all_schools_all_grades_2013)
    print(f"Mean enrollment in 2013: {math.trunc(mean_2013)}")

    all_schools_all_grades_2022 = enrollement_data[9, :, :]
    mean_2022 = np.nanmean(all_schools_all_grades_2022)
    print(f"Mean enrollment in 2022: {math.trunc(mean_2022)}")

    all_schools_grade12_2022 = enrollement_data[9, :, 2]
    total_grad_2022 = np.nansum(all_schools_grade12_2022)
    print(f"Total graduating class of 2022: {math.trunc(total_grad_2022)}")

    max_enrollment = np.nanmax(enrollement_data)
    print(f"Highest enrollment for a single grade: {math.trunc(max_enrollment)}")

    min_enrollment = np.nanmin(enrollement_data)
    print(f"Lowest enrollment for a single grade: {math.trunc(min_enrollment)}\n")


if __name__ == '__main__':
    main()

