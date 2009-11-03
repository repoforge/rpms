# $Id$
# Authority: dag

%define _bindir /bin

Summary: Restricted Unix shell
Name: ibsh
Version: 0.3e
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://ibsh.sourceforge.net/

Source: http://dl.sf.net/ibsh/ibsh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 
#Requires:

%description
Iron Bars SHell, or short ibsh is a restricted working environment for Unix.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 ibsh %{buildroot}%{_bindir}/ibsh

%{__install} -Dp -m0644 globals.cmds %{buildroot}%{_sysconfdir}/ibsh/globals.cmds
%{__install} -Dp -m0644 globals.xtns %{buildroot}%{_sysconfdir}/ibsh/globals.xtns
%{__install} -dp -m0755 %{buildroot}%{_sysconfdir}/ibsh/{cmds,xtns}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog CONTRIBUTORS COPYING COPYRIGHT INSTALL README TODO *.xtns
%config(noreplace) %{_sysconfdir}/ibsh/
%{_bindir}/ibsh

%changelog
* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 
- Initial package. (using DAR)
