import pandas as pd

branch_data = pd.read_csv(
    'database/CSV/List_of_Branches.csv', sep=',', header=0, na_filter=False)
inst_data = pd.read_csv(
    'database/CSV/List_of_Institute.csv', sep=',', header=0, na_filter=False)
data_2015 = pd.read_csv(
    'database/CSV/Rounds/Round7_2015.csv', sep=',', header=0, na_filter=False)
data_2016_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2016.csv', sep=',', header=0, na_filter=False)
data_2016_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2016.csv', sep=',', header=0, na_filter=False)
data_2017_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2017.csv', sep=',', header=0, na_filter=False)
data_2017_7 = pd.read_csv(
    'database/CSV/Rounds/Round7_2017.csv', sep=',', header=0, na_filter=False)
data_2018_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2018.csv', sep=',', header=0, na_filter=False)
data_2018_7 = pd.read_csv(
    'database/CSV/Rounds/Round7_2018.csv', sep=',', header=0, na_filter=False)
data_2019_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2019.csv', sep=',', header=0, na_filter=False)
data_2019_7 = pd.read_csv(
    'database/CSV/Rounds/Round7_2019.csv', sep=',', header=0, na_filter=False)
data_2020_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2020.csv', sep=',', header=0, na_filter=False)
data_2020_2 = pd.read_csv(
    'database/CSV/Rounds/Round2_2020.csv', sep=',', header=0, na_filter=False)
data_2020_3 = pd.read_csv(
    'database/CSV/Rounds/Round3_2020.csv', sep=',', header=0, na_filter=False)
data_2020_4 = pd.read_csv(
    'database/CSV/Rounds/Round4_2020.csv', sep=',', header=0, na_filter=False)
data_2020_5 = pd.read_csv(
    'database/CSV/Rounds/Round5_2020.csv', sep=',', header=0, na_filter=False)
data_2020_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2020.csv', sep=',', header=0, na_filter=False)
data_2020_CSAB1 = pd.read_csv(
    'database/CSV/Rounds/CSAB_2020_Round1.csv', sep=',', header=0, na_filter=False)
data_2020_CSAB2 = pd.read_csv(
    'database/CSV/Rounds/CSAB_2020_Round2.csv', sep=',', header=0, na_filter=False)
data_2020_provisonal = pd.read_csv(
    'database/CSV/Rounds/Round_2020_P.csv', sep=',', header=0, na_filter=False)
data_2018_provisonal = pd.read_csv(
    'database/CSV/Rounds/Round_2018_P.csv', sep=',', header=0, na_filter=False)
data_2019_provisonal = pd.read_csv(
    'database/CSV/Rounds/Round_2019_P.csv', sep=',', header=0, na_filter=False)
data_2020_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_2020.csv', sep=',', header=0, na_filter=False)
data_2019_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_2019.csv', sep=',', header=0, na_filter=False)
data_2021_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_2021.csv', sep=',', header=0, na_filter=False)
data_2021I_seats = pd.read_csv(
    'database/CSV/Seat_Increase_2021.csv', sep=',', header=0, na_filter=False)
data_CSAB_seats = pd.read_csv(
    'database/CSV/Seat_Matrix_CSAB.csv', sep=',', header=0, na_filter=False)
data_2016_2 = pd.read_csv(
    'database/CSV/Rounds/Round2_2016.csv', sep=',', header=0, na_filter=False)

data_2016_3 = pd.read_csv(
    'database/CSV/Rounds/Round3_2016.csv', sep=',', header=0, na_filter=False)

data_2016_4 = pd.read_csv(
    'database/CSV/Rounds/Round4_2016.csv', sep=',', header=0, na_filter=False)

data_2016_5 = pd.read_csv(
    'database/CSV/Rounds/Round5_2016.csv', sep=',', header=0, na_filter=False)

data_2017_2 = pd.read_csv(
    'database/CSV/Rounds/Round2_2017.csv', sep=',', header=0, na_filter=False)

data_2017_3 = pd.read_csv(
    'database/CSV/Rounds/Round3_2017.csv', sep=',', header=0, na_filter=False)

data_2017_4 = pd.read_csv(
    'database/CSV/Rounds/Round4_2017.csv', sep=',', header=0, na_filter=False)

data_2017_5 = pd.read_csv(
    'database/CSV/Rounds/Round5_2017.csv', sep=',', header=0, na_filter=False)

data_2017_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2017.csv', sep=',', header=0, na_filter=False)

