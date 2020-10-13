#!/usr/bin/python
# -*- coding: latin-1 -*-


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows',200)
import argparse
import math

def parsefilename(all_data):
    all_data['rootfilename'] = {}
    for i in range(len(all_data['args'].csvfilename)):
        filename = all_data['args'].csvfilename[i]
        filename = filename.split('/')[-1]
        filename = filename[:-4]
        all_data['rootfilename'][i] = filename
        splitname = filename.split('_')

        k = 0
        while k<len(splitname)-1:
            all_data[splitname[k]] = splitname[k+1]
            k += 2

    return all_data


def makeplot(all_data,i):
    db = all_data['db'][i]
    
    fig = plt.figure(tight_layout=True,figsize=(12,8))

    plt.subplot(2, 2, 1)
    x0 = db.loc[:,'CAPS - Pertinence (NB) pct'].to_numpy()
    y0 = db.loc[:,'CAPS - Taux detection (recall) fraude (NB) pct'].to_numpy()
    x1 = db.loc[:,'CAPS + MAURO - Pertinence (NB) pct'].to_numpy()
    y1 = db.loc[:,'CAPS + MAURO - Taux detection (recall) fraude (NB) pct'].to_numpy()
    x0,y0 = x0[~pd.isnull(x0)],y0[~pd.isnull(x0)]
    x1,y1 = x1[~pd.isnull(x1)],y1[~pd.isnull(x1)]
    idx0 = [i for i, x in enumerate(x0[:-1]-x0[1:]>0) if x]
    if len(idx0)>0 and x0[idx0[-1]+1]==0:
        x0,y0 = x0[:idx0[-1]+1],y0[:idx0[-1]+1]
    idx0 = [i for i, x in enumerate(x1[:-1]-x1[1:]>0) if x]
    if len(idx0)>0 and x1[idx0[-1]+1]==0:
        x1,y1 = x1[:idx0[-1]+1],y1[:idx0[-1]+1]
    if all_data['args'].revert_axes:
        plt.plot(x0,y0)
        plt.plot(x1,y1)
        plt.ylabel('Taux detection (recall) fraude (NB) pct')
        plt.xlabel('Pertinence')
    else:
        plt.plot(y0,x0)
        plt.plot(y1,x1)
        plt.xlabel('Taux detection (recall) fraude (NB) pct')
        plt.ylabel('Pertinence')
    plt.legend(['Indicateurs CAPS','Indicateurs CAPS + LIX'])

    plt.subplot(2, 2, 2)
    x0 = db.loc[:,'CAPS - Pertinence (MT) pct'].to_numpy()
    y0 = db.loc[:,'CAPS - Taux detection (recall) fraude (MT) pct'].to_numpy()
    x1 = db.loc[:,'CAPS + MAURO - Pertinence (MT) pct'].to_numpy()
    y1 = db.loc[:,'CAPS + MAURO - Taux detection (recall) fraude (MT) pct'].to_numpy()
    x0,y0 = x0[~pd.isnull(x0)],y0[~pd.isnull(x0)]
    x1,y1 = x1[~pd.isnull(x1)],y1[~pd.isnull(x1)]
    idx0 = [i for i, x in enumerate(x0[:-1]-x0[1:]>0) if x]
    if len(idx0)>0 and x0[idx0[-1]+1]==0:
        x0,y0 = x0[:idx0[-1]+1],y0[:idx0[-1]+1]
    idx0 = [i for i, x in enumerate(x1[:-1]-x1[1:]>0) if x]
    if len(idx0)>0 and x1[idx0[-1]+1]==0:
        x1,y1 = x1[:idx0[-1]+1],y1[:idx0[-1]+1]
    if all_data['args'].revert_axes:
        plt.plot(x0,y0)
        plt.plot(x1,y1)
        plt.ylabel('Taux detection (recall) fraude (MT) pct')
        plt.xlabel('Pertinence')
    else:
        plt.plot(y0,x0)
        plt.plot(y1,x1)
        plt.xlabel('Taux detection (recall) fraude (MT) pct')
        plt.ylabel('Pertinence')
    plt.legend(['Indicateurs CAPS','Indicateurs CAPS + LIX'])
    
    plt.subplot(2, 2, 3)
    x0 = db.loc[:,'CAPS - Pertinence (NB) pct'].to_numpy()
    y0 = db.loc[:,'CAPS - Taux detection (recall) TF (NB) pct'].to_numpy()
    x1 = db.loc[:,'CAPS + MAURO - Pertinence (NB) pct'].to_numpy()
    y1 = db.loc[:,'CAPS + MAURO - Taux detection (recall) TF (NB) pct'].to_numpy()
    x0,y0 = x0[~pd.isnull(x0)],y0[~pd.isnull(x0)]
    x1,y1 = x1[~pd.isnull(x1)],y1[~pd.isnull(x1)]
    idx0 = [i for i, x in enumerate(x0[:-1]-x0[1:]>0) if x]
    if len(idx0)>0 and x0[idx0[-1]+1]==0:
        x0,y0 = x0[:idx0[-1]+1],y0[:idx0[-1]+1]
    idx0 = [i for i, x in enumerate(x1[:-1]-x1[1:]>0) if x]
    if len(idx0)>0 and x1[idx0[-1]+1]==0:
        x1,y1 = x1[:idx0[-1]+1],y1[:idx0[-1]+1]
    if all_data['args'].revert_axes:
        plt.plot(x0,y0)
        plt.plot(x1,y1)
        plt.ylabel('Taux detection (recall) TF (NB) pct')
        plt.xlabel('Pertinence')
    else:
        plt.plot(y0,x0)
        plt.plot(y1,x1)
        plt.xlabel('Taux detection (recall) TF (NB) pct')
        plt.ylabel('Pertinence')
    plt.legend(['Indicateurs CAPS','Indicateurs CAPS + LIX'])

    plt.subplot(2, 2, 4)
    x0 = db.loc[:,'CAPS - Pertinence (MT) pct'].to_numpy()
    y0 = db.loc[:,'CAPS - Taux detection (recall) TF (MT) pct'].to_numpy()
    x1 = db.loc[:,'CAPS + MAURO - Pertinence (MT) pct'].to_numpy()
    y1 = db.loc[:,'CAPS + MAURO - Taux detection (recall) TF (MT) pct'].to_numpy()
    x0,y0 = x0[~pd.isnull(x0)],y0[~pd.isnull(x0)]
    x1,y1 = x1[~pd.isnull(x1)],y1[~pd.isnull(x1)]
    idx0 = [i for i, x in enumerate(x0[:-1]-x0[1:]>0) if x]
    if len(idx0)>0 and x0[idx0[-1]+1]==0:
        x0,y0 = x0[:idx0[-1]+1],y0[:idx0[-1]+1]
    idx0 = [i for i, x in enumerate(x1[:-1]-x1[1:]>0) if x]
    if len(idx0)>0 and x1[idx0[-1]+1]==0:
        x1,y1 = x1[:idx0[-1]+1],y1[:idx0[-1]+1]
    if all_data['args'].revert_axes:
        plt.plot(x0,y0)
        plt.plot(x1,y1)
        plt.ylabel('Taux detection (recall) TF (MT) pct')
        plt.xlabel('Pertinence')
    else:
        plt.plot(y0,x0)
        plt.plot(y1,x1)
        plt.xlabel('Taux detection (recall) TF (MT) pct')
        plt.ylabel('Pertinence')
    plt.legend(['Indicateurs CAPS','Indicateurs CAPS + LIX'])

    print('saving '+all_data['rootfilename'][i]+'.png')
    fig.savefig(all_data['rootfilename'][i]+'.png')
    plt.close()
    
if __name__ == '__main__':

    all_data = {}
    parser = argparse.ArgumentParser(description='Plots curves from RF',\
                                     formatter_class=argparse.RawTextHelpFormatter)

    menu = parser.add_argument_group('Menu Options')
    menu.add_argument('-d','--data',dest='csvfilename',nargs='+',required=True,\
                     help='reads the database in CSVFILENAME files (it can be a list of files)')
    menu.add_argument('--revert-axes',dest='revert_axes',action='store_true')
    args = parser.parse_args()
    all_data['args'] = args

    all_data = parsefilename(all_data)    

    all_data['db'] = {}
    for i in range(len(args.csvfilename)):
        all_data['db'][i] = pd.read_csv(args.csvfilename[i])
        makeplot(all_data,i)
