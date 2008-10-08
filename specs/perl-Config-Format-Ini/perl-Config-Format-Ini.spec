# $Id$
# Authority: dries
# Upstream: Ioannis Tambouras <ioannis$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Format-Ini

Summary: Reads INI configuration files
Name: perl-Config-Format-Ini
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Format-Ini/

Source: http://www.cpan.org/modules/by-module/Config/Config-Format-Ini-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.8
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 4:5.8.8

%description
Reads INI configuration files.

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
%doc Changes Debian_CPANTS.txt MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Config::Format::Ini.3pm*
%doc %{_mandir}/man3/Config::Format::Ini::*.3pm*
%dir %{perl_vendorlib}/Config/
%dir %{perl_vendorlib}/Config/Format/
%{perl_vendorlib}/Config/Format/Ini/
%{perl_vendorlib}/Config/Format/Ini.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.07-1
- Updated to release 0.07.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
