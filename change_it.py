def change_it(frame, columns=None, strindex=True, func=None, inplace=True):
    """
    Runs a function`func` on every column specified in the index `strindex`
    
    Parameters
    ----------
    frame : Dataframe
    columns : list, tuple, ndarray, str(e.g. for Dataframe.iloc; '0:1' and for Dataframe.loc; 'column1:column2').
    strindex : bool, 
        specify whether `True` for df.iloc or `False` for df.loc.
    func: function:
        function to run on each column.
    inplace: bool,
        select to change the initial datafram or return a new one with the previous unchanged.
        
        
    return
    ------
    DataFrame.head() when inplace = False
    """
    import pandas as pd
    import numpy as np
    import re
    
    if inplace == False:
        frame1 = pd.DataFrame()
        frame = frame1.append(frame)
            
    # check for instance of 'str'
    if isinstance(columns,str):
        
        # check for ':' in string
        if ':' in columns:
            # pattern for regular expression
            pattern = r'\s*\:\s*'
            # change columns to an index in tuple form: colindex
            colindex = re.split(pattern, columns)
            
            # check if the is an end of range
            if len(colindex[1]) == 0:
                colindex.pop(1)
            
            # Make index of either .iloc or .loc 
            if strindex == False:
                no_1 = int(colindex[0])
                if len(colindex) == 2:
                    no_2 = int(colindex[1])
                    columns = frame.iloc[:,no_1:no_2].columns
                else:
                    columns = list(frame.iloc[:,no_1:].columns)
            else:
                no_1 = (colindex[0])
                if len(colindex) == 2:
                    no_2 = (colindex[1])
                    columns = list(frame.loc[:,no_1:no_2].columns)
                else:
                    columns = list(frame.loc[:,no_1:].columns)
                    
        # is no ':' convert columns to list
        else: 
            columns = [columns,]
        
    # Run for loop for all the listed columns
    for col in columns:
        # check for func
        if func:
            fill = func(frame[col])
            frame.loc[:,col] = frame[col].fillna(fill) 
        else:
            frame.loc[:,col] = frame[col].fillna(np.nan)
    if inplace == False:
        return frame
