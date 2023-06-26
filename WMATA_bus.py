{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier-Bold;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red25\green25\blue25;\red0\green0\blue0;\red255\green255\blue255;
\red25\green25\blue25;}
{\*\expandedcolortbl;;\cssrgb\c12941\c12941\c12941;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000;
\cssrgb\c12941\c12941\c12941;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl325\partightenfactor0

\f0\b\fs26 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import
\f1\b0  requests\

\f0\b import
\f1\b0  pandas 
\f0\b as
\f1\b0  pd\

\f0\b import
\f1\b0  json\
\pard\pardeftab720\sl325\partightenfactor0

\f0\b\fs28 \cf3 \cb4 \strokec3 \
\pard\pardeftab720\sl325\partightenfactor0

\f1\b0\fs26 \cf5 \cb1 \outl0\strokewidth0 bus_stop 
\f0\b =
\f1\b0  '1002241'
\f0\b\fs28 \cf3 \cb4 \outl0\strokewidth0 \strokec3 \
\pard\pardeftab720\sl325\partightenfactor0
\cf3 \
def
\f1\b0  get_busTimes(bust_stop):\
    URL 
\f0\b =
\f1\b0  'https://api.wmata.com/NextBusService.svc/json/jPredictions?StopID=\{\}&api_key=fe14e29e73c3466f9aba8eee3c6e508a'
\f0\b .
\f1\b0 replace('\{\}',bus_stop)\
    data 
\f0\b =
\f1\b0  json
\f0\b .
\f1\b0 loads(requests
\f0\b .
\f1\b0 get(URL)
\f0\b .
\f1\b0 text)\
    df 
\f0\b =
\f1\b0  pd
\f0\b .
\f1\b0 json_normalize(data,record_path 
\f0\b =
\f1\b0 ['Predictions'])\
\
    stop 
\f0\b =
\f1\b0  df
\f0\b .
\f1\b0 drop(columns
\f0\b =
\f1\b0 ['DirectionNum','VehicleID','TripID'])\
    \
    
\f0\b return
\f1\b0  stop\
\pard\pardeftab720\sl325\partightenfactor0

\fs26 \cf2 \cb1 \strokec2 \
\pard\pardeftab720\sl325\partightenfactor0

\fs28 \cf3 \cb4 \strokec3 get_busTimes(bus_stop)\cb1 \
}