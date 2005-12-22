# $Id$
# Authority: dries
# Upstream: Jeremy D. Zawodny <Jeremy$Zawodny,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-METAR

Summary: Accesses Aviation Weather Information
Name: perl-Geo-METAR
Version: 1.14
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-METAR/

Source: http://search.cpan.org/CPAN/authors/id/J/JZ/JZAWODNY/Geo-METAR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
With this module, you can access Aviation Weather Information.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HACKING README TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Geo/METAR.pm

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
