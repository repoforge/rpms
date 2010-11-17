# $Id$
# Authority: dag
# Upstream: Ricardo Signes <rjbs$cpan,org>

### EL6 ships with perl-Sub-Install-0.925-6.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Install

Summary: Perl module to install subroutines into packages easily
Name: perl-Sub-Install
Version: 0.925
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Install/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-Install-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Sub-Install is a Perl module to install subroutines into packages easily.

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
%doc %{_mandir}/man3/Sub::Install.3pm*
%dir %{perl_vendorlib}/Sub/
#%{perl_vendorlib}/Sub/Install/
%{perl_vendorlib}/Sub/Install.pm

%changelog
* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 0.925-1
- Updated to version 0.925.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.924-1
- Initial package. (using DAR)
