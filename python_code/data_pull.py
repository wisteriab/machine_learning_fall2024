import requests
import re  
import pandas as pd 
url = (
    'https://api.census.gov/data/2023/cps/asec/mar?get='
    'A_LINENO,'
    'A_AGE,'
    'A_DTIND,'
    'A_DTOCC,'
    'A_ENRLW,'
    'A_EXPLF,'
    'A_FAMNUM,'
    'A_FTLF,'
    'A_FTPT,'
    'A_HGA,'
    'A_HSCOL,'
    'A_GRSWK,'
    'A_HRLYWK,'
    'A_HRS1,'
    'A_LFSR,'
    'A_MARITL,'
    'A_MJOCC,'
    'A_SEX,'
    'A_UNCOV,'
    'A_UNMEM,'
    'A_UNTYPE,'
    'A_WKSLK,'
    'A_WKSTAT,'
    'AGE1,'
    'AGI,'
    'CHCARE_YN,'
    'HCHCARE_VAL,'
    'HCHCARE_YN,'
    'COV_CYR,'
    'DEPPRIV,'
    'ESICOULD,'
    'FAMLIS,'
    'FEARNVAL,'
    'FFPOS,'
    'FMED_VAL,'
    'FMOOP,'
    'FOTC_VAL,'
    'FRNTVAL,'
    'GESTFIPS,'
    'GTCBSAST'
    '&for=state:*'
    '&key=b4cdb850b47d0c5c108b69a6d44a5c1c60f98e3b'
)
response = requests.get(url)
result = response.json()
df = pd.DataFrame(result)
df.columns=df.iloc[0] 
df = df.iloc[1:]
df.to_csv("../data/raw_data/census_raw.csv")


#Rename columns for ease of understanding
column_mask = {
    'A_LINENO' : 'line',
    'A_AGE' : 'age',
    'A_DTIND' : 'job_industry',
    'A_DTOCC' : 'job_industry_recode',
    'A_ENRLW' : 'school_enroll_lastweek',
    'A_EXPLF'  : 'employment',
    'A_FAMNUM' : 'fam_size',
    'A_FTLF' : 'full_time_work',
    'A_FTPT' : 'full_part_school',
    'A_HGA' : 'highest_education',
    'A_HSCOL' : 'hs_col_unenrolled',
    'A_GRSWK' : 'weekly_earnings',
    'A_HRLYWK' : 'hourly_work_yn',
    'A_HRS1' : 'hours_worked',
    'A_LFSR' : 'labor_force_recode',
    'A_MARITL' : 'marital_status',
    'A_MJOCC' : 'main_job_industry_recode',
    'A_SEX' : 'sex',
    'A_UNCOV' : 'union_contract_avail',
    'A_UNMEM' : 'union_member_yn',
    'A_UNTYPE' : 'reason_unemployed',
    'A_WKSLK' : 'weeks_unemployed',
    'A_WKSTAT' : 'ft_pt_unem',
    'AGE1' : 'age_recode_gt15',
    'AGI' : 'federal_gross_income_adj',
    'CHCARE_YN' : 'need_childcare',
    'HCHCARE_VAL' : 'hh_childcare_val',
    'HCHCARE_YN' : 'hh_childcare',
    'COV_CYR' : 'health_insurance_ly',
    'DEPPRIV' : 'dependent_private_insured',
    'ESICOULD' : 'company_offer_insurance',
    'FAMLIS' : 'poverty_ratio',
    'FEARNVAL' : 'family_earn_ly',
    'FFPOS' : 'fam_id',
    'FMED_VAL' : 'fam_med_costs',
    'FMOOP' : 'fam_outofpocket_med_costs',
    'FOTC_VAL' : 'fam_otc_med_costs',
    'FRNTVAL' : 'fam_rent_val',
    'GESTFIPS' : 'fips',
    'GTCBSAST' : 'state'
}
df.rename(columns=column_mask, inplace=True)
#Reformat categorical data to their proper labels
job_industry_recode_map = {
      "5": "Life, physical, and social service occupations",
      "12": "Protective service occupations",
      "17": "Office and administrative support occupations",
      "10": "Healthcare practitioner and technical occupations",
      "11": "Healthcare support occupations",
      "3": "Computer and mathematical science occupations",
      "1": "Management occupations",
      "15": "Personal care and service occupations",
      "16": "Sales and related occupations",
      "22": "Transportation and material moving occupations",
      "21": "Production occupations",
      "8": "Education, training, and library occupations",
      "13": "Food preparation and serving related occupations",
      "2": "Business and financial operations occupations",
      "7": "Legal occupations",
      "23": "Armed Forces",
      "9": "Arts, design, entertainment, sports, and media occupations",
      "0": "Not in universe, or children",
      "4": "Architecture and engineering occupations",
      "20": "Installation, maintenance, and repair occupations",
      "19": "Construction and extraction occupations",
      "14": "Building and grounds cleaning and maintenance occupations",
      "18": "Farming, fishing, and forestry occupations",
      "6": "Community and social service occupations"
    }
