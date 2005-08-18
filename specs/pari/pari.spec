# $Id$
# Authority: dries

Summary: PARI/GP Number Theory-oriented Computer Algebra System
Name: pari
Version: 2.1.6
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://www.parigp-home.de/

Source: pari-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, readline-devel

%description
Pari is a library of number theory algorithms.

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
# FIXME: configure macro can't be used: it doesn't accept/ignore arguments like --target=
# FIXME: non standard mandir

# strange not needed? code
%{__perl} -pi -e "s|^ *Defun\(.*||g;" src/gp/gp_rl.c
%{__perl} -pi -e "s|^ *Bind\(.*||g;" src/gp/gp_rl.c

./Configure --host=i686-redhat-linux-gnu  --prefix=/usr \
	--bindir=/usr/bin  --datadir=/usr/share \
	--includedir=/usr/include --libdir=/usr/lib --mandir=/usr/share/man/man1
%{__make} all %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%doc %{_mandir}/man1/*.1*
%{_bindir}/tex2mail
%{_bindir}/gp*
%{_libdir}/libpari.so.*
%{_libdir}/pari

%files devel
%{_includedir}/pari
%{_libdir}/libpari.so

%changelog
* Wed Aug 17 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.6-1
- Initial package.
