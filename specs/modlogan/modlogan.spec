# $Id$
# Authority: dag
# Upstream: Jan Kneschke <jan$kneschke,de>

Summary: Modular Log Analyzer
Name: modlogan
Version: 0.8.13
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://jan.kneschke.de/projects/modlogan/

Source: http://jan.kneschke.de/projects/modlogan/download/modlogan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gd-devel >= 1.8.3, libxml2-devel, pcre-devel, adns-devel, perl, libtool
BuildRequires: gcc-c++

%description
Modlogan is a modular logfile analyzer written.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

for i in %{buildroot}%{_sysconfdir}/modlogan/*-dist; do
	if test ! -f `echo $i |sed 's/-dist//'`; then
		%{__mv} -f  $i `echo $i |sed 's/-dist//'` || true
	fi
done

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/*ihtml doc/*txt doc/license.GD Doxyfile NEWS README TODO
%doc %{_mandir}/man1/modlogan.1*
%config %{_sysconfdir}/modlogan/
%{_bindir}/modlogan
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.13-1.2
- Rebuild for Fedora Core 5.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.8.13-1
- Updated to release 0.8.13.

* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 0.8.11-1
- Updated to release 0.8.11.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.8.10-0
- Updated to release 0.8.10.

* Wed Jul 09 2003 Dag Wieers <dag@wieers.com> - 0.8.9-0
- Updated to release 0.8.9.

* Sun May 08 2003 Dag Wieers <dag@wieers.com> - 0.8.8-0
- Updated to release 0.8.8.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 0.8.7-0
- Updated to release 0.8.7.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 0.8.6-0
- Updated to release 0.8.6.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.8.5-0
- Updated to release 0.8.5.
- Fixed the --program-prefix problem.

* Fri Feb 21 2003 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.
- Fixed the --program-prefix problem.

* Wed Jan 08 2003 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Initial package. (using DAR)
