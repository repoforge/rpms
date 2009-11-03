# $Id$
# Authority: dries
# Upstream: Simon Wistow <simon$thegestalt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Module-Pluggable

Summary: Automatically give your module the ability to have plugins
Name: perl-Module-Pluggable
Version: 3.9
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Pluggable/

Source: http://www.cpan.org/modules/by-module/Module/Module-Pluggable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Provides a simple but, hopefully, extensible way of having 'plugins' for
your module.

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
%doc Changes INSTALL MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Devel::InnerPackage.3pm*
%doc %{_mandir}/man3/Module::Pluggable.3pm*
%doc %{_mandir}/man3/Module::Pluggable::Object.3pm*
%dir %{perl_vendorlib}/Devel/
%{perl_vendorlib}/Devel/InnerPackage.pm
%dir %{perl_vendorlib}/Module/
%{perl_vendorlib}/Module/Pluggable/
%{perl_vendorlib}/Module/Pluggable.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 3.9-1
- Updated to version 3.9.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 3.8-1
- Updated to release 3.8.

* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 3.7-1
- Updated to release 3.7.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 3.6-1
- Updated to release 3.6.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.97-1
- Updated to release 2.97.

* Wed Jan  4 2006 Dries Verachtert <dries@ulyssis.org> - 2.96-1
- Initial package.
