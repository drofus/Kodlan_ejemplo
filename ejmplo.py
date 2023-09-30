meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
            }

x = input('Que palabra te gustaría conocer?:')

if x in meme_dict.keys():
    print(meme_dict[x])
else:
    print('no tenemos esa palabra aún...estamos trabajando en ello')
