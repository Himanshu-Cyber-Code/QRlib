from . import _util as ql

def json_custom(name, body=6, frame=5, ball=7, bodycolor=(17, 49, 81), bgcolor=(255, 255, 255), ballcolor=(17, 49, 81), framecolor=(17, 49, 81), shadecolor=(17, 49, 81), shadeonball=True, shadetype=0, logo="", size=200):
    json_data={'body':body, 'frame':frame, 'ball':ball, 'bodycolor':bodycolor, 'bgcolor':bgcolor, 'ballcolor':ballcolor, 'framecolor':framecolor, 'shadecolor':shadecolor, 'shadeonball':shadeonball, 'shadetype':shadetype, 'logo':logo, 'size':size}
    js= ql._str2json(json_data)
    nametemp = (str(name)+'.json')
    json_file = open(nametemp, "w")
    json_file.write(str(js))
    json_file.close()