data_2018_2 = pd.read_csv(
    'database/CSV/Rounds/Round2_2018.csv', sep=',', header=0, na_filter=False)

data_2018_3 = pd.read_csv(
    'database/CSV/Rounds/Round3_2018.csv', sep=',', header=0, na_filter=False)

data_2018_4 = pd.read_csv(
    'database/CSV/Rounds/Round4_2018.csv', sep=',', header=0, na_filter=False)

data_2018_5 = pd.read_csv(
    'database/CSV/Rounds/Round5_2018.csv', sep=',', header=0, na_filter=False)

data_2018_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2018.csv', sep=',', header=0, na_filter=False)

data_2019_2 = pd.read_csv(
    'database/CSV/Rounds/Round2_2019.csv', sep=',', header=0, na_filter=False)

data_2019_3 = pd.read_csv(
    'database/CSV/Rounds/Round3_2019.csv', sep=',', header=0, na_filter=False)

data_2019_4 = pd.read_csv(
    'database/CSV/Rounds/Round4_2019.csv', sep=',', header=0, na_filter=False)

data_2019_5 = pd.read_csv(
    'database/CSV/Rounds/Round5_2019.csv', sep=',', header=0, na_filter=False)

data_2019_6 = pd.read_csv(
    'database/CSV/Rounds/Round6_2019.csv', sep=',', header=0, na_filter=False)
data_cb = pd.read_csv(
    'database/CSV/College_Branch.csv', sep=',', header=0, na_filter=False)
data_category = pd.read_csv(
    'database/CSV/College_Category.csv', sep=',', header=0, na_filter=False)


data_2021_1 = pd.read_csv(
    'database/CSV/Rounds/Round1_2021.csv', sep=',', header=0, na_filter=False)
# data_2021_2 = pd.read_csv(
#     'database/CSV/Rounds/Round2_2021.csv', sep=',', header=0, na_filter=False)
# data_2021_3 = pd.read_csv(
#     'database/CSV/Rounds/Round3_2021.csv', sep=',', header=0, na_filter=False)
# data_2021_4 = pd.read_csv(
#     'database/CSV/Rounds/Round4_2021.csv', sep=',', header=0, na_filter=False)
# data_2021_5 = pd.read_csv(
#     'database/CSV/Rounds/Round5_2021.csv', sep=',', header=0, na_filter=False)
# data_2021_6 = pd.read_csv(
#     'database/CSV/Rounds/Round6_2021.csv', sep=',', header=0, na_filter=False)


data_list = {
    'branch': branch_data,
    'institute': inst_data,
    '_2015': data_2015,
    '1_2016': data_2016_1,
    '6_2016': data_2016_6,
    '1_2017': data_2017_1,
    '7_2017': data_2017_7,
    '1_2018': data_2018_1,
    '7_2018': data_2018_7,
    '1_2019': data_2019_1,
    '7_2019': data_2019_7,
    '1_2020': data_2020_1,
    '2_2020': data_2020_2,
    '3_2020': data_2020_3,
    '4_2020': data_2020_4,
    '5_2020': data_2020_5,
    '6_2020': data_2020_6,
    '2020_1': data_2020_CSAB1,
    '2020_2': data_2020_CSAB2,
    'sional_2018': data_2018_provisonal,
    'sional_2019': data_2019_provisonal,
    'sional_2020': data_2020_provisonal,
    'atrix_2020': data_2020_seats,
    'atrix_2019': data_2019_seats,
    'atrix_2021': data_2021_seats,
    'atrix_2021i': data_2021I_seats,
    'atrix_2020_csab': data_CSAB_seats,
    '2_2016': data_2016_2,
    '3_2016': data_2016_3,
    '4_2016': data_2016_4,
    '5_2016': data_2016_5,
    '2_2017': data_2017_2,
    '3_2017': data_2017_3,
    '4_2017': data_2017_4,
    '5_2017': data_2017_5,
    '6_2017': data_2017_6,
    '2_2018': data_2018_2,
    '3_2018': data_2018_3,
    '4_2018': data_2018_4,
    '5_2018': data_2018_5,
    '6_2018': data_2018_6,
    '2_2019': data_2019_2,
    '3_2019': data_2019_3,
    '4_2019': data_2019_4,
    '5_2019': data_2019_5,
    '6_2019': data_2019_6,
    'college_branch': data_cb,
    'college_category': data_category,
    '1_2021': data_2021_1,
    # '2_2021': data_2021_2,
    # '3_2021': data_2021_3,
    # '4_2021': data_2021_4,
    # '5_2021': data_2021_5,
    # '6_2021': data_2021_6,
}

