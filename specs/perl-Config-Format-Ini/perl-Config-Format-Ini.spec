# $Id$
# Authority: dries
# Upstream: Ioannis Tambouras <inputrc$yahoo,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Format-Ini

Summary: Reads INI configuration files
Name: perl-Config-Format-Ini
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Format-Ini/

Source: http://search.cpan.org//CPAN/authors/id/I/IO/IOANNIS/Config-Format-Ini-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 4:5.8.8, perl(ExtUtils::MakeMaker)

%description
Reads INI configuration files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Config::Format::Ini*
%{perl_vendorlib}/Config/Format/Ini.pm
%{perl_vendorlib}/Config/Format/Ini/

%changelog
* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
