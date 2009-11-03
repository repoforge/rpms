# $Id$
# Authority: dries
# Upstream: Kang-min Liu <gugod$gugod,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Shorten-0rz

Summary: Shorten URL using 0rz.tw
Name: perl-WWW-Shorten-0rz
Version: 0.07
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Shorten-0rz/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Shorten-0rz-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(WWW::Shorten)

%description
Shorten URL using 0rz.tw.

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
%doc %{_mandir}/man3/WWW::Shorten::0rz.3pm*
%dir %{perl_vendorlib}/WWW/
%dir %{perl_vendorlib}/WWW/Shorten/
#%{perl_vendorlib}/WWW/Shorten/0rz/
%{perl_vendorlib}/WWW/Shorten/0rz.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.07-2
- Add dependency for perl(WWW::Shorten)

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.07-1
- Updated to version 0.07.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
