# $Id$
# Authority: dag
# Upstream: Niklas Knutsson <nq$altern,org>

Summary: Versatile desktop calculator
Name: qalculate
Version: 0.8.1
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://qalculate.sourceforge.net/

Source: http://dl.sf.net/qalculate/qalculate-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, libglade2-devel, pkgconfig, cln-devel
BuildRequires: ImageMagick, gettext, glib2-devel >= 2.4
BuildRequires: intltool, perl-XML-Parser
Requires: gnuplot, wget

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting,
and a graphical interface (GTK+) that uses a one-line fault-tolerant
expression entry (although it supports optional traditional buttons). 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}
										
%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -Dp -m0644 data/icon.xpm %{buildroot}%{_datadir}/pixmaps/qalculate.xpm

%post
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_datadir}/gnome/help/qalculate/
%{_bindir}/qalc
%{_bindir}/qalculate-gtk
%{_datadir}/applications/qalculate.desktop
%{_datadir}/applnk/Utilities/qalculate.desktop
%{_datadir}/pixmaps/qalculate.xpm
%{_datadir}/qalculate/
%{_datadir}/omf/qalculate/
%{_includedir}/libqalculate/
%{_libdir}/libqalculate.a
%exclude %{_libdir}/libqalculate.la
%{_libdir}/libqalculate.so*
%{_libdir}/pkgconfig/libqalculate.pc
%exclude %{_localstatedir}/scrollkeeper/

%changelog
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
