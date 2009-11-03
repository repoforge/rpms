# $Id$
# Authority: dries
# Upstream: Sascha Kiefer <perl$intertivityNOSP4M,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Prototype

Summary: Generate HTML and Javascript for the Prototype library
Name: perl-HTML-Prototype
Version: 1.48
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Prototype/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Prototype-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Generate HTML and Javascript for the Prototype library.

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
%doc %{_mandir}/man3/HTML::Prototype*
%{perl_vendorlib}/HTML/Prototype.pm
%{perl_vendorlib}/HTML/Prototype/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.48-1
- Initial package.
