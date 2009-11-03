# $Id$
# Authority: dag

Summary: Analyse the Hidden Protected Area (HPA) of your hard disk
Name: fiesta
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://sourceforge.net/projects/fiesta/

Source: http://dl.sf.net/fiesta/fiesta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
fiesta is a tool to help you analyse the structure of the Hidden Protected
Area of your hard disk, allowing for a backup to be made. It can be used as
a backup tool for your HPA equipped computer.

%prep
%setup

%build
OPTS="%{optflags}" sh compile.sh

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 fiesta %{buildroot}%{_bindir}/fiesta

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BEER-SIGNATURE-ISSUE LICENSE README TODO
%{_bindir}/fiesta

%changelog
* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
