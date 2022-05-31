import discord
import json


def url_memes():
    return ['https://images7.memedroid.com/images/UPLOADED765/5fb2d2c623aca.jpeg',
            'https://images7.memedroid.com/images/UPLOADED723/5fb2df83ee5b6.jpeg',
            'https://images7.memedroid.com/images/UPLOADED987/5fb2f6ea7b451.jpeg',
            'https://images3.memedroid.com/images/UPLOADED495/5fb3b32f94dbc.jpeg',
            'https://images3.memedroid.com/images/UPLOADED363/5fb3187e5124d.jpeg',
            'https://images7.memedroid.com/images/UPLOADED400/5fb3f72a7a677.jpeg',
            'https://images7.memedroid.com/images/UPLOADED829/5fb2e6e78d797.jpeg',
            'https://images7.memedroid.com/images/UPLOADED753/5f4931a8de2ad.jpeg',
            'https://images7.memedroid.com/images/UPLOADED974/5f4930a2e0d95.jpeg',
            'https://images7.memedroid.com/images/UPLOADED782/5f11ece537144.jpeg',
            'https://images7.memedroid.com/images/UPLOADED722/5ecb562c6d8b2.jpeg',
            'https://images3.memedroid.com/images/UPLOADED372/5ec6930b2fa93.jpeg',
            'https://images7.memedroid.com/images/UPLOADED482/5ec5d2e354266.jpeg',
            'https://images3.memedroid.com/images/UPLOADED193/5e9e4ea4eddfe.jpeg',
            'https://images3.memedroid.com/images/UPLOADED253/5aef3ab39268d.jpeg',
            'https://images7.memedroid.com/images/UPLOADED606/5fb2f1feb077a.jpeg',
            'https://images3.memedroid.com/images/UPLOADED339/5fb32f00e542a.jpeg',
            'https://images7.memedroid.com/images/UPLOADED912/5fb2d8a793ad0.jpeg',
            'https://images7.memedroid.com/images/UPLOADED721/5fb41261828c3.jpeg',
            'https://images7.memedroid.com/images/UPLOADED680/5fb3dcc5b9705.jpeg',
            'https://images7.memedroid.com/images/UPLOADED972/5fb3e486dc5dd.jpeg',
            'https://images3.memedroid.com/images/UPLOADED352/5d6736ac12768.jpeg',
            'https://images7.memedroid.com/images/UPLOADED739/591ba25e9a7f9.jpeg',
            'https://images7.memedroid.com/images/UPLOADED665/5d843fdb92587.jpeg',
            'https://images3.memedroid.com/images/UPLOADED352/5d840ee24c068.jpeg',
            'https://images7.memedroid.com/images/UPLOADED919/5d83ffb060402.jpeg',
            'https://images3.memedroid.com/images/UPLOADED127/5fadcba0e90b0.jpeg',
            'https://images7.memedroid.com/images/UPLOADED792/5fc1c300eb67e.jpeg',
            'https://images3.memedroid.com/images/UPLOADED817/5fbf7d445dea4.jpeg',
            'https://images3.memedroid.com/images/UPLOADED972/5fbffaf01eaca.jpeg',
            'https://images3.memedroid.com/images/UPLOADED436/5ec0b08ab8fc2.jpeg',
            'https://images7.memedroid.com/images/UPLOADED858/5bf15c763ca8b.jpeg',
            'https://images7.memedroid.com/images/UPLOADED526/5fbad79e84f0e.jpeg',
            'https://images7.memedroid.com/images/UPLOADED608/5c6b3347e3150.jpeg',
            'https://images3.memedroid.com/images/UPLOADED271/5f3681c54f58f.jpeg',
            'https://images7.memedroid.com/images/UPLOADED871/5e58277233a3a.jpeg',
            'https://images3.memedroid.com/images/UPLOADED334/5cfa7a036cc76.jpeg',
            'https://images7.memedroid.com/images/UPLOADED658/5fc6bc38dc1f7.jpeg',
            'https://images3.memedroid.com/images/UPLOADED978/5e4342a69c526.jpeg',
            'https://images7.memedroid.com/images/UPLOADED895/5d60745061bf6.jpeg',
            'https://images3.memedroid.com/images/UPLOADED604/5fa9994436dd3.jpeg',
            'https://images3.memedroid.com/images/UPLOADED361/5e8648763fa3d.jpeg',
            'https://images7.memedroid.com/images/UPLOADED608/5c4bb0ed0e0a3.jpeg',
            'https://images7.memedroid.com/images/UPLOADED612/5f6a469b8a75c.jpeg',
            'https://images3.memedroid.com/images/UPLOADED50/5e26c4be3f2d0.jpeg',
            'https://images3.memedroid.com/images/UPLOADED413/5d9e28345d570.jpeg',
            'https://images3.memedroid.com/images/UPLOADED201/5f9fcf7b8c4d6.jpeg',
            'https://images7.memedroid.com/images/UPLOADED380/5f1304016f90b.jpeg',
            'https://images7.memedroid.com/images/UPLOADED984/5e7b8c2bd16df.jpeg',
            'https://images7.memedroid.com/images/UPLOADED921/5c5bea047bfbb.jpeg',
            'https://images7.memedroid.com/images/UPLOADED405/5fbec2e634514.jpeg',
            'https://images7.memedroid.com/images/UPLOADED864/5fc6b28304999.jpeg',
            'https://images3.memedroid.com/images/UPLOADED837/5fc54a03a9faa.jpeg',
            'https://images7.memedroid.com/images/UPLOADED838/5fc0f01aa1e4a.jpeg',
            'https://images7.memedroid.com/images/UPLOADED559/5fc3f9c2345bf.jpeg',
            'https://images7.memedroid.com/images/UPLOADED498/5fc6e29e27fcc.jpeg',
            'https://images7.memedroid.com/images/UPLOADED362/5fc040cb2c3a9.jpeg',
            'https://images3.memedroid.com/images/UPLOADED542/5fc6be32442f8.jpeg',
            'https://images7.memedroid.com/images/UPLOADED786/5fc043b12f411.jpeg',
            'https://images3.memedroid.com/images/UPLOADED996/5fc452822dac6.jpeg',
            'https://images7.memedroid.com/images/UPLOADED635/5fc157a74656d.jpeg',
            'https://images3.memedroid.com/images/UPLOADED556/5fc19e7236eba.jpeg',
            'https://images7.memedroid.com/images/UPLOADED700/5fc6c14d3a50d.jpeg',
            'https://images7.memedroid.com/images/UPLOADED344/5fc11042af875.jpeg',
            'https://images7.memedroid.com/images/UPLOADED441/5fbf6a60411ce.jpeg',
            'https://images3.memedroid.com/images/UPLOADED117/5fc0572801a6f.jpeg',
            'https://images3.memedroid.com/images/UPLOADED738/5fc52aa4d343b.jpeg',
            ]


