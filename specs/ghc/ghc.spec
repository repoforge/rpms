# $Id$

# Authority: dries

# NeedsCleanup

Summary: The Glasgow Haskell Compiler
Name: ghc
Version: 6.2
Release: 1
License: Other
Group: todo
URL: http://www.haskell.org/ghc/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-src.tar.bz2
Source1: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-i386-unknown-linux.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: readline-devel, readline, m4
Requires: readline
%description
todo

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup
tar -xjvf %{SOURCE1}
mkdir -p ghc-6.2/temp
echo `pwd`/ghc-6.2/lib/i386-unknown-linux/ghc-6.2 -B`pwd`/ghc-6.2/lib/i386-unknown-linux \$\{1+\"\$@\"\} > ghc-6.2/lib/i386-unknown-linux/ghc
echo `pwd`/ghc-6.2/lib/i386-unknown-linux/ghc-asm.prl \$\{1+\"\$@\"\} > ghc-6.2/lib/i386-unknown-linux/ghc-asm
chmod +x ghc-6.2/lib/i386-unknown-linux/ghc
chmod +x ghc-6.2/lib/i386-unknown-linux/ghc-asm
export PATH=`pwd`/ghc-6.2/lib/i386-unknown-linux:`pwd`/ghc-6.2/bin/i386-unknown-linux/:$PATH
# when you use the configure macro:
# GHC configuration does not support differing host/target (i.e., cross-compiling)
./configure --program-prefix= \
	--prefix=/usr \
	--exec-prefix=/usr \
	--bindir=/usr/bin \
	--sbindir=/usr/sbin \
	--sysconfdir=/etc \
	--datadir=/usr/share \
	--includedir=/usr/include \
	--libdir=/usr/lib \
	--libexecdir=/usr/libexec \
	--localstatedir=/var \
	--sharedstatedir=/usr/com \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info
%build
%{__make} %{?_smp_mflags}

%install
%makeinstall

%files


%changelog
* Mon Mar 1 2004 Dries Verachtert <dries@ulyssis.org>
- first packaging for Fedora Core 1
