# $Id$
# Authority: dries
# Upstream: Peter Forty <forty$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-SimpleTemplate

Summary: Simple templates
Name: perl-Apache-SimpleTemplate
Version: 0.06b
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-SimpleTemplate/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-SimpleTemplate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Apache::SimpleTemplate is *another* Template-with-embedded-Perl package
for mod_perl. It allows you to embed blocks of Perl code into text
documents, such as HTML files, and have this code executed upon HTTP
request. It should take moments to set-up and learn; very little knowledge
of mod_perl is necessary, though some knowledge of Apache and perl is
assumed.

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
%doc README
%doc %{_mandir}/man3/Apache::SimpleTemplate.3pm*
%dir %{perl_vendorlib}/Apache/
#%{perl_vendorlib}/Apache/SimpleTemplate/
%{perl_vendorlib}/Apache/SimpleTemplate.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.06b-1
- Updated to release 0.06b.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
