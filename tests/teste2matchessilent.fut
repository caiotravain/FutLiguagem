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

}s
caio.AddPlayer(OI SKILL 90)

TEAM alpha
alpha.AddPlayer(James SKILL 30)
alpha.AddPlayer(Lucas SKILL 70)
PRINT TEAM alpha

TEAM beta
beta.AddPlayer(Ethan SKILL 60)
beta.AddPlayer(Noah SKILL 80)
PRINT TEAM beta

PRINT PLAYER alpha.James
PRINT PLAYER beta.Ethan

MATCH alpha VS beta {
    if (alpha.James.SKILL == 50) {
        alpha.Lucas REDCARD
    }
    if (alpha.James.SKILL > beta.Ethan.SKILL) {
        beta.Ethan.SKILL = beta.Ethan.SKILL - 15
        PRINT TEAM beta
    }
    if (alpha.James.SKILL + 15 < beta.Ethan.SKILL) {
        beta.Ethan SCORES
        MATCHTIME(MATCHTIME + 5)
        alpha.James PASSES
    }
    alpha.James.SKILL = alpha.James.SKILL + 20
    beta.Ethan.SKILL = beta.Ethan.SKILL + 5
    PRINT PLAYER alpha.James
    MATCHTIME(MATCHTIME + 10)
    if (alpha.James.SKILL > 70) {
        PRINT TEAM alpha
        alpha.James SHOOTS
        alpha.James SCORES
    }
    beta.Ethan SHOOTS
}

beta.AddPlayer(Oscar SKILL 75)
PRINT TEAM beta
