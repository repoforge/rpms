# $Id$
# Authority: dag
# Upstream: 

Summary: File encryption utility
Name: bcrypt
Version: 1.1
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://bcrypt.sourceforge.net/

Source: http://bcrypt.sourceforge.net/bcrypt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bcrypt is a cross platform file encryption utility. Encrypted files are
portable across all supported operating systems and processors.
Passphrases must be between 8 and 56 characters and are hashed internally
to a 448 bit key. However, all characters supplied are significant. The
stronger your passphrase, the more secure your data.

In addition to encrypting your data, bcrypt will by default overwrite the
original input file with random garbage three times before deleting it in
order to thwart data recovery attempts by persons who may gain access to
your computer. If you're not quite ready for this level of paranoia yet,
see the installation instructions below for how to disable this feature.
If you don't think this is paranoid enough.. see below.

Bcrypt uses the blowfish encryption algorithm published by Bruce Schneier
in 1993. More information on the algorithm can be found at Counterpane.
Specifically, bcrypt uses Paul Kocher's implementation of the algorithm.
The source distributed with bcrypt has been slightly altered from the
original.

%prep
%setup

%{__perl} -pi.orig -e 's|\${PREFIX}/man/man1|\${PREFIX}/share/man/man1|g' Makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man1/bcrypt.1*
%{_bindir}/bcrypt

%changelog
* Fri Nov 30 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
