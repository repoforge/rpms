# $Id$
# Authority: dries

Summary: Library for client-server games
Name: libggz
Version: 0.0.12
Release: 1.2
License: LGPL
Group: Development/Libraries
URL: http://www.ggzgamingzone.org/

Source: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%{version}/libggz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
#Requires:

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man3/ggz*
%{_libdir}/libggz.so.*

%files devel
%{_includedir}/ggz*.h
%{_libdir}/libggz.a
%{_libdir}/libggz.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1.2
- Rebuild for Fedora Core 5.

* Sat Dec 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1
- Initial package.
