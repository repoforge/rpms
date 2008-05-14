# $Id$
# Authority: dries
# Upstream: James Bromberger <james$rcpt,to>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-IndexParser

Summary: Fetch and parse the directory index from a web server
Name: perl-WWW-IndexParser
Version: 0.9
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-IndexParser/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-IndexParser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Fetch and parse the directory index from a web server.

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
%doc %{_mandir}/man3/WWW::IndexParser.3pm*
%doc %{_mandir}/man3/WWW::IndexParser::*.3pm*
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/IndexParser/
%{perl_vendorlib}/WWW/IndexParser.pm

%changelog
* Thu May 15 2008 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
