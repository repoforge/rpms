# $Id$
# Authority: dag
# Upstream: Nick Gerakines <nick$socklabs,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Session-Generate-UUID

Summary: Perl module to generate UUID for session ID
Name: perl-Apache-Session-Generate-UUID
Version: 0.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Session-Generate-UUID/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Session-Generate-UUID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
perl-Apache-Session-Generate-UUID is a Perl module to generate UUID
for session ID.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Apache::Session::Generate::UUID.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Apache/
%dir %{perl_vendorlib}/Apache/Session/
%dir %{perl_vendorlib}/Apache/Session/Generate/
#%{perl_vendorlib}/Apache/Session/Generate/UUID/
%{perl_vendorlib}/Apache/Session/Generate/UUID.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
