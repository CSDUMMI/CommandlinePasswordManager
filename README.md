# A simple Password Manager for the Commandline
If you are suprised to see that this little tool was
written, be because today most passwords are needed
in the Browser, where many people sign in and out
of accounts every day. But I am a developer, thus
I need my Passwords where I most use them, in the
Commandline. Here where I have to enter my credentials
blind a utility like this is more usefull than any 
Browser Extension.

# How this is build
All the Passwords are derived from
a combination of service specific rubbish
and the Masterpassword, then hashed
by SHA256 and split in halve to make the
first halve upper the second lower case.
And thus you have the principle function
of this program.


# How to use it in the Commandline
There are these commands
```bash
pass get <service>			Get Password to service
pass set				Set Masterpassword
pass add <name> <split_at> <salt>	Add new service
pass list				List services
```
