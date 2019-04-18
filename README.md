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


# How to use this
A look into the pass.json file:
```js
{
	"someService": {
		"split_at":100,
		"salt":"some_service_salt_can_be_anything_you_want",
	},
	"masterpass":"c40fbd0be29679dd4..."
}
```
Every Service to which you want a Passwords needs such a field 
as `"someService"` here.
`"split_at"` is the index at which the SHA256 Hash, the resulting password,
is split, some services want your password to be of a certain length.
`"salt"` is the field with the rubbish, that combined with the masterpassword
gives the Password.

The `"masterpass"` field is special because it has the SHA512 Hash of the
Masterpassword.

# How to use it in the Commandline
There are two commands:
`get` and `set`.
`set` creates a new Masterpassword.
`get <service>` prints the password to the service, after entering the Masterpassword.

