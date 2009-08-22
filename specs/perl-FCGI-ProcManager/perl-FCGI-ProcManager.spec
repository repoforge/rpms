# $Id$
# Authority: dag
# Upstream: Gareth Kirwan <gbjk$thermeoneurope,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FCGI-ProcManager

Summary: Functions for managing FastCGI applications
Name: perl-FCGI-ProcManager
Version: 0.19
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FCGI-ProcManager/

Source: http://www.cpan.org/modules/by-module/FCGI/FCGI-ProcManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Functions for managing FastCGI applications.

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
%doc COPYING ChangeLog MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/FCGI::ProcManager.3pm*
%dir %{perl_vendorlib}/FCGI/
#%{perl_vendorlib}/FCGI/ProcManager/
%{perl_vendorlib}/FCGI/ProcManager.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.19-1
- Updated to version 0.19.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.18-1
- Initial package. (using DAR)
