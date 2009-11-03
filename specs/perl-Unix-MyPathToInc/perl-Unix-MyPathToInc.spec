# $Id$
# Authority: dag
# Upstream: Daniel Hagerty <hag$linnaean,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-MyPathToInc

Summary: Perl module to add the location of the current program to @INC
Name: perl-Unix-MyPathToInc
Version: 0.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-MyPathToInc/

Source: http://www.cpan.org/modules/by-module/Unix/Unix-MyPathToInc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unix-MyPathToInc is a Perl module to add the location
of the current program to @INC.

This package contains the following Perl module:

    Unix::MyPathToInc

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
%doc MANIFEST META.yml
%doc %{_mandir}/man3/Unix::MyPathToInc.3pm*
%dir %{perl_vendorlib}/Unix/
#%{perl_vendorlib}/Unix/MyPathToInc/
%{perl_vendorlib}/Unix/MyPathToInc.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
