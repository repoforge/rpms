# $Id$
# Authority: dries
# Upstream: Dominique Dumont <Dominique_Dumont$hp,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Vpp

Summary: Versatile text pre-processor
Name: perl-Text-Vpp
Version: 1.17
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Vpp/

Source: http://www.cpan.org/modules/by-module/Text/Text-Vpp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Vpp can handle conditional text, loop, variable substitutions in the
text.  Advanced users may also include inline perl code , inline
subroutines in the text.

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
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/vpp
%{perl_vendorlib}/Text/Vpp.pm
%{perl_vendorlib}/auto/Text/Vpp

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.
