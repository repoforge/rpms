# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Exporter

Summary: Perl module that implements a sophisticated exporter for custom-built routines
Name: perl-Sub-Exporter
Version: 0.974
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Exporter/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-Exporter-0.974.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Sub/
%{perl_vendorlib}/Sub/Exporter/
%{perl_vendorlib}/Sub/Exporter.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.974-1
- Initial package. (using DAR)
