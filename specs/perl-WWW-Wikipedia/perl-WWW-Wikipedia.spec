# $Id$
# Authority: dries
# Upstream: Ed Summers <ehs$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Wikipedia

Summary: Automated interface to the Wikipedia
Name: perl-WWW-Wikipedia
Version: 1.96
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Wikipedia/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Wikipedia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Text::Autoformat)
BuildRequires: perl(URI)


%description
Automated interface to the Wikipedia.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man1/wikipedia.1*
%doc %{_mandir}/man3/WWW::Wikipedia.3pm*
%doc %{_mandir}/man3/WWW::Wikipedia::*.3pm*
%{_bindir}/wikipedia
%dir %{perl_vendorlib}/WWW/
%{perl_vendorlib}/WWW/Wikipedia/
%{perl_vendorlib}/WWW/Wikipedia.pm

%changelog
* Tue Sep 15 2009 Christoph Maser <cmr@financial.com> - 1.96-1
- Updated to version 1.96.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 1.95-1
- Updated to version 1.95.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 1.94-1
- Updated to release 1.94.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 1.93-1
- Updated to release 1.93.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.92-1
- Updated to release 1.92.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.91-1
- Initial package.

