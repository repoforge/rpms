# $Id$
# Authority: dries

Summary: Client libraries for GGZ gaming zone
Name: ggz-client-libs
Version: 0.0.12
Release: 1
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
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man3/ggz*
%doc %{_mandir}/man5/ggz*
%doc %{_mandir}/man6/ggz*
%{_bindir}/ggz-config
%{_bindir}/ggz-wrapper
%{_libdir}/libggzcore.so.*
%{_libdir}/libggzmod.so.*
%{_sysconfdir}/xdg/menus/applications-merged/ggz.merge.menu
%{_sysconfdir}/xdg/menus/ggz.menu
%{_datadir}/desktop-directories/ggz*.directory
%{_datadir}/locale/*/LC_MESSAGES/ggz-config.mo

%files devel
%{_includedir}/ggz*.h
%{_libdir}/libggzcore.a
%{_libdir}/libggzmod.a
%{_libdir}/libggzcore.so
%{_libdir}/libggzmod.so
%exclude %{_libdir}/*.la

%changelog
* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
