# $Id$

# Authority: dag
# Upstream: Tobi Oetiker <oetiker@ee.ethz.ch>

%define rversion 1.0.46
%define pversion %(rpm -q php-devel --qf '%{RPMTAG_VERSION}' | tail -1)
%define release 4

Summary: RRDtool - round robin database
Name: rrdtool
Version: %{rversion}
Release: %{release}
License: GPL
Group: Applications/Databases
URL: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/pub/%{name}-%{version}.tar.gz
Patch: php-rrdtool-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: php-devel, tcl-devel, perl

%description
RRD is the Acronym for Round Robin Database. RRD is a system to store and 
display time-series data (i.e. network bandwidth, machine-room temperature, 
server load average). It stores the data in a very compact way that will not 
expand over time, and it presents useful graphs by processing the data to 
enforce a certain data density. It can be used either via simple wrapper 
scripts (from shell or Perl) or via frontends that poll network devices and 
put a friendly user interface on it.

%package devel
Summary: RRDtool - round robin database static libraries and headers
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
RRD is the Acronym for Round Robin Database. RRD is a system to store and
display time-series data (i.e. network bandwidth, machine-room temperature,
server load average). This package allow you to use directly this library.

%package -n php-rrdtool
Summary: A PHP module for using RRD databases or rrdtool.
Version: %{pversion}
Release: %{release}_%{rversion}
Group: Development/Languages

BuildRequires: php-devel
Requires: php = %{pversion}, rrdtool = %{rversion}

%description -n php-rrdtool
The php-rrdtool package contains a dynamic shared object that will add
RRD and RRDtool support to PHP.

This module is built for PHP v%{pversion}.

%prep
%setup

%build
%configure \
	--enable-shared \
	--enable-local-libpng \
	--enable-local-zlib \
	--with-tcllib="%{_libdir}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	examplesdir="%{buildroot}%{_datadir}/rrdtool/examples/" \
	idocdir="%{buildroot}%{_datadir}/rrdtool/doc/" \
	ihtmldir="%{buildroot}%{_datadir}/rrdtool/html/" \
	imandir="%{buildroot}%{_mandir}/man1" \
	contribdir="%{buildroot}%{_datadir}/rrdtool/contrib"

cd contrib/php4
	%configure \
		--with-rrdtool="%{buildroot}%{_prefix}" \
		--includedir="%{_includedir}/php"
	%{__make} %{?_smp_mflags} all
	#%{__make} %{?_smp_mflags} clean all
	#	CFLAGS="-g %{optflags}"
	#	LTLIBRARY_LDFLAGS="-g"
cd -

%{__install} -d -m0755 %{buildroot}/%{perl_archlib} \
			%{buildroot}%{_includedir} \
			%{buildroot}%{_libdir}/php4/ 
%{__mv} -f %{buildroot}%{_libdir}/perl/* %{buildroot}%{perl_archlib}
%{__install} -m0644 src/rrd*.h %{buildroot}%{_includedir}
%{__install} -m0755 contrib/log2rrd/log2rrd.pl %{buildroot}%{_bindir}
%{__install} -m0755 contrib/php4/modules/rrdtool.so %{buildroot}%{_libdir}/php4/

### Clean up examples
%{__perl} -pi -e '
		s|^#!  \@perl\@|#!%{__perl}|i;
		s|\015||gi;
	' examples/*.pl

### Clean up buildroot
%{__rm} -rf contrib/php4/examples/CVS/
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}
 
%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTRIBUTORS COPYING COPYRIGHT README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/rrdtool/
%{perl_archlib}

%files devel
%defattr(-, root, root, 0755)
%doc examples/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
#exclude %{_libdir}/*.la

%files -n php-rrdtool
%defattr(-, root, root, 0755)
%doc contrib/php4/CREDITS contrib/php4/EXPERIMENTAL contrib/php4/INSTALL
%doc contrib/php4/README contrib/php4/USAGE contrib/php4/examples/
%{_libdir}/php4/*.so

%changelog
* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 1.0.46-0
- Updated to release 1.0.46.

* Thu Jul 24 2003 Dag Wieers <dag@wieers.com> - 1.0.45-0
- Fixed the longstanding php-rrdtool bug.
- Updated to release 1.0.45.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 1.0.44-0
- Updated to release 1.0.44.

* Thu May 08 2003 Dag Wieers <dag@wieers.com> - 1.0.42-4
- Fixed a problem with php-rrdtool module.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 1.0.42-0
- Updated to release 1.0.42.
- Merge php-rrdtool package with this package.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 1.0.41-0
- Updated to release 1.0.41.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 1.0.40-4
- Cleaned up perl stuff and added %{_perl_archlib} macro.

* Wed Oct 23 2002 Dag Wieers <dag@wieers.com> - 1.0.40-0
- Updated to release 1.0.40.

* Wed Sep 11 2002 Dag Wieers <dag@wieers.com> - 1.0.39-0
- Updated to release 1.0.39.

* Wed Apr 10 2002 Dag Wieers <dag@wieers.com> - 1.0.35-0
- Initial package.
