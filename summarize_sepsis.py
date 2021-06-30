#!/usr/bin/python

import pandas

# set `exporter.csv.export = true` in src/main/resources/synthea.properties, then generate data

# DATE,PATIENT,ENCOUNTER,CATEGORY,CODE,DESCRIPTION,VALUE,UNITS,TYPE
csv_path = './output/csv/observations.csv'

DESCRIPTION_COL = 'DESCRIPTION'
PATIENT_COL = 'PATIENT'
VALUE_COL = 'VALUE'

PATIENT_ID_FIELD = 'PATIENT_ID'
HQ_PROVIDER_FIELD = 'HQ_PROVIDER'
DO_ENHANCED_FIELD = 'DO_ENHANCED'
FLUID_RESPONSIVE_FIELD = 'FLUID_RESPONSIVE'
DEATH_FIELD = 'DIED'

HQ_PROVIDER_DESC = 'Debug: HQ_PROVIDER'
DO_ENHANCED_DESC = 'Debug: DO_ENHANCED'
FLUID_RESPONSIVE_DESC = 'Debug: FLUID_RESPONSIVE'
DEATH_DESC = 'Debug: Death'

FIELD_MAPPING = {
    HQ_PROVIDER_FIELD: HQ_PROVIDER_DESC,
    DO_ENHANCED_FIELD: DO_ENHANCED_DESC,
    FLUID_RESPONSIVE_FIELD: FLUID_RESPONSIVE_DESC,
    DEATH_FIELD: DEATH_DESC
}

PRINT_FIELD_ORDER = [PATIENT_ID_FIELD, HQ_PROVIDER_FIELD, DO_ENHANCED_FIELD, FLUID_RESPONSIVE_FIELD, DEATH_FIELD]

def main():
    df = pandas.read_csv(csv_path)
    subset = df.loc[df[DESCRIPTION_COL].str.contains('Debug')]
    
    print(','.join(PRINT_FIELD_ORDER))
    for patient_id in subset[PATIENT_COL].unique():
        data = {}
        data[PATIENT_ID_FIELD] = patient_id
        patient_subset = subset[patient_id == subset[PATIENT_COL]]
        
        for key in FIELD_MAPPING:
            col = FIELD_MAPPING[key]
            val = patient_subset[patient_subset[DESCRIPTION_COL] == col][VALUE_COL].values[0]
            data[key] = val
            
        row = []
        for key in PRINT_FIELD_ORDER:
            row.append(data[key])
        print(','.join(row))

if __name__ == '__main__':
    main()
    