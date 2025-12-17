import random
import string

print(" ")
print("ABAtch-Obfuscator")
print(" ")
inputbat = input("Input: ")
outputbat = input("Output: ")

def abatch_obfuscator(input_bat, output_bat):
    with open(input_bat, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    alphabet = list(string.ascii_letters + string.digits + "/\\:.-_")
    random.shuffle(alphabet)
    
    def gen_confusing_name():
        return "".join(random.choices("AА", k=10))

    key_names = [gen_confusing_name() for _ in range(15)]
    key_names = list(set(key_names)) 
    
    storage = {}
    temp_alph = alphabet[:]
    
    for name in key_names[:8]:
        if not temp_alph: break
        chunk = "".join(temp_alph[:10])
        temp_alph = temp_alph[10:]
        padding = "".join(random.choices(string.ascii_letters + string.digits, k=40))
        storage[name] = chunk + padding

    header = [
        "@echo off",
        "chcp 65001 >nul",
        "setlocal enabledelayedexpansion"
    ]
    
    all_vars = []
    for name, val in storage.items():
        all_vars.append(f'set "{name}={val}"')
    
    for _ in range(50):
        f_name = gen_confusing_name()
        if f_name in storage: continue
        f_val = "".join(random.choices(string.ascii_letters + string.digits, k=45))
        all_vars.append(f'set "{f_name}={f_val}"')
    
    random.shuffle(all_vars)
    header.extend(all_vars)

    spc_var = gen_confusing_name()
    header.append(f'set "{spc_var}= "')

    obfuscated_lines = []
    for line in lines:
        line = line.strip()
        if not line: continue
        
        cmd_parts = []
        for char in line:
            if char == " ":
                cmd_parts.append(f"!{spc_var}!")
                continue
            
            found = False
            for kname, kval in storage.items():
                if char in kval:
                    idx = kval.find(char)
                    cmd_parts.append(f"!{kname}:~{idx},1!")
                    found = True
                    break
            
            if not found:
                cmd_parts.append(char)
        
        obfuscated_lines.append(f"call {''.join(cmd_parts)}")

    with open(output_bat, 'w', encoding='utf-8') as f:
        f.write("\n".join(header) + "\n" + "\n".join(obfuscated_lines))

    print(f"[+] Setup obf: {output_bat}")

if __name__ == "__main__":
    abatch_obfuscator(inputbat, outputbat)
