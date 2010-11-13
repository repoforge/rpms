# $Id$
# Authority: dag
# Upstream: Pascal Rigaux <pixel$merd,net>

### EL2 ships with hexedit-1.2.1-3
%{?el2:# Tag: rfx}

Summary: Hexadecimal file viewer and editor
Name: hexedit
Version: 1.2.10
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://merd.net/pixel/

Source: http://merd.net/pixel/hexedit-%{version}.src.tgz
Patch0: hexedit-1.2.2-config.patch

BuildRequires: ncurses-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Hexedit is a utility which allows you to view and edit hexadecimal
or ASCII files and/or view binary files.

%prep
%setup -n %{name}
%patch0 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall mandir="%{buildroot}%{_mandir}"

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes COPYING TODO
%doc %{_mandir}/man1/hexedit.1*
%{_bindir}/hexedit

%changelog
* Sat Sep 17 2005 Dag Wieers <dag@wieers.com> - 1.2.10-1
- Initial package. (using DAR)
