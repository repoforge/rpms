# $Id$
# Authority: shuff
# Upstream: Synergy+ Development List <synergy-plus-dev$googlegroups,com>


%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: Synergy+ mouse and keyboard sharing utility
Name: synergy-plus
Version: 1.3.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://code.google.com/p/synergy-plus/
Source: http://synergy-plus.googlecode.com/files/synergy-plus-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++ >= 2.95, autoconf, automake, doxygen
%{!?_without_modxorg:BuildRequires: libX11-devel, libXt-devel, libXinerama-devel, libXtst-devel, libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

Provides: %{_bindir}/synergyc %{_bindir}/synergys 
Provides: synergy = %{version}
Obsoletes: synergy

%description
Synergy lets you easily share a single mouse and keyboard between
multiple computers with different operating systems, each with its
own display, without special hardware.  It's intended for users
with multiple computers on their desk since each system uses its
own display.

Synergy+ is a bugfix fork of the original Synergy project.

%package doc

Summary: Developer documentation for Synergy+
Group: Documentation

%description doc
doxygen documentation for Synergy+.

Requires: %{name} = %{version}

%prep
%setup

%build
autoreconf
%configure
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} doxygen

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc doc/PORTING
%doc examples/synergy.conf
%{_bindir}/synergyc
%{_bindir}/synergys

%files doc
%doc doc/doxygen/

%changelog
* Thu Nov 05 2009 Steve Huff <shuff@vecna.org> - 1.3.4-1
- Initial package.
