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
MATCH oi VS caio{oi.Alisson SCORES
    if (oi.Alisson.SKILL > caio.OI.SKILL){
        caio.OI.SKILL = caio.OI.SKILL - 10
        PRINT TEAM caio
    }
    if (oi.Alisson.SKILL + 20 < caio.OI.SKILL){
        caio.OI SCORES
        MATCHTIME(20)
        ENDMATCH     }
    caio.OI.SKILL = caio.OI.SKILL + 10
    ENDMATCH
    PRINT PLAYER oi.Alisson
    MATCHTIME(20)
    PRINT TEAM caio
    REDCARD oi.Alisson}

MATCH oi VS caio{
    BALLCONTROL TRUE
    oi.Alisson SCORES
    if (oi.Alisson.SKILL > caio.OI.SKILL){
        caio.OI.SKILL = caio.OI.SKILL - 10 + 20
        PRINT TEAM caio
    }
    if (oi.Alisson.SKILL + 20 < caio.OI.SKILL){caio.OI SCORES
        MATCHTIME(20)
        ENDMATCH
        
    }

    ENDMATCH
    PRINT PLAYER oi.Alisson
    MATCHTIME(20)
    PRINT TEAM caio
    
}
caio.AddPlayer(OI SKILL 90)
