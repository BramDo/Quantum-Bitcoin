# Quantum-Bitcoin
Coin Flipping Leader election for use in Quantum Bitcoin application
Bitcoin runs a leader election algoritm to elect the next node to add a block to the blockchain. Quantum leader election is a natural extension of the coin flipping problem to n nodes: arXiv:0910.4952v2.
Start with two parties or nodes Alice and Bob share a Bell state or EPR pair. Without normalisation factor we want the state 
01> +10> First qubit is A and second qubit is Botb, so both nodes have 50% chance of winning.
Next Alice Bob invite Charlie to join the game and they agree that Charlie starts with a chance 1/3 to give him a fair chance.

P(Alice)= 1/2*2/3 = 1/3

P(Bob)  = 1/2*2/3 =1/3

P(Charlie) = 1/3

All chances are equal.
We can make Bell state with H and Cnote gate, but we want to reuse the same circuit for all nodes or parties.
So we start with 00 state -> ROTy (a|0>  + b|1>)0>
After Cnot                -> CNOT  a|00> + b|11>
X gate                    -> X     a|01> + b|10>

