# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Package-Generator

Summary: Perl module to generate new packages quickly and easily
Name: perl-Package-Generator
Version: 0.100
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Package-Generator/

Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Package-Generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Package-Generator is a Perl module to generate new packages
quickly and easily.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Package::Generator.3pm*
%doc %{_mandir}/man3/Package::Reaper.3pm*
%dir %{perl_vendorlib}/Package/
%{perl_vendorlib}/Package/Generator.pm
%{perl_vendorlib}/Package/Reaper.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.100-1
- Initial package. (using DAR)
