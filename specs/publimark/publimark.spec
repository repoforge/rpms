# $Id$

# Authority: dries
# Upstream: 

Summary: Tool to secretly embed text in an audio file
Name: publimark
Version: 0.1.2
Release: 1
License: GPL
Group: Applications/System
URL: http://perso.wanadoo.fr/gleguelv/soft/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

#Source: http://perso.wanadoo.fr/gleguelv/soft/publimark-%{version}.tgz
Source: http://perso.wanadoo.fr/gleguelv/soft/publimark/publimark-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: audiofile-devel, botan-devel, gcc-c++, automake, autoconf

%description
Publimark is a command line tool to secretly embed text in an audio file.
Like cryptography, it uses a pair of keys: the public one can be shared,
whereas the private one must be kept secret. Anybody can send a
steganographic message, but only the private key owner will be able read it.
Marked audio files are still playable. 

%prep
%setup

%build
%configure
# seems to be necessary when gcc296 is used:
# sed -i "s/#include.*\"scs.h\"/#include \"scs.h\"\n#include <math.h>/g;" src/scs.cpp
%{__aclocal}
%{__automake} -a
%{__autoconf}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*

%changelog
* Fri May 28 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.2-1
- Initial package.
