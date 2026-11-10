def golpear(atacante, defensor):
    dano = 1
    defensor.stats["current_hp"] -= dano
    print(f"{defensor.name} levou {dano} de dano!")

weapons = {

}

armors = {

}

moves = {
    "Golpear": golpear
}