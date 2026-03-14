RENAME_COLS = {
    "AÑO": "year",
    "MES": "month",
    "NACION_01": "country",
    "REGION_01": "region",
    "PASO_02": "crossing_type",
    "PASO_01": "crossing_detail",
    "SumaDeTTAS": "arrivals",
}

MONTH_MAP = {
    "ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
    "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12,
}

OUTPUT_COLS = ["period", "region", "country", "crossing_type", "crossing_detail", "arrivals"]

CROSSING_NORMALIZE = {
    "Aeropuerto C. Arturo Merino Benítez": "Aeropuerto Comodoro Arturo Merino Benítez",
    "Los Libertadores": "Sistema Cristo Redentor (Los Libertadores)",
    "Coyhaique Alto": "Coyhaique",
    "Monte Aymond": "Integración Austral (Monte Aymond)",
    "Casas Viejas": "Laurita Casas Viejas",
    "El Límite - Futaleufu": "Futaleufú",
    "Peulla": "Pérez Rosales (Peulla)",
    "Jeinimeni": "Rio Jeinimeni",
    "Río Encuentro - Palena": "Río Encuentro",
    "La Mina - Pehuenche": "Pehuenche",
    "Portezuelo Socompa": "Socompa",
    "Isla de Pascua - Aeropuerto": "Aeropuerto Isla de Pascua",
    "Chacalluta - Aeropuerto": "Concordia (Chacalluta)",
    "FF.CC Ollague": "Salar de Ollagüe",
    "Ollague terrestre": "Salar de Ollagüe",
    "Paso Lama": "Pascua Lama",
    "FF.CC. Arica - Tacna": "Ferrocarril Arica - Tacna",
}