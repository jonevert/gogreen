#!/bin/bash
#ssh into OM - in OM there is an ssh key so password input is not needed
ssh -R 9999:localhost:8160 -p 9595 gogreen@vpn.htg.is
