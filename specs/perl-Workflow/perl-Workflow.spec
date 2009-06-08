# $Id$
# Authority: dag
# Upstream: Jonas B, NIelsen <jonasbn$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Workflow
%define real_version 1.32

Summary: Simple, flexible system to implement workflows
Name: perl-Workflow
Version: 1.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Workflow/

Source: http://www.cpan.org/modules/by-module/Workflow/Workflow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Simple, flexible system to implement workflows.

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
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 1.32-1
- Updated to version 1.32.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.31-1
- Updated to release 0.31.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 0.28-1
- Initial package. (using DAR)
