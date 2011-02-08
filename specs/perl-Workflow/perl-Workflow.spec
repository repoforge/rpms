# $Id$
# Authority: dag
# Upstream: Jonas B, NIelsen <jonasbn$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Workflow

Summary: Simple, flexible system to implement workflows
Name: perl-Workflow
Version: 1.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Workflow/

Source: http://search.cpan.org/CPAN/authors/id/J/JO/JONASBN/Workflow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor) >= 0.18
BuildRequires: perl(Class::Factory) >= 1
BuildRequires: perl(Class::Observable) >= 1.04
BuildRequires: perl(DBD::Mock) >= 0.1
BuildRequires: perl(DBI)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(DateTime) >= 0.15
BuildRequires: perl(DateTime::Format::Strptime) >= 1
BuildRequires: perl(Exception::Class) >= 1.1
BuildRequires: perl(File::Slurp)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Log::Dispatch) >= 2
BuildRequires: perl(Log::Log4perl) >= 0.34
BuildRequires: perl(Module::Build) >= 0.36
BuildRequires: perl(Safe)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More) >= 0.41
BuildRequires: perl(XML::Simple) >= 2
Requires: perl(Carp)
Requires: perl(Class::Accessor) >= 0.18
Requires: perl(Class::Factory) >= 1
Requires: perl(Class::Observable) >= 1.04
Requires: perl(DBI)
Requires: perl(Data::Dumper)
Requires: perl(DateTime) >= 0.15
Requires: perl(DateTime::Format::Strptime) >= 1
Requires: perl(Exception::Class) >= 1.1
Requires: perl(File::Slurp)
Requires: perl(Log::Dispatch) >= 2
Requires: perl(Log::Log4perl) >= 0.34
Requires: perl(Safe)
Requires: perl(XML::Simple) >= 2

%filter_from_requires /^perl*/d
%filter_setup
BuildRequires: perl

%description
Simple, flexible system to implement workflows.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO doc/ eg/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/Workflow/
%{perl_vendorlib}/Workflow.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.34-1
- Updated to version 1.34.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.33-1
- Updated to version 1.33.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.32-1
- Updated to version 1.32.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.28-1
- Initial package. (using DAR)
