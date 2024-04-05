
# Link: https://leetcode.com/problems/defanging-an-ip-address/description/

def defang_ip_address(address: str) -> str:
    
    out_str = ''

    for char in address:
        out_str += '[.]' if char == '.' else char

    return out_str


print(defang_ip_address('23.45.67.8'))