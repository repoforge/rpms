# $Id$
# Authority: dag

Summary: Gaim Extended Preferences Plugin
Name: gaim-extprefs
Version: 0.5
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gaim-extprefs.sourceforge.net/

Source: http://dl.sf.net/gaim-extprefs/gaim-extprefs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gaim-devel, pkgconfig

%description
The Extended Preferences Plugin provides additional options within Gaim
that users sometimes request, but Gaim's developers have deemed
inappropriate for inclusion in Gaim. It was originally created partially
as a proof of concept that someone's "fork" of Gaim was entirely viable
as a plugin, but also to provide Gaim users with the ability to "zoom"
their conversation text to a larger size to make up for people using
very small fonts in conversations.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README
%dir %{_libdir}/gaim/
%exclude %{_libdir}/gaim/libextprefs.a
%exclude %{_libdir}/gaim/libextprefs.la
%{_libdir}/gaim/libextprefs.so

%changelog
* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-2
- pkgconfig buildrequirement added.

* Mon Mar 13 2006 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
