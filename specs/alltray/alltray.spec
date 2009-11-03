# $Id$
# Authority: dag
# Upstream: Jochen Baier <email$jochen-baier,de>

Summary: Dock any application into the system tray
Name: alltray
Version: 0.66
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://alltray.sourceforge.net/

Source: http://dl.sf.net/alltray/alltray-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4, gcc-c++, GConf2-devel

%description
alltray allows you to dock any application into the system tray/notification
area. A high-light feature is that a click on the "close" button will
minimize to system tray.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure Makefile.in */Makefile.in

%build
%configure
%{__make}  %{?_smp_mflags} LIBDIR="%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Fix library symlinks
for lib in $(ls %{buildroot}%{_libdir}/liballtray.so.?.?.?); do
	%{__ln_s} -f $(basename $lib) ${lib//%\.?}
	%{__ln_s} -f $(basename $lib) ${lib//%\.?\.?}
#	%{__ln_s} -f $(basename $lib) ${lib//%\.?\.?\.?}
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/alltray.1*
%{_bindir}/alltray
%{_datadir}/applications/alltray.desktop
%{_datadir}/pixmaps/alltray.png
#%exclude %{_libdir}/liballtray.a
%exclude %{_libdir}/liballtray.la
%{_libdir}/liballtray.so*


%changelog
* Thu Apr 27 2006 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.60-1
- Updated to release 0.60.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 0.51-1
- Updated to release 0.51.

* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Fri Dec 17 2004 Che
- initial rpm release
