global traders
global grades
global terms
global countries
global match


globals()['traders'] = ['Ilya','Juan','Nick','Gonzalo']

globals()['grades'] = ['DKL','OCC','SWL','SOP']

globals()['terms'] = ['FAS','FCA','EXW']

globals()['countries'] = ['CR','PR','Colombia']

globals()['match'] = {
    'Juan': {
        'C':['DR','PR','Belize','Cuba', 'El Salvador', 'Guatemala', 'Haiti', 'Honduras', 'Mexico', 'Bolivia'],
        'G':['OCC', 'DKL', 'SWL', 'SOP', 'PET'],
    },
    'Nick': {
        'C': ['Puerto Rico', 'Ecuador','Mexico','Chile','Paraguay','Colombia'],
        'G': ['OCC', 'DKL', 'SWL', 'SOP'],
    },
    'Yuri': {
        'C': ['Puerto Rico', 'Ecuador', 'Mexico', 'Chile', 'Paraguay', 'Colombia'],
        'G': ['OCC', 'DKL', 'SWL', 'SOP'],
    },
    'Gonzalo': {
        'C': ['Colombia', 'Ecuador', 'Peru', 'CR', 'Mexico', 'DR', 'Guatemala'\
              'Honduras', 'Panama', 'Colombia'],
        'G': ['OCC', 'DKL', 'SWL', 'SOP'],
    },
    'Ilya': {
        'C': ['CR', 'PR'],
        'G': ['OCC', 'DKL'],
    }
}