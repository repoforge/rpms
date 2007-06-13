# $Id$
# Authority: dag
# Upstream: Jos Boumans <kane$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Package-Constants

Summary: Perl module to list all constants declared in a package
Name: perl-Package-Constants
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Package-Constants/

Source: http://www.cpan.org/authors/id/K/KA/KANE/Package-Constants-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-Package-Constants is a Perl module to list all constants
declared in a package

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST META.yml README
%doc %{_mandir}/man3/Package::Constants.3pm*
%dir %{perl_vendorlib}/Package/
%{perl_vendorlib}/Package/Constants.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
