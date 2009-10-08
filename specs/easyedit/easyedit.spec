# $Id$
# Authority: shuff
# Upstream: Hugh Mahon <hugh$mahon,cwx,net>

Name:         easyedit
Summary:      Easy Text Editor
Version:      1.5.0
Release:      1
License:      BSD
Group:        Applications/Editors
URL:          http://wtf.geek.nz/

Source:      http://mahon.cwx.net/sources/ee-%{version}.src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make
BuildRequires: glibc-devel
BuildRequires: ncurses-devel

Requires: glibc
Requires: ncurses

Provides: ee

%description
EE is a an easy to use text editor. Intended to be usable with
little or no instruction. Provides a terminal (curses based)
interface and features pop-up menus.


%prep
%setup

%build
%{__make}
 

%install

rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%{__install} -m 0755 ee %{buildroot}%{_bindir}/ee
%{__install} -m 0644 ee.1 %{buildroot}%{_mandir}/man1/ee.1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(755,root,root,-)
%doc %{_mandir}/man1/ee.1.gz
%{_bindir}/ee


%changelog
* Wed Oct 07 2009 Steve Huff <shuff@vecna.org> - 1.5.0-1
- Initial package (thanks to Spiro Harvey).