school_enroll_lastweek_map = {
      "0": "Not in univ. or children & Armed Forces",
      "2": "No",
      "1": "Yes"
    }
highest_education_map = {
      "35": "9th Grade",
      "41": "Assc degree-occupation/vocation",
      "0": "Children",
      "31": "Less Than 1st Grade",
      "44": "Master's degree (MA,MS,MENG,MED,MSW,MBA)",
      "43": "Bachelor's degree (BA,AB,BS)",
      "34": "7th and 8th grade",
      "38": "12th Grade No Diploma",
      "37": "11th Grade",
      "33": "5th Or 6th Grade",
      "45": "Professional school degree (MD,DDS,DVM,L",
      "39": "High school graduate-high school diploma",
      "32": "1st,2nd,3rd,or 4th grade",
      "40": "Some College But No Degree",
      "46": "Doctorate degree (PHD,EDD)",
      "36": "10th Grade",
      "42": "Assc degree-academic program"
    }
labor_force_recode_map = {
      "4": "Unemp,on layoff",
      "1": "Working",
      "0": "Not In Universe",
      "2": "W/job,not at work",
      "3": "Unemp,looking for work",
      "7": "Not in labor force"
    }
marital_status_map = {
      "4": "Widowed",
      "1": "Marr-civ sp present",
      "6": "Separated",
      "5": "Divorced",
      "7": "Never married",
      "3": "Marr-spouse absent",
      "2": "Marr-AF spo present"
    }
main_job_industry_recode_map = {
      "11": "Armed Forces",
      "9": "Production occupations",
      "4": "Sales and related occupations",
      "0": "Not in universe, or children",
      "5": "Office and administrative support occupations",
      "6": "Farming, fishing, and forestry occupations",
      "8": "Installation, maintenance, and repair occupations",
      "10": "Transportation and material moving occupations",
      "3": "Service occupations",
      "2": "Professional and related occupations",
      "7": "Construction and extraction occupations",
      "1": "Management, business, and financial occupations"
    }
sex_map = {
      "2": "Female",
      "1": "Male"
    }
union_contract_avail_map = {
      "1": "Yes",
      "0": "Not in universe or children & Armed Forc",
      "2": "No"
    }
union_member_yn_map = {
      "1": "Yes",
      "0": "Not in universe or children & Armed Forc",
      "2": "No"
    }
reason_unemployed_map = {
      "4": "Re-entrant",
      "3": "Job leaver",
      "2": "Other job loser",
      "0": "Not in univ or children or Armed Forces",
      "1": "Job loser - on layoff",
      "5": "New entrant"
    }
ft_pt_unem_map = {
      "2": "FT schedules",
      "5": "PT/econ rea,us PT",
      "6": "Unemployed FT",
      "1": "Not in labor force",
      "4": "PT/non-ec rea,us PT",
      "3": "PT/econ rea,us FT",
      "7": "Unemployed PT",
      "0": "Not In Universe"
    }
age_recode_gt15_map = {
      "9": "40 to 44 years",
      "6": "25 to 29 years",
      "5": "22 to 24 years",
      "4": "20 and 21 years",
      "8": "35 to 39 years",
      "10": "45 to 49 years",
      "2": "16 and 17 years",
      "11": "50 to 54 years",
      "7": "30 to 34 years",
      "3": "18 and 19 years",
      "16": "70 to 74 years",
      "1": "15 years",
      "0": "Not In Universe",
      "13": "60 to 61 years",
      "12": "55 to 59 years",
      "14": "62 to 64 years",
      "15": "65 to 69 years",
      "17": "75 years and over"
    }
need_childcare_map = {
      "1": "Yes",
      "2": "No",
      "0": "Niu"
    }
hh_childcare_map = {
      "0": "Niu",
      "2": "No",
      "1": "Yes"
    }
