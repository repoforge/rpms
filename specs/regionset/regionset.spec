# $Id$
# Authority: dag

Summary: Show or set the region of a DVD player
Name: regionset
Version: 0.1
Release: 1
License: GPL
Group: System Environment/Base
URL: http://linvdr.org/projects/regionset/

Source: http://linvdr.org/download/regionset/regionset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 
#Requires:

%description
regionset is a tool to show or configure the region of a DVD player.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CC="%{__cc} %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 regionset %{buildroot}%{_sbindir}/regionset

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%{_sbindir}/regionset

%changelog
* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
