# Authority: dag

# Upstream: Jan Kneschke <jan@kneschke.de>

Summary: Modular Log Analyzer.
Name: modlogan
Version: 0.8.10
Release: 0
License: GPL
Group: Applications/Internet
URL: http://jan.kneschke.de/projects/modlogan/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.kneschke.de/projekte/modlogan/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gd-devel >= 1.8.3, libxml2-devel, pcre-devel, adns-devel, perl, libtool

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
%doc AUTHORS ChangeLog COPYING Doxyfile NEWS README TODO doc/license.GD  doc/*txt doc/*ihtml
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/modlogan/
%{_bindir}/*
%{_libdir}/*

%changelog
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
