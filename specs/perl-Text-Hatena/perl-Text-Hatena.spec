# $Id$
# Authority: dries
# Upstream: Junya Kondo <jkondo$hatena,ne,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Hatena

Summary: Perl extension for formatting text with Hatena Style
Name: perl-Text-Hatena
Version: 0.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Hatena/

Source: http://www.cpan.org/modules/by-module/Text/Text-Hatena-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Perl extension for formatting text with Hatena Style.

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
%doc %{_mandir}/man3/Text::Hatena*
%{perl_vendorlib}/Text/Hatena.pm
%{perl_vendorlib}/Text/Hatena/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
