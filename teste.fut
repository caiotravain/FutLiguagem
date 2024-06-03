TEAM oi
oi.AddPlayer(Alisson SKILL 10)
oi.Alisson.SKILL
oi.AddPlayer(Thiago SKILL 90)
TEAM caio
caio.AddPlayer(OI SKILL 90)
caio.OI.SKILL = 90
PRINT TEAM oi
PRINT PLAYER oi.Alisson

MATCH oi VS caio {
    if (oi.Alisson.SKILL > caio.OI.SKILL){
        caio.OI.SKILL = caio.OI.SKILL - 10
        PRINT TEAM caio
    }
    if (oi.Alisson.SKILL + 20 > caio.OI.SKILL){
        MATCHTIME(20)
        ENDMATCH     
    }
    caio.OI.SKILL = caio.OI.SKILL + 10
    PRINT PLAYER oi.Alisson
    MATCHTIME(MATCHTIME + 10)
    PRINT TEAM caio
}

