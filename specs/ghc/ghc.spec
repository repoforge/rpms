# $Id$
# Authority: dries


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

# Warning: you need a lot of diskspace if you want to build this rpm!

Summary: The Glasgow Haskell Compiler
Name: ghc
Version: 6.4
Release: 1.2%{?dist}
License: Other
Group: Development/Languages
URL: http://www.haskell.org/ghc/

Source: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-src.tar.bz2
Source1: http://www.haskell.org/ghc/dist/%{version}/ghc-%{version}-i386-unknown-linux.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: readline-devel, readline
BuildRequires: m4, python, perl
BuildRequires: python-devel, docbook-dtds
BuildRequires: openjade, jadetex
%{?fc4:BuildRequires: compat-readline43}
%if 0%{?_without_modxorg:1}
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}
%else
BuildRequires: libXt-devel, mesa-libGLU-devel
%endif
Requires: readline

%description
The Glasgow Haskell Compiler is a robust, fully-featured, optimising
compiler for the functional programming language Haskell. GHC compiles
Haskell to either native code or C. It implements numerous experimental
language extensions to Haskell for example concurrency, a foreign language
interface, several type-system extensions, exceptions, and so on. GHC comes
with a generational garbage collector, a space and time profiler, and a
comprehensive set of libraries.

%prep
%setup -a 1

%build
# This is ugly and x86 centric... :-(
%{__mkdir_p} ghc-%{version}/temp
echo `pwd`/ghc-%{version}/lib/i386-unknown-linux/ghc-%{version} -B`pwd`/ghc-%{version}/lib/i386-unknown-linux \$\{1+\"\$@\"\} > ghc-%{version}/lib/i386-unknown-linux/ghc
echo `pwd`/ghc-%{version}/lib/i386-unknown-linux/ghc-asm.prl \$\{1+\"\$@\"\} > ghc-%{version}/lib/i386-unknown-linux/ghc-asm
chmod +x ghc-%{version}/lib/i386-unknown-linux/ghc
chmod +x ghc-%{version}/lib/i386-unknown-linux/ghc-asm
export PATH=`pwd`/ghc-%{version}/lib/i386-unknown-linux:`pwd`/ghc-%{verson}/bin/i386-unknown-linux/:$PATH
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc README docs
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_libexecdir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 6.4-1.2
- Rebuild for Fedora Core 5.

* Fri Jul 1 2005 Dries Verachtert <dries@ulyssis.org>
- Update to release 6.4.

* Mon Mar 1 2004 Dries Verachtert <dries@ulyssis.org>
- first packaging for Fedora Core 1
