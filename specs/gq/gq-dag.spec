# $Id$
# Authority: axel

Summary: Interactive graphical LDAP browser
Name: gq
Version: 0.6.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://biot.com/gq/

Source: http://dl.sf.net/gqclient/gq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openldap-devel >= 2.0

%description
GQ is GTK+ LDAP client and browser utility. It can be used
for searching LDAP directory as well as browsing it using a
tree view.

%prep
%setup

%build
%configure \
	--enable-cache \
	--enable-browser-dnd
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_bindir}/*
%{_datadir}/gnome/apps/Internet/gq.desktop
%{_datadir}/pixmaps/gq/

%changelog
* Thu Jan 20 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
