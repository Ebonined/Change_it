# Change_it

A little function that can change NaN values in any index column in a pandas.DataFrame object

## Description

    Runs a function`func` on every column specified in the index `strindex`

## Parameters

### frame

    Dataframecolumns : list, tuple, ndarray, str(e.g. for Dataframe.iloc; '0:1' and for Dataframe.loc; 'column1:column2').

### strindex

    bool, specify whether `True` for df.iloc or `False` for df.loc.

### func

    function:function to run on each column.

### inplace

    bool,select to change the initial datafram or return a new one with the previous unchanged.

## return

    DataFrame.head() when inplace = False
