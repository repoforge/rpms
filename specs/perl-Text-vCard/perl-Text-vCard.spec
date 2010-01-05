# $Id$
# Authority: dries
# Upstream: Leo Lapworth <LLAP$cuckoo,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-vCard

Summary: Edit and create a single vCard (RFC 2426)
Name: perl-Text-vCard
Version: 2.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-vCard/

Source: http://search.cpan.org/CPAN/authors/id/L/LL/LLAP/Text-vCard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Slurp) >= 9999.04
BuildRequires: perl(MIME::QuotedPrint) >= 3.07
BuildRequires: perl(Test::More) >= 0.1
BuildRequires: perl(Text::vFile::asData) >= 0.05
Requires: perl(File::Slurp) >= 9999.04
Requires: perl(MIME::QuotedPrint) >= 3.07
Requires: perl(Test::More) >= 0.1
Requires: perl(Text::vFile::asData) >= 0.05

%filter_from_requires /^perl*/d
%filter_setup


%description
With this module you can create and edit a single vCard (RFC 2426).

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
%doc Changes MANIFEST META.yml TODO
%doc %{_mandir}/man3/Text::vCard.3pm*
%doc %{_mandir}/man3/Text::vCard::*.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/vCard/
%{perl_vendorlib}/Text/vCard.pm

%changelog
* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 2.04-1
- Updated to version 2.04.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 2.01-1
- Updated to release 2.01.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.00-1
- Updated to release 2.00.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.99-1
- Updated to release 1.99.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.96-1
- Updated to release 1.96.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.94-1
- Updated to release 1.94.

* Wed Mar  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.93-1
- Initial package.
