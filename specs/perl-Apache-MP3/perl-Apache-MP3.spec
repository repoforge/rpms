# $Id$
# Authority: dag
# Upstream: Lincoln D. Stein <lstein$cshl,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-MP3

Summary: Perl module to generate streamable directories of MP3 and Ogg Vorbis files
Name: perl-Apache-MP3
Version: 4.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-MP3/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-MP3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Apache-MP3 is a Perl module to generate streamable directories
of MP3 and Ogg Vorbis files.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/MP3/
%{perl_vendorlib}/Apache/MP3.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 4.00-1
- Initial package. (using DAR)
