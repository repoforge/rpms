# $Id$
# Authority: dag
# Upstream: Niklas Knutsson <nq$altern,org>

Summary: Versatile desktop calculator
Name: qalculate
Version: 0.7.0
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://qalculate.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/qalculate/qalculate-%{version}.tar.gz
Patch: qalculate_missing_includes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel, libglade2-devel, pkgconfig, cln-devel
BuildRequires: ImageMagick, gettext
Requires: gnuplot, wget

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting,
and a graphical interface (GTK+) that uses a one-line fault-tolerant
expression entry (although it supports optional traditional buttons). 

%prep
%setup
#patch0 -p 1

%build
%configure
%{__make} %{?_smp_mflags}
										
%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -D -m0644 data/icon.xpm %{buildroot}%{_datadir}/pixmaps/qalculate.xpm

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
%{_bindir}/qalculate
%{_datadir}/applications/qalculate.desktop
%{_datadir}/applnk/Utilities/qalculate.desktop
%{_datadir}/pixmaps/qalculate.xpm
%{_datadir}/qalculate/
%{_datadir}/qalculate/
%{_datadir}/omf/qalculate/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Nov 13 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Initial package. (using DAR)
