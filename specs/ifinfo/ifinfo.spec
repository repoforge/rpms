# $Id$

# Authority: dag

Summary: Commandline network inquiry/formatting tool
Name: ifinfo
Version: 0.85
Release: 0
License: GPL
Group: Applications/System
URL: http://scalableinformatics.com/ifinfo.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://scalableinformatics.com/downloads/ifinfo/ifinfo-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
ifinfo is a simple commandline network inquiry/formatting tool specifically
designed to output some useful information about your network connection.
It works by querying the relevant tables in /proc as well as the output of
various Unix commands. Its entire purpose in life is to tell you what you
want to know, hopefully in the format you wish to see it.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man8/
%{__install} -m0755 ifinfo %{buildroot}%{_bindir}
%{__install} -m0755 ifinfo.8 %{buildroot}%{_mandir}/man8/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.85-0
- Initial package. (using DAR)