health_insurance_ly_map = {
      "0": "Infant born after calendar year",
      "2": "Coverage for some of year",
      "3": "Coverage for all of year",
      "1": "No Coverage"
    }
dependent_private_insured_map = {
      "0": "Out of universe",
      "1": "Yes",
      "2": "No"
    }
company_offer_insurance_map = {
      "2": "No",
      "1": "Yes",
      "0": "NIU"
    }
poverty_ratio_map = {
      "1": "BELOW POVERTY LEVEL",
      "4": "150 AND ABOVE THE POVERTY LEVEL",
      "3": "125 - 149 PERCENT OF THE POVERTY LEVEL",
      "2": "100 - 124 PERCENT OF THE POVERTY LEVEL",
      "-1": "NOT IN POVERTY UNIVERSE"
    }
fips_map =  {
      "51": "VA",
      "21": "KY",
      "15": "HI",
      "45": "SC",
      "44": "RI",
      "36": "NY",
      "55": "WI",
      "26": "MI",
      "22": "LA",
      "30": "MT",
      "41": "OR",
      "47": "TN",
      "25": "MA",
      "27": "MN",
      "31": "NE",
      "42": "PA",
      "53": "WA",
      "18": "IN",
      "46": "SD",
      "10": "DE",
      "16": "ID",
      "1": "AL",
      "50": "VT",
      "56": "WY",
      "9": "CT",
      "35": "NM",
      "6": "CA",
      "23": "ME",
      "33": "NH",
      "40": "OK",
      "49": "UT",
      "13": "GA",
      "20": "KS",
      "32": "NV",
      "37": "NC",
      "8": "CO",
      "19": "IA",
      "34": "NJ",
      "28": "MS",
      "38": "ND",
      "5": "AR",
      "54": "WV",
      "11": "DC",
      "12": "FL",
      "29": "MO",
      "2": "AK",
      "39": "OH",
      "4": "AZ",
      "48": "TX",
      "17": "IL",
      "24": "MD"
    }
hourly_map = {
      "2": "No",
      "1": "Yes",
      "0": "Not in universe or children & Armed Forc"
    }
df.job_industry_recode = df.job_industry_recode.map(job_industry_recode_map)
df.school_enroll_lastweek = df.school_enroll_lastweek.map(school_enroll_lastweek_map)
df.highest_education = df.highest_education.map(highest_education_map)
df.labor_force_recode = df.labor_force_recode.map(labor_force_recode_map)
df.marital_status = df.marital_status.map(marital_status_map)
df.main_job_industry_recode = df.main_job_industry_recode.map(main_job_industry_recode_map)
df.sex = df.sex.map(sex_map)
df.union_contract_avail = df.union_contract_avail.map(union_contract_avail_map)
df.union_member_yn = df.union_member_yn.map(union_member_yn_map)
df.reason_unemployed = df.reason_unemployed.map(reason_unemployed_map)
df.ft_pt_unem = df.ft_pt_unem.map(ft_pt_unem_map)
df.age_recode_gt15 = df.age_recode_gt15.map(age_recode_gt15_map)
df.need_childcare = df.need_childcare.map(need_childcare_map)
df.hh_childcare = df.hh_childcare.map(hh_childcare_map)
df.health_insurance_ly = df.health_insurance_ly.map(health_insurance_ly_map)
df.dependent_private_insured = df.dependent_private_insured.map(dependent_private_insured_map)
df.company_offer_insurance = df.company_offer_insurance.map(company_offer_insurance_map)
df.poverty_ratio = df.poverty_ratio.map(poverty_ratio_map)
df.fips = df.fips.map(fips_map)
df.hourly_work_yn = df.hourly_work_yn.map(hourly_map)
df.hh_childcare_val = df.hh_childcare_val.replace(-1,0)
#Drop Columns found to be unnecessary
df.drop(columns = ['job_industry', 'line', 'dependent_private_insured'], inplace=True)
#convert data types to integer where necessary
int_columns = ['age', 
            'fam_size', 
            'weekly_earnings', 
            'hours_worked', 
            'weeks_unemployed', 
            'federal_gross_income_adj',
            'hh_childcare_val',
            'family_earn_ly', 
            'fam_med_costs', 
            'fam_outofpocket_med_costs', 
            'fam_otc_med_costs', 
            'fam_rent_val'
]
for col in int_columns:
    df[col] = df[col].astype(int)
df.to_csv("../data/clean_data/data_v1.csv")
