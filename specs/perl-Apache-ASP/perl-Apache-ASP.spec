# $Id$
# Authority: dag
# Upstream: Joshua Chamas <josh,chamas$gmail,com>
 
%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-ASP

Summary: Active Server Pages for Apache with mod_perl
Name: perl-Apache-ASP
Version: 2.61
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-ASP/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-ASP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(ExtUtils::MakeMaker)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(MLDBM)
BuildRequires: perl(MLDBM::Sync)
Requires: perl >= 0:5.00503, perl(Digest::MD5), perl(MLDBM), perl(MLDBM::Sync)
#Requires: mod_perl

### FIXME: Provide perl(Apache::ASP::Share::CORE) as it seems to be missing
Provides: perl(Apache::ASP::Share::CORE)

%description
Apache::ASP provides an Active Server Pages port to the Apache Web
Server with Perl scripting only, and enables developing of dynamic
web applications with session management and embedded Perl code.
There are also many powerful extensions, including XML taglibs, XSLT
rendering, and new events not originally part of the ASP API!

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" \
	--ssl
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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man1/asp-perl.1*
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/ASP/
%{perl_vendorlib}/Apache/ASP.pm
%dir %{perl_vendorlib}/Bundle/
%dir %{perl_vendorlib}/Bundle/Apache/
%{perl_vendorlib}/Bundle/Apache/ASP/
%{perl_vendorlib}/Bundle/Apache/ASP.pm
%{_bindir}/asp-perl

%changelog
* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 2.61-1
- Updated to release 2.61.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.59-1
- Updated to release 2.59.

* Fri Aug 06 2004 Dag Wieers <dag@wieers.com> - 2.57-2
- Added explicit perl(Apache::ASP::Share::CORE) provides. (Johnathan Kupferer)

* Sun Jul 11 2004 Dag Wieers <dag@wieers.com> - 2.57-1
- Cosmetic changes.

* Fri Jul  9 2004 Johnathan Kupferer <kupferer@redhat.com> 2.57-1
- Initial build.
