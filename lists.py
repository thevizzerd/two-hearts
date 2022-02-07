# Create lists for iteration

list_str = ['01','02','03','04','05','06','07','08','09'] + list(map(str, range(10, 71)))

list_datafiles_raw = 'sample-data/raw/00{list_str}'
list_datafiles = 'sample-data/00{list_str}'

datafiles_wfdb = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_raw.format(list_str = list_str[i])
    datafiles_wfdb.append(datafiles_str)

datafiles_raw = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_raw.format(list_str = list_str[i])
    datafiles_raw.append(datafiles_str)
append_str = '.npy'
datafiles_raw = [sub + append_str for sub in datafiles_raw]

datafiles = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles.format(list_str = list_str[i])
    datafiles.append(datafiles_str)
append_str = '.npy'
datafiles = [sub + append_str for sub in datafiles]

append_str = 'drive/MyDrive/Masterarbeit/Code/two-hearts/'
datafiles_raw_google = [append_str + sub for sub in datafiles_raw]
datafiles_google = [append_str + sub for sub in datafiles]
