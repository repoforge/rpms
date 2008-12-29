# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name RRDutils

Summary: Utilities to deal with RRD files and graphs
Name: rrdutils
Version: 5.2.1
Release: 1
License: BSD
Group: Applications/Databases
URL: http://rrdutils.sourceforge.net/

Source: http://dl.sf.net/rrdutils/RRDutils-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl, rrdtool
Obsoletes: rrdUtils <= %{version}-%{release}

%description
This is a set of tools intended to help creation and displaying of RRD
files. The RRD characteristics (data sources, consolidation functions)
and the graphs are described in a configuration file that we can use to
create new instances of a RRD, and to generate the graphs for them.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/rrd/conf/

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog DESCRIPTION MANIFEST README ToDo examples/
%{_bindir}/RRD*
%{perl_vendorlib}/RRDutils.pm
%{_localstatedir}/lib/rrd/

%changelog
* Mon Dec 08 2008 Christoph Maser <cmr@financial.com> - 5.1.2-1
- Update version to 5.1.2

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 5.0.1-1.2
- Rebuild for Fedora Core 5.

* Fri Jan 27 2006 Dag Wieers <dag@wieers.com> - 5.0.1-1
- Updated to release 5.0.1.

* Sat Jan 14 2005 Dag Wieers <dag@wieers.com> - 4.2-1
- Updated to release 4.2.

* Sat Sep 25 2004 Dag Wieers <dag@wieers.com> - 3.3.5-1
- Initial package. (using DAR)
