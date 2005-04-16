# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$ActiveState,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name PostScript-EPSF

Summary: Include external EPSF files
Name: perl-PostScript-EPSF
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PostScript-EPSF/

Source: http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/PostScript-EPSF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The PostScript::EPSF module provide the function include_epsf() that
makes it easy to include external EPSF files in your postscript
output.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
#%doc %{_mandir}/man3/*
%{perl_vendorlib}/PostScript/EPSF.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
