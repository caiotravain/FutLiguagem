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
