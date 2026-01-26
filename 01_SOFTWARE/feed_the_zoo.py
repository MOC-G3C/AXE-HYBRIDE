{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # MOC-G3C : Entropy Injection Script\
# Location: Beloeil Node | Target: Zoo Stability\
\
bio_mass = 1336528 # Tes points de vie actuels\
stability = -0.0432 # Score Landau\
\
def calculate_zoo_health(mass, gamma):\
    # Plus la masse est haute, plus le zoo est riche\
    energy = mass * abs(gamma)\
    return f"\'c9NERGIE DU ZOO : \{energy:.2f\} Joules Entropiques"\
\
print("--- INITIALISATION DU ZOO ---")\
print(calculate_zoo_health(bio_mass, stability))\
print("STATUT : ANIMAL NOURRI PAR LA BIOLOGIE DU M.O.C.")}