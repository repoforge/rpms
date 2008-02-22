# $Id$
# Authority: dries
# Upstream: Leo Charre <leocharre$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Auth-Auto

Summary: Automatic authentication maintenance and persistence for cgi scripts
Name: perl-CGI-Auth-Auto
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Auth-Auto/

Source: http://www.cpan.org/modules/by-module/CGI/CGI-Auth-Auto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Automatic authentication maintenance and persistence for cgi scrips.

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
%doc MANIFEST META.yml README
%doc %{_mandir}/man1/authman.1*
%doc %{_mandir}/man3/CGI::Auth::Auto.3pm*
%{_bindir}/authman
%dir %{perl_vendorlib}/CGI/
%dir %{perl_vendorlib}/CGI/Auth/
#%{perl_vendorlib}/CGI/Auth/Auto/
%{perl_vendorlib}/CGI/Auth/Auto.pm

%changelog
* Tue Feb 19 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Wed Nov 07 2007 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
