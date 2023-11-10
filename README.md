# Marcel Broccoli

Marcel's broccoli module for simplifying his coding.


## Module

### Structure

```
-marcelbroccoli
 |-functions.py         Custom functions
   |-load_env           Load a `.env` file and log an error if any
   |-load_config_file   Load a JSON configuration file and return config object
   |-starts_with        Check if string starts with pattern (case sensitive or case insensitive)
   |-str2datetime       Convert from all date and date time sources to date object
   |-datetime2str       Convert date to string in HomeBank format
   |-format_phone       Format phone number in Swiss and French style (depending on prefix)
 |-logger.py            Custom logging
   |-logger             Logger object
   |-setup              Setup custom logger
   |-log                Write log entry
```

### Documentation

Click here for [module documentation](marcelbroccoli/README.md).


## Use Module

Load each module (I recommend use module aliases for shorter code).

```python
import marcelbroccoli.errorcodes as marcelec
import marcelbroccoli.config as config
import marcelbroccoli.functions as marcelfn
import marcelbroccoli.logger as marcellg

if __name__ == '__main__':
	# set working dir
	working_dir = marcelfn.set_working_dir(__file__)

  # load config
	cfg_file = os.path.join(working_dir, 'config.json')
	logger.info("Load configuration file '{}'.".format(cfg_file))
	config.data = config.load_config_file(cfg_file)
	if config.data is None: errorcode = ERR_LOADING_CONFIG

  # access config variable
  print("my variable: ", config.data['my_cfg_var'])
```


## Manage Releases

Default branch is `dev` for development and updates of module.

Example for release 1.0.0.
```bash
release=1.0.0
# Create and checkout a new "release" branch.
git checkout -b release-$release dev

# Finalize code and update version in setup.py
git add setup.py marcelbroccoli/version.py
git commit -m "update version $release"

# Merge final version of release into `dev` and `main`.
git checkout main
git merge release-$release
git push
git checkout dev
git merge release-$release
git push
# Delete branch release-$release
git branch -d release-$release
# Create and push tag to main branch
git tag -a $release -m "release $release" main
git push --tags
git status

```

Create a new release on GitHub with the created tag.


## Use Release in pip

1. Jump to the release page of the repository on GitHub.
1. Copy the tar.gz link of the release.
1. use the link for `pip install`.

```bash
pip install https://github.com/chemage/marcelbroccoli/archive/refs/tags/1.4.1.tar.gz
```


### Unrelated but Useful

## Setup SSH key for MingW

As these modules have been developed on Windows and Linux, the need to push using MingW
came up. It was easier than using the TortoiseGit GUI all the time.

Setup a `config` file as follows.

```
Host github.com-chemage
  HostName github.com
  IdentityFile ~/.ssh/<your-identity-file>-openssh.ppk
  IdentitiesOnly yes
```

Note that the OpenSSH format is necessary (in case you generate your keys with PuTTY).

Then either add a new remote for CMD or use modify the remote `origin` as follows.

```bash
git remote add origin git@github.com-chemage:chemage/marcelbroccoli.git
```

One more thing, is to set the correct upstream.

```bash
git branch --set-upstream-to origin-cmd
```

That's it. 

Now you can push and pull from MingW.

Be aware that you won't be able to use the TortoiseGit GUI without reverting to the remote `origin`.
