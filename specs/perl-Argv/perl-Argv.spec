# $Id$
# Authority: cmr
# Upstream: David Boyce <dsb$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Argv

Summary: Perl module named Argv
Name: perl-Argv
Version: 1.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Argv/

Source: http://www.cpan.org/modules/by-module/Argv/Argv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Argv is a Perl module.

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
* Wed Jul 15 2009 Unknown - 1.24-1
- Initial package. (using DAR)
