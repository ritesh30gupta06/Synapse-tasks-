def earliest_step_for_lumos(runes: str) -> int:
    
    required = set("LUMOS")    
    collected = set()          
    
    for i, ch in enumerate(runes):
        up = ch.upper()               
        if up in required:            
            collected.add(up)         
            if len(collected) == len(required):  
                return i + 1         
    return -1
