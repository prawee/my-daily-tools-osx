# How to solved with ruby

## Error

```bash
brew list
```

```text
Traceback (most recent call last):
	7: from /usr/local/Homebrew/Library/Homebrew/brew.rb:23:in `<main>'
	6: from /usr/local/Homebrew/Library/Homebrew/brew.rb:23:in `require_relative'
	5: from /usr/local/Homebrew/Library/Homebrew/global.rb:132:in `<top (required)>'
	4: from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/core_ext/kernel_require.rb:54:in `require'
	3: from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/core_ext/kernel_require.rb:54:in `require'
	2: from /usr/local/Homebrew/Library/Homebrew/tap.rb:3:in `<top (required)>'
	1: from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/core_ext/kernel_require.rb:54:in `require'
/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/core_ext/kernel_require.rb:54:in `require': cannot load such file -- commands (LoadError)
```

## Fixed

```bash
sudo gem update --system
```

```bash
Password:
Updating rubygems-update
Fetching rubygems-update-3.1.4.gem
Successfully installed rubygems-update-3.1.4
Parsing documentation for rubygems-update-3.1.4
Installing ri documentation for rubygems-update-3.1.4
Installing darkfish documentation for rubygems-update-3.1.4
Done installing documentation for rubygems-update after 104 seconds
Parsing documentation for rubygems-update-3.1.4
Done installing documentation for rubygems-update after 0 seconds
Installing RubyGems 3.1.4
```

```bash
brew update
brew install rbenv
```

## Test

```bash
brew list
```
