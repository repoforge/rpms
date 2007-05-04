# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Find

Summary: Perl module to find RFC 822 email addresses in plain text
Name: perl-Email-Find
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Find/

Source: http://www.cpan.org/modules/by-module/Email/Email-Find-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Email-Find is a Perl module to find RFC 822 email addresses in plain text.

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
%doc %{_mandir}/man3/Email::Find.3pm*
%doc %{_mandir}/man3/Email::Find::addrspec.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Find/
%{perl_vendorlib}/Email/Find.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
