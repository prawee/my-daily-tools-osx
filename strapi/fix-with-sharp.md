# How to fix install/run error with sharp

## Error 

```bash

```

## Solved it

open with `iTerm` without `rosetta`

```bash
brew info vips
```

```bash
vips: stable 8.10.5
Image processing library
https://github.com/libvips/libvips
Not installed
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/vips.rb
License: LGPL-2.1-or-later
==> Dependencies
Build: pkg-config ✔
Required: cfitsio ✘, fftw ✘, fontconfig ✘, gettext ✔, giflib ✘, glib ✘, imagemagick ✘, libexif ✘, libgsf ✘, libheif ✘, libimagequant ✘, libmatio ✘, libpng ✘, librsvg ✘, libspng ✘, libtiff ✘, little-cms2 ✘, mozjpeg ✘, openexr ✘, openslide ✘, orc ✘, pango ✘, poppler ✘, webp ✘
==> Analytics
install: 4,669 (30 days), 15,120 (90 days), 50,202 (365 days)
install-on-request: 4,560 (30 days), 13,879 (90 days), 39,714 (365 days)
build-error: 0 (30 days)
```

```bash
brew reinstall vips
```

```bash
==> Downloading https://homebrew.bintray.com/bottles/cfitsio-3.490.arm64_big_sur
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/e5e1b4c2c73622ff93025
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/gmp-6.2.1.arm64_big_sur.bot
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/ff4ad8d068ba4c14d146a
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/isl-0.23.arm64_big_sur.bott
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/5b066bc471862c8d16608
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/mpfr-4.1.0.arm64_big_sur.bo
==> Downloading from https://d29vzk4ow07wi7.cloudfront.net/9df11560dd3650ffae35c
######################################################################## 100.0%
==> Downloading https://homebrew.bintray.com/bottles/libmpc-1.2.1.arm64_big_sur.
######################################################################## 100.0%
Error: gcc: the bottle needs the Xcode CLT to be installed.
You can try to install from source with:
  brew install --build-from-source gcc
Please note building from source is unsupported. You will encounter build
failures with some formulae. If you experience any issues please create pull
requests instead of asking for help on Homebrew's GitHub, Twitter or any other
official channels.
```

```bash
brew install --build-from-source gcc
```

```bash
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/core).
==> Updated Formulae
Updated 1 formula.

==> Downloading https://homebrew.bintray.com/bottles/gmp-6.2.1.arm64_big_sur.bottle.tar.gz
Already downloaded: /Users/prawee/Library/Caches/Homebrew/downloads/53a5d5fa040098ba7c06af4feded400cff20e49fc5a56e165d14373c74bac32a--gmp-6.2.1.arm64_big_sur.bottle.tar.gz
==> Downloading https://homebrew.bintray.com/bottles/isl-0.23.arm64_big_sur.bottle.tar.gz
Already downloaded: /Users/prawee/Library/Caches/Homebrew/downloads/d2e31d619367bf22d9684d2f15475628d13ba028f0d1595bd89065ef3e62f978--isl-0.23.arm64_big_sur.bottle.tar.gz
==> Downloading https://homebrew.bintray.com/bottles/mpfr-4.1.0.arm64_big_sur.bottle.tar.gz
Already downloaded: /Users/prawee/Library/Caches/Homebrew/downloads/5eabfc945992707d8e9aa04c6798599749ecd2fa15fbd388b18df35fe072c4ed--mpfr-4.1.0.arm64_big_sur.bottle.tar.gz
==> Downloading https://homebrew.bintray.com/bottles/libmpc-1.2.1.arm64_big_sur.bottle.tar.gz
Already downloaded: /Users/prawee/Library/Caches/Homebrew/downloads/0e834f839450c0e1fc5db528de89e61324bb94bdacb31038ec4ad8613c3a0982--libmpc-1.2.1.arm64_big_sur.bottle.tar.gz
==> Downloading https://github.com/fxcoudert/gcc/archive/gcc-10-arm-20210220.tar.gz
==> Downloading from https://codeload.github.com/fxcoudert/gcc/tar.gz/gcc-10-arm-20210220
##
==> Installing dependencies for gcc: gmp, isl, mpfr and libmpc
==> Installing gcc dependency: gmp
==> Pouring gmp-6.2.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/gmp/6.2.1: 21 files, 3.3MB
==> Installing gcc dependency: isl
==> Pouring isl-0.23.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/isl/0.23: 72 files, 5.0MB
==> Installing gcc dependency: mpfr
==> Pouring mpfr-4.1.0.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mpfr/4.1.0: 30 files, 5.2MB
==> Installing gcc dependency: libmpc
==> Pouring libmpc-1.2.1.arm64_big_sur.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libmpc/1.2.1: 13 files, 432.8KB
==> Installing gcc
==> ../configure --build=aarch64-apple-darwin20 --prefix=/opt/homebrew/Cellar/gcc/10.2.0_4 --libdir=/o
==> make BOOT_LDFLAGS=-Wl,-headerpad_max_install_names
==> make install
🍺  /opt/homebrew/Cellar/gcc/10.2.0_4: 1,367 files, 301.8MB, built in 16 minutes 10 seconds
```

## Failed!!!!!

```bash
arch
#arm64
```

### Update

```bash
cd
nano ~/.zshrc
```

Older

```bash
# homebrew
export PATH="/opt/homebrew/bin:$PATH"
```

to

```bash
# Support for two Homebrew installations
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
alias ibrew='arch -x86_64 /usr/local/bin/brew'
```

```bash
source ~/.zshrc
```

```bash
brew reinstall node
brew reinstall node@14
```

```bash
cd
npm uninstall -g yarn
brew install yarn
```

```bash
brew install pkg-config zlib
```

## Reference

<https://joseph-pereniguez.medium.com/how-to-fix-err-sharp-prebuilt-libvips-8-10-5-binaries-are-not-yet-available-for-darwin-arm64v8-1d29d538e932>
<https://www.component-driven.dev/articles/native-node-on-m1>
<https://soffes.blog/homebrew-on-apple-silicon>