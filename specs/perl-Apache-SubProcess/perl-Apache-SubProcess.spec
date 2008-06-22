# $Id$
# Authority: dag
# Upstream: Doug MacEachern <dougm$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-SubProcess

Summary: Perl module named Apache-SubProcess
Name: perl-Apache-SubProcess
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-SubProcess/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-SubProcess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mod_perl
BuildRequires: perl

%description
perl-Apache-SubProcess is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
#%doc %{_mandir}/man3/Apache::SubProcess.3pm*
%dir %{perl_vendorarch}/auto/Apache/
%{perl_vendorarch}/auto/Apache/SubProcess/
%dir %{perl_vendorarch}/Apache/
%{perl_vendorarch}/Apache/SubProcess.pm

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
