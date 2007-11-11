# $Id$
# Authority: dries
# Upstream: Ed Summers <ehs$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Wikipedia

Summary: Lookup an entry in the wikipedia
Name: perl-WWW-Wikipedia
Version: 1.92
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Wikipedia/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Wikipedia-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Lookup an entry in the wikipedia.

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
%doc %{_mandir}/man3/WWW::Wikipedia*
%doc %{_mandir}/man1/wikipedia*
%{_bindir}/wikipedia
%{perl_vendorlib}/WWW/Wikipedia.pm
%{perl_vendorlib}/WWW/Wikipedia/

%changelog
* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.92-1
- Updated to release 1.92.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.91-1
- Initial package.

