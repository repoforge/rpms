# $Id$

# Authority: dries
# Upstream:

Summary: Tool to secretly embed text in an audio file
Name: publimark
Version: 0.1.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://perso.wanadoo.fr/gleguelv/soft/

#Source: http://perso.wanadoo.fr/gleguelv/soft/publimark-%{version}.tgz
Source: http://perso.wanadoo.fr/gleguelv/soft/publimark/publimark-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, automake, autoconf
BuildRequires: audiofile-devel, botan-devel >= 1.3.12

%description
Publimark is a command line tool to secretly embed text in an audio file.
Like cryptography, it uses a pair of keys: the public one can be shared,
whereas the private one must be kept secret. Anybody can send a
steganographic message, but only the private key owner will be able read it.
Marked audio files are still playable.

%prep
%setup

%build
autoreconf --force --install --symlink
%configure
# seems to be necessary when gcc296 is used:
# sed -i "s/#include.*\"scs.h\"/#include \"scs.h\"\n#include <math.h>/g;" src/scs.cpp
#%{__aclocal}
#%{__automake} -a
#%{__autoconf}
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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1.2-1.2
- Rebuild for Fedora Core 5.

* Fri May 28 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.2-1
- Initial package.
