# Zelda-ALTTP-sram-checksum-reverse-engineering

Simple python3 script to calculate the checksum of slot1 in sram file of Zelda a link to the past for SNES.


Using:
python3 checksum.py <file.srm>

Explanation of the sram checksum calculation:

The checksum is calculated by subtract with carry all bytes of the slot in the sram file. The asm code is something like this:

		CLC              ; Clear carry flag
		ADC	7EF000,X ; Add with carry the first byte of the slot
		INX              ; Increment X register
		INX              ; Increment X register
		INY              ; Increment Y register
		CPY	004FEH/2    ; Compare Y with memory
		BNE	8973		     ; Branch if not equals to address 0000:8973. This loop repeats for every word in slot. When finished jumps to next instruction
            STA	02       ; Store A register in work ram address 2
		LDX	00       ; Load in X register address 0 of work ram
		LDA	#05A5AH      ; Load #5A5AH in A register
		SEC              ; Set carry flag
		SBC	02       ; Subtract with carry A with address 2 of work ram
		STA     7FE4FEH,X	; checksum set
