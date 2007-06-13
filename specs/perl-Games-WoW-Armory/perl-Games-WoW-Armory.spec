# $Id$
# Authority: dries
# Upstream: Franck Cuny <franck,cuny$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Games-WoW-Armory

Summary: Access to the WoW Armory
Name: perl-Games-WoW-Armory
Version: 0.0.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Games-WoW-Armory/

Source: http://search.cpan.org//CPAN/authors/id/F/FR/FRANCKC/Games-WoW-Armory-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Access to the WoW Armory.

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
%doc %{_mandir}/man3/Games::WoW::Armory*
%{perl_vendorlib}/Games/WoW/Armory.pm
%dir %{perl_vendorlib}/Games/WoW/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.0.3-1
- Initial package.
