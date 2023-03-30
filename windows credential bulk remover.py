import subprocess

credetntial_list_result = subprocess.Popen("cmdkey /list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
credetntial_list_result = str(credetntial_list_result)
credetntial_list_result = credetntial_list_result.replace("\\r", "")
credentials = credetntial_list_result.split('\\n')
# just set the target name or part of the target name you want it's credentials removed 
credential_to_remove_contains = "credential target name or part of name here" #like: 'Adobe', or 'vscode' 
for cred in credentials:
    cred_parts = cred.split(",")
    if "Target" in cred_parts[0] and credential_to_remove_contains in cred_parts[0]:
        print(f'items: {cred_parts}')
        cred_to_remove = cred_parts[0].split("target=")[1]
        print(f'to remove: {cred_to_remove}')
        delete_result = subprocess.Popen(f"cmdkey /delete:{cred_to_remove}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        print(f'removed {delete_result}')