# $Id$
# Authority: dag

%define real_name guifications

Summary: Guifications Plugin for Gaim
Name: gaim-guifications
Version: 2.12
Release: 1
License: GPL
Group: Applications/Internet
URL: http://guifications.sourceforge.net/Guifications/

Source: http://dl.sf.net/guifications/guifications-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libtool, gettext, gaim-devel, gtk2-devel

%description
Guifications is a graphical notification plugin for the open source
instant messaging client Gaim

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README doc/*.dia doc/*.png
%{_datadir}/pixmaps/gaim/guifications/
%dir %{_libdir}/gaim/
#exclude %{_libdir}/gaim/guifications.a
%exclude %{_libdir}/gaim/guifications.la
%{_libdir}/gaim/guifications.so

%changelog
* Mon Mar 13 2006 Dag Wieers <dag@wieers.com> - 2.12-1
- Initial package. (using DAR)
