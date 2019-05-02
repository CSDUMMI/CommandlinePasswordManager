
# Add  $PWD to $PATH and do so on every
echo "export PATH=$PATH:$PWD" >> ~/.bashrc
echo "export PASS_PY_PATH=$PWD" >> ~/.bashrc

export PATH=$PATH:$PWD
export PASS_PY_PATH=$PWD

# Clean up pass.json
# And backup pass.json in pass_backup.json
cat pass.json > pass_backup.json
echo "{}" > pass.json

# Request Masterpassword
./pass.py set

