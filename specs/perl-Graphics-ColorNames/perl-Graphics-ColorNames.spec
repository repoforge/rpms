# $Id$

# Authority: dries
# Upstream: Robert Rothenberg <rrwo$cpan,org>

%define real_name Graphics-ColorNames
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Defines RGB values for common color names
Name: perl-Graphics-ColorNames
Version: 0.3901
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorNames/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RR/RRWO/Graphics-ColorNames-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module defines RGB values for common color names. The intention is
to (1) provide a common module that authors can use with other modules
to specify colors; and (2) free module authors from having to "re-invent
the wheel" whenever they decide to give the users the option of
specifying a color by name rather than RGB value.
    
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes TODO
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Graphics/ColorNames.pm
%{perl_vendorlib}/Graphics/ColorNames/*

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.3901-1
- Initial package.
