TEAM oi
oi.AddPlayer(Alisson SKILL 10)
oi.Alisson.SKILL
oi.AddPlayer(Thiago SKILL 90)
TEAM caio
caio.AddPlayer(OI SKILL 90)
caio.OI.SKILL = 90 + oi.Alisson.SKILL * 2
PRINT TEAM oi
PRINT TEAM caio
PRINT PLAYER oi.Alisson
MATCH oi VS caio{
    oi.Alisson SCORES
    if (oi.Alisson.SKILL == 10){
       oi.Thiago REDCARD
    }
    if (oi.Alisson.SKILL > caio.OI.SKILL){
        caio.OI.SKILL = caio.OI.SKILL - 10
        PRINT TEAM caio
    }
    if (oi.Alisson.SKILL + 20 < caio.OI.SKILL){
        caio.OI SCORES
        MATCHTIME(MATCHTIME + 5)
        oi.Alisson PASSES
    }
    oi.Alisson.SKILL = oi.Alisson.SKILL + 10
    caio.OI.SKILL = caio.OI.SKILL + 10
    PRINT PLAYER oi.Alisson
    MATCHTIME(MATCHTIME + 10)
    if (oi.Alisson.SKILL > 60){
        PRINT TEAM oi
        oi.Alisson SHOOTS
        oi.Alisson SCORES
        oi.Alisson REDCARD
    }
    caio.OI SHOOTS

}
caio.AddPlayer(OI SKILL 90)
