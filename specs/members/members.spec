# $Id$
# Authority: yury
# Upstream: Debian Project <http://debian.org>

%define real_version 20080128
%define debian_release 5

Summary:   Outputs members of a group
Name:      members
Version:   0.0
Release:   0.%{real_version}.%{debian_release}%{?dist}
License:   GPL
Group:     Applications/System
URL:       http://ftp.de.debian.org/debian/pool/main/m/members/

Source:    http://ftp.de.debian.org/debian/pool/main/m/members/members_%{real_version}-%{debian_release}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
members is a program that sends a space-separated list of secondary
member names to its standard output.

%prep
%setup -n %{name}-%{version}

%build
make

%install
%{__rm} -rf %{buildroot}

%{__install} -m 0755 -d %{buildroot}/usr/bin
sed -i -r '/^[[:space:]]+chown/d' Makefile
make install DESTDIR="%{buildroot}"

# Install documentation
%{__install} -m 0755 -d %{buildroot}%{_mandir}/man1
%{__install} -m644 members.1 %{buildroot}%{_mandir}/man1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/members
%{_mandir}/man1/members.1

%changelog
* Sat Mar 12 2011 Yury V. Zaytsev <yury@shurup.com> - 0.0-0.20080128.5
- Ported over to RPMForge (thanks to William Horka and Philip Durbin!)
