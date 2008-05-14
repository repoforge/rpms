# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Exporter

Summary: Perl module that implements a sophisticated exporter for custom-built routines
Name: perl-Sub-Exporter
Version: 0.979
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Exporter/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-Exporter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.6.0

%description
Sub-Exporter is a Perl module that implements a sophisticated exporter
for custom-built routines.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Sub::Exporter.3pm*
%doc %{_mandir}/man3/Sub::Exporter::*.3pm*
%dir %{perl_vendorlib}/Sub/
%{perl_vendorlib}/Sub/Exporter/
%{perl_vendorlib}/Sub/Exporter.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.979-1
- Updated to release 0.979.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.978-1
- Updated to release 0.978.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.976-1
- Updated to release 0.976.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.974-1
- Initial package. (using DAR)
