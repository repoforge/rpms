# $Id$
# Authority: cmr
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Argv

Summary: Perl module named Argv
Name: perl-Argv
Version: 1.25
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Argv/

Source: http://search.cpan.org/CPAN/authors/id/D/DS/DSB/Argv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Getopt::Long) >= 2.23
Requires: perl(Getopt::Long) >= 2.23

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Argv is a Perl module.

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
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Argv.html Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Argv.3pm*
#%{perl_vendorlib}/Argv/
%{perl_vendorlib}/Argv.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 1.25-1
- Updated to version 1.25.

* Wed Jul 15 2009 Unknown - 1.24-1
- Initial package. (using DAR)
