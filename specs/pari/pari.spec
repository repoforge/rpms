# $Id$
# Authority: dries

Summary: PARI/GP Number Theory-oriented Computer Algebra System
Name: pari
Version: 2.1.7
Release: 1.2%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://pari.math.u-bordeaux.fr/

Source: http://pari.math.u-bordeaux.fr/pub/pari/unix/pari-%{version}.tgz
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

./Configure --host="%{_host}" --prefix="%{_prefix}" --bindir="%{_bindir}" \
	--datadir="%{_datadir}" --includedir="%{_includedir}" --libdir="%{_libdir}" \
	--mandir="%{_mandir}/man1"
%{__make} all %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%doc %{_mandir}/man1/*.1*
%{_bindir}/tex2mail
%{_bindir}/gp*
%{_libdir}/libpari.so.*
%{_libdir}/pari/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/pari/
%{_libdir}/libpari.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.7-1.2
- Rebuild for Fedora Core 5.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 2.1.7-1
- Updated to release 2.1.7.

* Wed Aug 17 2005 Dries Verachtert <dries@ulyssis.org> - 2.1.6-1
- Initial package.
