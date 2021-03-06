def get_all_champions() -> list:
    return ['/annie', '/olaf', '/galio', '/twistedfate', '/xinzhao', '/urgot', '/leblanc', '/vladimir', '/fiddlesticks',
            '/kayle', '/masteryi', '/alistar', '/ryze', '/sion', '/sivir', '/soraka', '/teemo', '/tristana', '/warwick',
            '/nunuwillump', '/missfortune', '/ashe', '/tryndamere', '/jax', '/morgana', '/zilean', '/singed',
            '/evelynn', '/twitch', '/karthus', '/chogath', '/amumu', '/rammus', '/anivia', '/shaco', '/drmundo',
            '/sona', '/kassadin', '/irelia', '/janna', '/gangplank', '/corki', '/karma', '/taric', '/veigar',
            '/trundle', '/swain', '/caitlyn', '/blitzcrank', '/malphite', '/katarina', '/nocturne', '/maokai',
            '/renekton', '/jarvaniv', '/elise', '/orianna', '/wukong', '/brand', '/leesin', '/vayne', '/rumble',
            '/cassiopeia', '/skarner', '/heimerdinger', '/nasus', '/nidalee', '/udyr', '/poppy', '/gragas', '/pantheon',
            '/ezreal', '/mordekaiser', '/yorick', '/akali', '/kennen', '/garen', '/leona', '/malzahar', '/talon',
            '/riven', '/kogmaw', '/shen', '/lux', '/xerath', '/shyvana', '/ahri', '/graves', '/fizz', '/volibear',
            '/rengar', '/varus', '/nautilus', '/viktor', '/sejuani', '/fiora', '/ziggs', '/lulu', '/draven', '/hecarim',
            '/khazix', '/darius', '/jayce', '/lissandra', '/diana', '/quinn', '/syndra', '/aurelionsol', '/kayn',
            '/zoe', '/zyra', '/kaisa', '/gnar', '/zac', '/yasuo', '/velkoz', '/taliyah', '/camille', '/braum', '/jhin',
            '/kindred', '/jinx', '/tahmkench', '/lucian', '/zed', '/kled', '/ekko', '/vi', '/aatrox', '/nami', '/azir',
            '/thresh', '/illaoi', '/reksai', '/ivern', '/kalista', '/bard', '/rakan', '/xayah', '/ornn', '/pyke', ]


def only_numerics(seq: str) -> int:
    seq_type = type(seq)
    return int(seq_type().join(filter(seq_type.isdigit, seq)))
