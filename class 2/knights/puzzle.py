from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Implication(AKnight,And(AKnight,AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Implication(AKnight,And(AKnave,BKnave)),
    Implication(AKnave,Not(And(AKnave,BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),

    Implication(AKnight,Biconditional(AKnight,BKnight)),
    Implication(AKnave,Not(Biconditional(AKnight,BKnight))),
    
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),  # 如果 B 是骑士，A 和 B 的身份不同
    Implication(BKnave, Biconditional(AKnight, BKnight)) 
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave)),

    # A 的陈述
    Implication(AKnight, Or(AKnight, AKnave)),  # 如果 A 是骑士，则 A 的话为真
    Implication(AKnave, Not(Or(AKnight, AKnave))),  # 如果 A 是无赖，则 A 的话为假

    # B 的陈述
    Implication(BKnight, AKnave),  # 如果 B 是骑士，则 A 是无赖
    Implication(BKnight, CKnave),  # 如果 B 是骑士，则 C 是无赖
    Implication(BKnave, Not(CKnave)), # 如果 B 是无赖，则 C 不是无赖
    Implication(BKnave, Not(AKnave)), # 如果 B 是无赖，则 A 不是无赖

    # C 的陈述
    Implication(CKnight, AKnight),  # 如果 C 是骑士，则 A 是骑士
    Implication(CKnave, Not(AKnight))  # 如果 C 是无赖，则 A 不是骑士
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
