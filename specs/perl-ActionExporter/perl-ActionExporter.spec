# $Id$
# Authority: dag
# Upstream: Adam Griffiths <public$adam-griffiths,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ActionExporter

Summary: Perl module to extend Exporter with export_action()
Name: perl-ActionExporter
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ActionExporter/

Source: http://www.cpan.org/authors/id/A/AD/ADZZ/ActionExporter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-ActionExporter is a Perl module to extend Exporter with the
export_action() function, for use with the GCT::XSP::ActionTaglib
module. 

This package contains the following Perl module:

    ActionExporter

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/ActionExporter.3pm*
%{perl_vendorlib}/ActionExporter.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
