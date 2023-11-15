## cd-tuner_negpip-ComfyUI

<b> This custom node implements ComfyUI the following two webUI extensions by hako-mikan .

https://github.com/hako-mikan/sd-webui-cd-tuner : 

Function to adjust color tone and writing amount, only some functions are implemented for now...<br> 

https://github.com/hako-mikan/sd-webui-negpip : 

Ability to implement negative weight for prompts explanation<br>

This extension enhances the stable diffusion web-ui prompts and cross-attention, allowing for the use of prompts with negative effects within regular prompts and prompts with positive effects within negative prompts. Typically, unwanted elements are placed in negative prompts, but negative prompts may not always have a significant impact in calculations. With this extension, it becomes possible to use negative prompts with effects comparable to regular prompts. This enables stronger effects even for words that might have collapsed when their values were increased too much in negative prompts before, by incorporating negative effects into the prompts.<br>


Two nodes are added to the loader. 

It's not so difficult that you need instructions on how to use it. 

Please specify the start and end of cd-tuner in the range of 0,1000 (not in step units for implementation reasons).<br>

Acknowledgment<br>

We would like to thank hako-mikan , the creator of the two implementations .<br>



---------------------------------------------------------------------------------------------
