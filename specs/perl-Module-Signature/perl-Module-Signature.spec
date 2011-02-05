# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#40179;&#9787; <autrijus$autrijus,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Signature

Summary: Check and create SIGNATURE files for CPAN distributions
Name: perl-Module-Signature
Version: 0.66
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Signature/

#Source: http://www.cpan.org/modules/by-module/Module/Module-Signature-%{version}.tar.gz
Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Module-Signature-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: gnupg
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(IO::Socket::INET)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.005
Requires: gnupg
BuildRequires: perl(Digest::SHA)
Requires: perl(IO::Socket::INET)
Requires: perl >= 5.005

%filter_from_requires /^perl*/d
%filter_setup


%description
A module to check and create SIGNATURE files for CPAN distributions.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/cpansign*
%{_bindir}/cpansign
%{perl_vendorlib}/Module/Signature.pm

%changelog
* Sat Feb 05 2011 Denis Fateyev <denis@fateyev.com> - 0.66-1
- Updated to version 0.66.

* Fri Dec 11 2009 Christoph Maser <cmr@financial.com> - 0.61-1
- Updated to version 0.61.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.55-1
- Updated to release 0.55.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.54-1
- Updated to release 0.54.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.50-1
- Initial package.
