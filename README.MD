# AI House of Commons
A multi-agent AI system designed to enhance response quality and reduce hallucinations through structured inter-model debate.

## Structure 

The architecture is modeled after the **Westminster system of the British Parliament**, using adversarial parliamentary mechanics to govern how agents propose, scrutinize, and pass a final response. Rather than relying on an unstructured group chat, agents are assigned formal constitutional roles with strict speaking rights and responsibilities.

## Adding Invividuals to parliment 
To add another member to the House, you must take the following actions:

- Create a unique 3-character ID.

- Write their personal prompt.

- Adjust the other individuals' prompts to make them aware of the new member.

- Add them to the elif chain of possible next speakers.