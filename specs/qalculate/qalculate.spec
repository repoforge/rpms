# $Id$
# Authority: dag
# Upstream: Niklas Knutsson <nq$altern,org>

Summary: Versatile desktop calculator library
Name: qalculate
Version: 0.9.0
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://qalculate.sourceforge.net/

Source: http://dl.sf.net/qalculate/libqalculate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, cln-devel, gcc-c++
BuildRequires: ImageMagick, gettext, glib2-devel >= 2.4
BuildRequires: intltool, perl-XML-Parser
Requires: gnuplot, wget

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision and plotting.
This package contains the qulculate library which is used by the KDE and GTK+ 
GUI packages.

%prep
%setup -n libqalculate-%{version}

%build
%configure
%{__make} %{?_smp_mflags}
										
%install
%{__rm} -rf %{buildroot}
%makeinstall

#%post
#scrollkeeper-update -q

#%postun
#scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/qalc
%{_datadir}/qalculate/
%{_includedir}/libqalculate/
%{_libdir}/libqalculate.a
%exclude %{_libdir}/libqalculate.la
%{_libdir}/libqalculate.so*
%{_libdir}/pkgconfig/libqalculate.pc
%{_datadir}/locale/*/LC_MESSAGES/libqalculate.mo

%changelog
* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Mon Oct 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.

* Fri Jun 10 2005 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Mon Nov 22 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Initial package. (using DAR)
