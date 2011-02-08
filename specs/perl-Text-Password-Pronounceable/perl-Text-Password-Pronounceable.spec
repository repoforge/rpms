# $Id$
# Authority: dries
# Upstream: Thomas Sibley <tsibley@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Password-Pronounceable

Summary: Generate pronounceable passwords
Name: perl-Text-Password-Pronounceable
Version: 0.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Password-Pronounceable/

Source: http://search.cpan.org/CPAN/authors/id/T/TS/TSIBLEY/Text-Password-Pronounceable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Generate pronounceable passwords.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/Text::Password::Pronounceable*
%{perl_vendorlib}/Text/Password/Pronounceable.pm
%dir %{perl_vendorlib}/Text/Password/

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.30-1
- Updated to version 0.30.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Initial package.
