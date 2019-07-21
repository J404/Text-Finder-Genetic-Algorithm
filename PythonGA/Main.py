from Population import Population

target = "test phrase" 
pop = Population(1000, target)
while pop.pop[pop.best_ind].brain.guess != target:
    pop.calculate_fitness()
    pop.natural_selection()
    pop.mutate_babies()
    pop.show_best()
    pop.cull()
