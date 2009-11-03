# $Id$
# Authority: dag


%{?el3: %define _without_perl 1}
%{?el3: %define _without_sasl 1}
%{?rh9: %define _without_perl 1}
%{?rh9: %define _without_sasl 1}
%{?rh7: %define _without_perl 1}
%{?rh7: %define _without_sasl 1}
%{?el2: %define _without_perl 1}
%{?el2: %define _without_sasl 1}

Summary: Advanced IRC bouncer
Name: znc
Version: 0.062
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://znc.sourceforge.net/

Source: http://dl.sf.net/sourceforge/znc/znc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++ 
%{!?_without_perl:BuildRequires: perl > 2:5.8.0}
%{!?_without_sasl:BuildRequires: cyrus-sasl-devel}
%{!?_without_ssl:BuildRequires: openssl-devel}

%description
ZNC is an IRC bounce with many advanced features like detaching,
multiple users, per channel playback buffer, SSL, IPv6, transparent
DCC bouncing, Perl and C++ module support to name a few.

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
%{__perl} -pi.add_release -e 's|(?<="ZNC \%1\.3f)|-%{release}|' znc.cpp

%build
%{expand: %%define optflags %{optflags} %(pkg-config --cflags openssl)}
%configure \
    --with-module-prefix="%{_libdir}/znc" \
%{?_without_ssl:--disable-openssl} \
%{!?_without_sasl:--enable-sasl} \
%{?_without_perl:--disable-perl} \
%{!?_without_ipv6:--enable-ipv6} \
%{?_with_debug:--enable-debug} 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS LICENSE README znc.conf
%doc %{_mandir}/man1/znc.1*
%{_bindir}/znc
%{_datadir}/znc/
%{_libdir}/znc/

%files devel
%defattr(-, root, root, 0755)
%doc modules/sample.cpp
%doc %{_mandir}/man1/znc-buildmod.1*
%doc %{_mandir}/man1/znc-config.1*
%{_bindir}/znc-buildmod
%{_bindir}/znc-config
%{_includedir}/znc/

%changelog
* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 0.062-1
- Initial package. (using DAR)
