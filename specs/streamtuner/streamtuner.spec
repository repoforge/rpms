# $Id$
# Authority: dag
# Upstream: Jean-Yves Lefort <jylefort$brutele,be>

%define	desktop_vendor rpmforge

Summary: Stream directory browser
Name: streamtuner
Version: 0.99.99
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/streamtuner/

Source: http://savannah.nongnu.org/download/streamtuner/streamtuner-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4, curl-devel, openssl-devel, scrollkeeper
BuildRequires: libxml2-devel, python, gettext
BuildRequires: desktop-file-utils
Obsoletes: streamtuner-live365 < %{version}
Obsoletes: streamtuner-xiph < %{version}
Obsoletes: streamtuner-local < %{version}
Obsoletes: streamtuner-python < %{version}

%description
Streamtuner is a stream directory browser. Through the use
of a plugin system, it offers an intuitive GTK+ 2.0 interface
to Internet radio directories such as SHOUTcast and Live365.

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
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original             \
	--vendor %{desktop_vendor}                 \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/streamtuner.desktop

%clean
%{__rm} -rf %{buildroot}

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%doc %{_datadir}/gtk-doc/html/streamtuner/
%doc %{_datadir}/help/streamtuner/
%{_bindir}/streamtuner
%dir %{_libdir}/streamtuner/
%dir %{_libdir}/streamtuner/plugins/
%{_libdir}/streamtuner/plugins/*.so
%{_datadir}/applications/%{desktop_vendor}-streamtuner.desktop
%{_datadir}/omf/streamtuner/
%{_datadir}/pixmaps/streamtuner.png
%{_datadir}/streamtuner/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/streamtuner/
%{_libdir}/pkgconfig/streamtuner.pc
%dir %{_libdir}/streamtuner/
%dir %{_libdir}/streamtuner/plugins/
%{_libdir}/streamtuner/plugins/*.a
%exclude %{_libdir}/streamtuner/plugins/*.la
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.99.99-1.2
- Rebuild for Fedora Core 5.

* Thu Jul 17 2003 Che
- new fixes thanks to matthias haase for submitting his nice work
- new version out

* Sat Jan 18 2003 Che
- removed distribution tag in spec because of cosmetical needs for rpm2html

* Sat Dec 28 2002 Che
- added signature files
- added the icon into the source package (thanks to matthias haase again)

* Wed Dec 25 2002 Matthias Haase <matthias_haase@bennewitz.com>
- Some cleanups in order to match RH8
- smp flag added
- RPM_OPT_FLAGS added
- debugging disabled

* Sat Oct 29 2002 Rudolf Kastl
- Cosmetical changes.

* Sat Oct 05 2002 Rudolf Kastl
- Minor fixes and new version.

* Wed Aug 21 2002 Rudolf Kastl
- Initial RPM release
