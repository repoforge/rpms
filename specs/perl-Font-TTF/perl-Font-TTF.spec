# $Id$
# Authority: dries
# Upstream: Martin Hosken <martin_hosken$sil,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Font-TTF

Summary: TTF Fonts
Name: perl-Font-TTF
Version: 0.37
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Font-TTF/

Source: http://search.cpan.org/CPAN/authors/id/M/MH/MHOSKEN/Font-TTF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Provides: perl(ttfmod.pl)

%description
Use TTF fonts with Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}
%{__rm} -f %{buildroot}%{perl_vendorlib}/Font/TTF/Win32.pm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.TXT
%doc %{_mandir}/man?/*
#%{_bindir}/check_attach.plx
#%{_bindir}/eurofix.plx
#%{_bindir}/hackos2.plx
#%{_bindir}/psfix.plx
#%{_bindir}/ttfbuilder.plx
#%{_bindir}/ttfname.plx
#%{_bindir}/ttfremap.plx
#%{perl_vendorlib}/Font/TTF.pm
%{perl_vendorlib}/Font/TTF
%{perl_vendorlib}/ttfmod.pl

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.37-1
- Updated to release 0.37.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Initial package.
