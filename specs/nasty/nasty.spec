# $Id$
# Authority: dag
# Upstream: Folkert Vanheusden <folkert@vanheusden.com>

Summary: Recover the passphrase of a PGP or GPG key
Name: nasty
Version: 0.6
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.vanheusden.com/nasty/

Source: http://www.vanheusden.com/nasty/nasty-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: gpgme-devel >= 1.0
BuildRequires: gpgme-devel

%description
Nasty is a program that helps to recover the passphrase of a PGP or GPG key.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -DVERSION=\\\"\${VERSION}\\\""

%install
%{__rm} -rf %{buildroot}
#makeinstall
%{__install} -Dp -m0755 nasty %{buildroot}%{_bindir}/nasty

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.txt readme.txt
%{_bindir}/nasty

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