round_2015 = []
round_1_2016 = []
round_6_2016 = []
round_1_2017 = []
round_7_2017 = []
round_1_2018 = []
round_7_2018 = []
round_1_2019 = []
round_7_2019 = []
round_1_2020 = []
round_2_2020 = []
round_3_2020 = []
round_4_2020 = []
round_5_2020 = []
round_6_2020 = []
round_2_2016 = []
round_3_2016 = []
round_4_2016 = []
round_5_2016 = []
round_2_2017 = []
round_3_2017 = []
round_4_2017 = []
round_5_2017 = []
round_6_2017 = []
round_2_2018 = []
round_3_2018 = []
round_4_2018 = []
round_5_2018 = []
round_6_2018 = []
round_2_2019 = []
round_3_2019 = []
round_4_2019 = []
round_5_2019 = []
round_6_2019 = []
round1_2020_CSAB = []
round2_2020_CSAB = []
round_2018_provisonal = []
round_2019_provisonal = []
round_2020_provisonal = []
seats_2020 = []
seats_2019 = []
seats_2021 = []
seats_2021I = []
seats_CSAB = []
cb = []
cc = []
round_1_2021 = []
round_2_2021 = []
round_3_2021 = []
round_4_2021 = []
round_5_2021 = []
round_6_2021 = []

lists = {
    '_2015': round_2015,
    '1_2016': round_1_2016,
    '6_2016': round_6_2016,
    '1_2017': round_1_2017,
    '7_2017': round_7_2017,
    '1_2018': round_1_2018,
    '7_2018': round_7_2018,
    '1_2019': round_1_2019,
    '7_2019': round_7_2019,
    '1_2020': round_1_2020,
    '2_2020': round_2_2020,
    '3_2020': round_3_2020,
    '4_2020': round_4_2020,
    '5_2020': round_5_2020,
    '6_2020': round_6_2020,
    '2_2016': round_2_2016,
    '3_2016': round_3_2016,
    '4_2016': round_4_2016,
    '5_2016': round_5_2016,
    '2_2017': round_2_2017,
    '3_2017': round_3_2017,
    '4_2017': round_4_2017,
    '5_2017': round_5_2017,
    '6_2017': round_6_2017,
    '2_2018': round_2_2018,
    '3_2018': round_3_2018,
    '4_2018': round_4_2018,
    '5_2018': round_5_2018,
    '6_2018': round_6_2018,
    '2_2019': round_2_2019,
    '3_2019': round_3_2019,
    '4_2019': round_4_2019,
    '5_2019': round_5_2019,
    '6_2019': round_6_2019,
    '2020_1': round1_2020_CSAB,
    '2020_2': round2_2020_CSAB,
    'sional_2018': round_2018_provisonal,
    'sional_2019': round_2019_provisonal,
    'sional_2020': round_2020_provisonal,
    'atrix_2020': seats_2020,
    'atrix_2019': seats_2019,
    'atrix_2021': seats_2021,
    'atrix_2021i': seats_2021I,
    'atrix_2020_csab': seats_CSAB,
    'college_branch': cb,
    'college_category': cc,
    '1_2021': round_1_2021,
    '2_2021': round_2_2021,
    '3_2021': round_3_2021,
    '4_2021': round_4_2021,
    '5_2021': round_5_2021,
    '6_2021': round_6_2020,
}


viewset_url = ['branches', 'institutes', '1_2016', '1_2017', '1_2018', '1_2019', '1_2020', '2_2020',
               '3_2020', '4_2020', '5_2020', '6_2016', '6_2020', '7_2017', '7_2018', '7_2019', '7_2015', 'provisional_2018', 'provisional_2019', 'provisional_2020', '1_csab_2020', '2_csab_2020', 'seat_2019', 'seat_2020', 'seat_csab_2020', '2_2016', '3_2016', '4_2016', '5_2016', '2_2017', '2_2018', '2_2019', '3_2017', '3_2018', '3_2019', '4_2017', '4_2018', '4_2019', '5_2017', '5_2018', '5_2019', '6_2017', '6_2018', '6_2019',  'update', 'college_branch', 'seat_2021', 'seat_2021I', 'college_category', '1_2021', '2_2021', '3_2021', '4_2021', '5_2021', '6_2021']