def cores_disc(tipo='nogrey'):
    """
    retorna uma lista com as cores possíveis para o discord
    :param tipo: 'tudo': (default) retorna a lista com todas as cores, 'regular': retorna uma lista contendo apenas as
    versões regulares das cores. (tudo -dark) e 'dark': retorna uma lista que contém apenas as versões DARK das cores.
    :return: lista contendo as cores
    """
    tipo = tipo.lower()

    regular = [discord.Colour.green(),
               discord.Colour.red(),
               discord.Colour.blue(),
               discord.Colour.blurple(),
               discord.Colour.gold(),
               discord.Colour.magenta(),
               discord.Colour.orange(),
               discord.Colour.purple(),
               discord.Colour.teal(),
               ]

    darkers = [discord.Colour.dark_gold(),
               discord.Colour.dark_purple(),
               discord.Colour.dark_blue(),
               discord.Colour.dark_green(),
               discord.Colour.dark_magenta(),
               discord.Colour.dark_orange(),
               discord.Colour.dark_red(),
               discord.Colour.dark_teal(),
               ]

    greys = [discord.Colour.dark_grey(),
             discord.Colour.dark_theme(),
             discord.Colour.greyple(),
             ]

    if tipo == 'nogrey':
        lista_final = regular + darkers

        return lista_final

    elif tipo == 'tudo':
        lista_final = regular + darkers + greys

        return lista_final

    elif tipo == 'regular':
        return regular

    elif tipo == 'dark':
        return darkers

    else:
        raise SyntaxError


def veros_id() -> int:
    return 246040430494351362


def myguild_id() -> int:
    return 247535193114673163


def fbot_id() -> int:
    return 775495739127889971


# noinspection PyUnusedLocal,PyShadowingNames
def get_prefix(client, message):
    with open('data/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    if type(message) == int:
        guildid = str(message)
    else:
        guildid = str(message.guild.id)

    return prefixes[guildid]


def version_():
    __version__ = '0.7.9.8'

    return __version__
