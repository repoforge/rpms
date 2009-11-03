# $Id$
# Authority: dries

Summary: Client libraries for GGZ gaming zone
Name: ggz-client-libs
Version: 0.0.14
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.ggzgamingzone.org/

Source: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/ggz-client-libs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libggz-devel, gettext

%description
GGZ (which is a recursive acronym for GGZ Gaming Zone) develops libraries,
games and game-related applications for client-server online gaming. Player
rankings, game spectators, AI players and a chat bot are part of this effort.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man3/ggz*.3*
%doc %{_mandir}/man5/ggz*.5*
%doc %{_mandir}/man6/ggz*.6*
%doc %{_mandir}/man7/ggz*.7*
%doc %{_mandir}/man1/ggz*.1*
%{_bindir}/ggz
%{_bindir}/ggz-config
%{_bindir}/ggz-wrapper
%{_libdir}/libggzcore.so.*
%{_libdir}/libggzmod.so.*
%{_libdir}/ggz/
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_sysconfdir}/xdg/menus/ggz.menu
%{_datadir}/desktop-directories/ggz*.directory
%{_datadir}/locale/*/LC_MESSAGES/ggz-config.mo
%{_datadir}/locale/*/LC_MESSAGES/ggzcore.mo

%files devel
%{_includedir}/ggz*.h
%{_libdir}/libggzcore.a
%{_libdir}/libggzmod.a
%{_libdir}/libggzcore.so
%{_libdir}/libggzmod.so
%exclude %{_libdir}/*.la

%changelog
* Wed Sep  5 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.14-1
- Updated to release 0.0.14.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
